class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if(n==0) return 1;
        if(n==1) return 10;
        int count = 10;
        int product = 9;
        for (int i=1;i<n&&i<10;i++){
            product *= (10-i);
            count += product;
        }
        return count;
    }
};