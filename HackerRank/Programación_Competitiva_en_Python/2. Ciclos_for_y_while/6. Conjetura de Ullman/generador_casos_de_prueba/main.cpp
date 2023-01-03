#include <bits/stdc++.h>

using namespace std;

const long long MAX = 1e6;

int main(){

    srand(time(0));

    for (int i = 1; i <= 50; ++i){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");


         long long x = rand() % MAX + 1;
         fprintf(in,"%lld", x);

         int pasos = 0;
         while (x > 1){
            if (x % 2 == 0)
                x /= 2;
            else
                x = x*3 + 1;
            pasos ++;
         }


         fprintf(out,"%lld", pasos);

         fclose(in);
         fclose(out);
    }



    return 0;
}
