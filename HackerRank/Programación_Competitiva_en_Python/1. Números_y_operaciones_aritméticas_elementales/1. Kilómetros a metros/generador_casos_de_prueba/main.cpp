#include <bits/stdc++.h>

using namespace std;

const long long MAX = 1e9;

int main(){

    srand(time(0));

    for (int i = 1; i <= 50; ++i){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");

         long long distancia_m = rand() % MAX + 1;
         long long distancia_k = distancia_m * 1000;

         fprintf(in,"%lld", distancia_m);
         fprintf(out,"%lld", distancia_k);

         fclose(in);
         fclose(out);
    }



    return 0;
}
