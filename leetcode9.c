bool isPalindrome(int x) {
    int length=0, pre, post, i;
    int tmp = x;
    if(x<0)
        return false;
    if(x<10)
        return true;
    while((tmp=tmp/10)!=0)
        length++;
    pre=pow(10,length);
    post=1;
    while(pre>=post){
        if(x/pre%10 != x/post%10)
            return false;
        pre /= 10;
        post *= 10;
    }
    return true;
}