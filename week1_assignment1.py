#include <stdio.h>
int main() {
    int T,N,i,points;
    scanf("%d",&T);
    for(i=0;i<T;i++)
    {
        points=0;
        scanf("%d",&N);
        points=(N*(N-1))/2;
        printf("%d\n",points);
    }
    return 0;
}
