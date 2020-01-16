#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int i;
int main() {
    vector<char> P(9);
    vector<char>::iterator b,e;
    b=P.begin();
    e=P.end();
    for (i=0;i<9;i++) P[i]=i+1;
    i=0;
    do {
        if (P[0]+P[1]+P[3]==12&& P[0]+P[2]+P[5]==12&& P[3]+P[4]+P[5]==12) 
		{
            printf("Èý½ÇÐÎ%d:\n",++i);
            printf("  %d\n"    ,    P[0]      );
            printf(" %d %d\n"  ,  P[1],P[2]   );
            printf("%d %d %d\n",P[3],P[4],P[5]);
        }
    } 
	while (next_permutation(b,e));
    printf("The total: %d",i);
    return 0;
}
