//O(n)
int maxArea(int* height, int heightSize) {
    int l=0, r=heightSize-1, max, water=0;
    while(l<r){
        max = (r-l)*(height[l]>=height[r] ? height[r--]:height[l++]);  //skip the shorter line, not two lines at the same time 
        //max = (height[l]>=height[r] ? height[r--]:height[l++]) * (r-l);
        //r--;l++
        if(max>water)
            water=max;
    }
    return water;
}