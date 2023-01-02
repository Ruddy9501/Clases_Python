#include <bits/stdc++.h>

using namespace std;

const long long MAX = 1e9;

int main(){

    srand(time(0));

    for (int i = 3; i <= 50; ++i){

         string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
         string input_name = "input" + number_case + ".txt";
         string output_name = "output" + number_case + ".txt";

         FILE* in = fopen(input_name.c_str(), "w");
         FILE* out = fopen(output_name.c_str(), "w");


         long long x = rand() % MAX + 1;

		 long long sum = 0, j = 0;
		 while (sum <= x){
			 j++;
			 sum += j*j;
		 }

         fprintf(in,"%lld", x);
         fprintf(out,"%lld", j);

         fclose(in);
         fclose(out);
    }



    return 0;
}
