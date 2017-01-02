//cpp
int lengthOfLongestSubstring(string s) {  
  int n = s.length();  
  int i = 0, j = 0;  
  int maxLen = 0;  
  bool exist[256] = { false };  
  while (j < n) {  
    if (exist[s[j]]) {  
      maxLen = max(maxLen, j-i);  
      while (s[i] != s[j]) {  
        exist[s[i]] = false;  
        i++;  
      }  
      i++;  
      j++;  
    } else {  
      exist[s[j]] = true;  
      j++;  
    }  
  }  
  maxLen = max(maxLen, n-i);  
  return maxLen;  
} 
//C
int lengthOfLongestSubstring(char* s) {
    int length, head, tail, max, exit[256];
    length = strlen(s);
    memset(exit, 0, 256*sizeof(int));
    head = tail = max = 0;
    while(tail<length){
        if(exit[s[tail]]){
            max = (max>tail-head)? max:(tail-head);
            while(s[head]!=s[tail]){
                exit[s[head]] = 0;
                head++;
            }
            head++;
            tail++;
        }
        else
            exit[s[tail++]] = 1;
    }
    max = (length-head>max)? (length-head):max;
    return max;
}

/*int lengthOfLongestSubstring(char* s) {
    int Count, Max, i, j, Flag, Top, k;
    char Temp[10000];
    Count = Max = i = j = Flag = Top = 0;
    while(s[i]){
        while(Temp[j])
            if(Temp[j++]==s[i]){
                Flag = 1;
                k = j;
            }
        if(!Flag){
            Count++;
            Temp[Top] = s[i]; 
            i++;
            Top++;
        }
        else{
            Count = (Top-k)+1;
            Flag = 0;
            i++;
        }
        Max = (Count>Max)? Count : Max;
        j = 0;
    }
    return Max;
}

