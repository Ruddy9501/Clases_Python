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

         int hh = rand() % 99 + 1;
         int mm = rand() % 59 + 1;

         fprintf(in,"%.2d:%.2d", hh, mm);
         fprintf(out,"%d", hh*60+mm);

         fclose(in);
         fclose(out);
    }



    return 0;
}
