#include <iostream>
#include <string>
#include <random>
#include <vector>
#include <ctime>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

void remove_zeroes(double number, char * result, int buf_len) { 
    char * pos;
    int len;

    snprintf(result, buf_len, "%lf", number);
    len = strlen(result);
    pos = result + len - 1;
    
    #if 0
    while(*div != '.')
        div++;
    #endif

    while (*pos == '0')
        *pos-- = '\0';

    if (*pos == '.')
        *pos = '\0';
}

int main() {
    srand((unsigned) time(NULL)); 
    cout.precision(2);

    const long long MAX_ITERS = 1e8;
    char s[81];
    
    int c;
    float time;
    float last_time;
    
    vector <long long> chests(400);
    vector <float> percentage(400);
    
    for (long long i=0; i<MAX_ITERS; i++) {
        c = 0;
        for (int x=0; x<400; x++) {
            if ((float) rand()/RAND_MAX <= 0.0425) {
                c++;
            }
        }
        chests[c] += 1;

        if (i == 0.01*MAX_ITERS) {
            time = clock() / 1e6;
            cout << fixed << "Примерное время: " << time*100 / 60. << 'm' << endl;
        }

        if (i % (MAX_ITERS / 10) == 0 && i != 0) {
            cout << 100. * i/MAX_ITERS << "% ";
            cout << time*100 * (1 - i*1.0/MAX_ITERS) << 's' << endl;
        }
    }
    cout << endl;

    for (int i=0; i<400; i++) {
        percentage[i] = (float) chests[i] / MAX_ITERS;
    }

    for (int i=10; i<=70; i++) {
        if (17==i || 20==i || 24==i || 25==i || 28==i || 30==i || i>=40 && percentage[i]!=0) {
            remove_zeroes(percentage[i] * 100., s, 81);
            cout << "Для " << i << ": ";
            cout << chests[i] << " " << s << '%' << endl;
        }
    }
    
    float summ;
    for (int i=0; i<400; i++){ summ += percentage[i]; }
    remove_zeroes(summ, s, 81);
    cout << "\nСумма: " << s << endl;

    summ = 0.;
    for (int i=0; i<17; i++) { summ += percentage[i]; }
    remove_zeroes(summ*100, s, 81);
    cout << "До 17: " << s << '%' << endl;
    
    summ = 0.;
    for (int i=17; i<400; i++) { summ += percentage[i]; }
    remove_zeroes(summ*100, s, 81);
    cout << "После 17: " << s << '%' << endl;
    
    summ = 0.;
    for (int i=14; i<20; i++) { summ += percentage[i]; }
    remove_zeroes(summ*100, s, 81);
    cout << "От 14 до 20: " << s << '%' << endl;
    
    summ = 0.;
    for (int i=20; i<30; i++) { summ += percentage[i]; }
    remove_zeroes(summ*100, s, 81);
    cout << "От 20 до 30: " << s << '%' << endl;
    
    summ = 0.;
    for (int i=30; i<400; i++) { summ += percentage[i]; }
    remove_zeroes(summ*100, s, 81);
    cout << "От 30: " << s << '%' << endl;

    cout << "\nОбщее время: " << (float) clock() / 60e6 << 'm' << endl;
    return 0;
}
