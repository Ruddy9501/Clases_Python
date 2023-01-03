#include <bits/stdc++.h>

using namespace std;

const long long MAX = 100;

int main(){

srand(time(0));

for (int i = 1; i <= 50; ++i){

	 string number_case = (i > 9 ? to_string(i) : "0" + to_string(i));
	 string input_name = "input" + number_case + ".txt";
	 string output_name = "output" + number_case + ".txt";

	 FILE* in = fopen(input_name.c_str(), "w");
	 FILE* out = fopen(output_name.c_str(), "w");

	 int a[2][2][2], b[2][2], tot = 0;

     for (int l = 0; l < 2; l++){
         for (int j = 0; j < 2; ++j){
              for (int k = 0; k < 2; ++k){

                   a[j][k][l] = rand() % 10 + 1;

                   fprintf(in,"%d", a[j][k][l]);
                   if (k < 1) fprintf(in," ");
              }
              fprintf(in,"\n");
         }
         fprintf(in,"\n");
     }

	 for (int j = 0; j < 2; ++j){
		  for (int k = 0; k < 2; ++k){
			   b[j][k] = 0;
			   for (int l = 0; l < 2; ++l){
                    b[j][k] += a[j][l][0]*a[l][k][1];
			   }

               fprintf(out,"%d", b[j][k]);
			   if (k < 1) fprintf(out," ");
		  }
		  fprintf(out,"\n");

	 }

	 fclose(in);
	 fclose(out);
}



return 0;
}
