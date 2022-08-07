#include <stdio.h>
int main() {
    int n,check=0,twopower=1;
    scanf("%d",&n);
    while(n>=twopower)
    {
        if(n==twopower)
        {
            printf("YES\n");
            check=1;
        }
        twopower*=2;
    }
    if(check==0)
    {
        printf("NO\n");
    }
    return 0;
}
