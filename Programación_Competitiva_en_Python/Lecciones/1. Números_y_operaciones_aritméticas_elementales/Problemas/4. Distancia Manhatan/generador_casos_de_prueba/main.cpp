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

         int x1 = rand() % 2001 - 1000;
         int y1 = rand() % 2001 - 1000;
         int x2 = rand() % 2001 - 1000;
         int y2 = rand() % 2001 - 1000;

         int d = abs(x1-x2) + abs(y1-y2);

         fprintf(in,"%d %d\n%d %d", x1, y1, x2, y2);
         fprintf(out,"%d", d);

         fclose(in);
         fclose(out);
    }



    return 0;
}
