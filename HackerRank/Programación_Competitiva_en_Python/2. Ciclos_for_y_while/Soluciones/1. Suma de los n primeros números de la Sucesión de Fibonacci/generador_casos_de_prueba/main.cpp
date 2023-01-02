#include <bits/stdc++.h>

using namespace std;

const long long MAX = 1e9;
long long fibonacci[55];


int main(){

    fibonacci[1] = fibonacci[2] = 1;
    for (int i = 3; i <= 50; ++i)
         fibonacci[i] = fibonacci[i-1] + fibonacci[i-2];

    for (int i = 1; i <= 50; ++i){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");

         int n = i;
         long long suma = 0;
         for (int j = 1; j <= n; ++j)
              suma += fibonacci[j];

         fprintf(in,"%d", n);
         fprintf(out,"%lld", suma);

         fclose(in);
         fclose(out);
    }



    return 0;
}
