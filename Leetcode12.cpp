class Solution {
public:
    string intToRoman(int num) {
        string a[] = {"", "M", "MM", "MMM"};
        string b[] = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        string c[] = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        string d[] = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
        return a[num/1000]+b[num%1000/100]+c[num%100/10]+d[num%10];
    }
};