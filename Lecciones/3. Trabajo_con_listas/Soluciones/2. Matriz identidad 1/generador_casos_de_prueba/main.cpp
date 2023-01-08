#include <bits/stdc++.h>

using namespace std;

const long long MAX = 50;

int main(){

    srand(time(0));

    for (int i = 3; i <= 50; ++i){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");


         int n = rand() % MAX + 1;
         int m = rand() % MAX + 1;
         int a[n][m], tot = 0;

         fprintf(in,"%d %d\n", n, m);
         for (int j = 0; j < n; ++j){
              for (int k = 0; k < m; ++k){
                   int x = (j == k ? 1 : 0);
                   fprintf(out,"%d", x);
                   if (k < m-1) fprintf(out," ");
              }
              fprintf(out,"\n");
         }

         fclose(in);
         fclose(out);
    }



    return 0;
}
