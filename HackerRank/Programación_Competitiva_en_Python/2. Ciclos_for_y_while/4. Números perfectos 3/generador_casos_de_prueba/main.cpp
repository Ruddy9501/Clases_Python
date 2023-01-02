#include <bits/stdc++.h>

using namespace std;

const long long MAX = 1e9;

int main(){

     srand(time(0));

     string input_name = "input00.txt";
     string output_name = "output00.txt";

     FILE* in = fopen(input_name.c_str(), "w");
     FILE* out = fopen(output_name.c_str(), "w");


     int a = 6, b = 28;
     fprintf(in,"%d %d", a, b);
     vector <int> v;
     for (int i = a; i <= b; ++i){
          int sum = 0;
          for (int j = 1; j < i; ++j)
               if (i % j == 0)
                   sum += j;
          if (sum == i)
              v.push_back(i);
     }

     if ((int)v.size())
        fprintf(out,"%d", v[0]);
     for (int i = 1; i < (int)v.size(); ++i)
          fprintf(out," %d", v[i]);

     fclose(in);
     fclose(out);




    return 0;
}
