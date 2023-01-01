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

         int a = rand() % 100 + 1;
         int b = rand() % 100 + 1;
         int c = rand() % 100 + 1;

         while (a+b <= c || a+c <= b || c+b <= a){
                a = rand() % 100 + 1;
                b = rand() % 100 + 1;
                c = rand() % 100 + 1;
         }

         double S = 1.0 * (a+b+c) / 2;
         double A = sqrt(S*(S-a)*(S-b)*(S-c));

         fprintf(in,"%d %d %d", a, b, c);
         fprintf(out,"%d", int(A));

         fclose(in);
         fclose(out);
    }



    return 0;
}
