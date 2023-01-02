#include <bits/stdc++.h>

using namespace std;

const long long MAX = 1e9;

int main(){

    srand(time(0));

    int n = 1;
    for (int i = 1; i <= 10; ++i, n += 2){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");



         fprintf(in,"%lld", n);

         int mid = (n+1) / 2;
         for (int j = 1; j <= n; ++j){
              for (int k = 1; k <= n; ++k){
                   int d1 = min(n-j, j-1) + min(n-k, k-1);
                   int d2 = abs(j - mid) + abs(k - mid);
                   if (d2 <= d1)
                       fprintf(out,"*");
                   else fprintf(out," ");

                   if (k == n) fprintf(out, "\n");
                   else fprintf(out, " ");
              }


         }

         fclose(in);
         fclose(out);
    }



    return 0;
}
