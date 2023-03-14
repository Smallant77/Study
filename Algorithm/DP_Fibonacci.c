#include <stdio.h>

/*Memoiztion : Top-Down 가끔 재귀 횟수 제한 오류가 걸릴 수도 있음
int fibo(int n){
    int a;
    int d[30] = {0};
    if((n==1)||(n==2)) return 1;
    if(d[n] != 0){
        return d[n];
    }
    d[n] = fibo(n-1) + fibo(n-2);
    return d[n];
}

int main(void){
    int x, result;
    scanf("%d", &x);
    result = fibo(x);
    printf("%d", result);
}*/


/*Bottom-Up
int fibo(int n){
    int a;
    int d[30];
    d[0] = 0;
    d[1] = 1;

    for (a = 2; a<=n; a++){
        d[a] = d[a-2] + d[a-1];
    }
    return d[n];
}

int main(){
    int x, result;
    scanf("%d", &x);
    result = fibo(x);
    printf("%d", result);
}*/
