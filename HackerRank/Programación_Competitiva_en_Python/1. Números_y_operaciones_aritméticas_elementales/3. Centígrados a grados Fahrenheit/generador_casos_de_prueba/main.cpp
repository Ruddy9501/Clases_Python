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

         int c = rand() % 201 - 100;
         double f = 1.0 * c * 9 / 5 + 32;

         fprintf(in,"%d", c);
         fprintf(out,"%.5lf", f);

         fclose(in);
         fclose(out);
    }



    return 0;
}
