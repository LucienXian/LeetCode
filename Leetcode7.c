int reverse(int x) {
    int top=0,flag=0;
    int i=1;
    long long result=0;
    long long a[64];
    if(x<0){
        flag=1;
        x=-x;
    }
    while(x>0){
        a[top++]=x%10;
        x/=10;
    }
    top--;
    while(top>=0){
        result+=a[top--]*i;
        i*=10;
    }
    if(flag)
        result = -result;
    return (result>INT_MAX||result<INT_MIN)?0:result;
}