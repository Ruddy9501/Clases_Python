#include <bits/stdc++.h>

using namespace std;

int main(){

    srand(time(0));

    for (int i = 1; i <= 50; ++i){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");

         int n = rand() % 900 + 100;
         int d1 = n / 100;
         int d2 = (n / 10) % 10;
         int d3 = n % 10;
         int nn = d1*10 + d2 + d3;

         fprintf(in,"%d", n);
         fprintf(out,"%d", nn);

         fclose(in);
         fclose(out);
    }



    return 0;
}
