#include <bits/stdc++.h>

using namespace std;

const int MAX = 1e9;

int main(){

    srand(time(0));

    for (int i = 1; i <= 50; ++i){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");

         int n = rand() % MAX + 1;
         int temp = n, nn = 0;
         while (temp){
             nn += (temp%10);
             temp /= 10;
         }

         fprintf(in,"%d", n);
         fprintf(out,"%d", nn);

         fclose(in);
         fclose(out);
    }



    return 0;
}
