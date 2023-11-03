class Solution {
public:
    
    bool isItPossible(char s1, char s2) {
          if(s1 == 'z') s1 = 'a';
          else s1 = (char)(int)s1 + 1;
          return s1 == s2;
    }
    
    bool canMakeSubsequence(string str1, string str2) {
        int first = 0;
        
        if(str2.size() > str1.size())return false;
        
        for(int index = 0; index < str1.size(); index++) {
                
               if(str1[index] == str2[first] or isItPossible(str1[index], str2[first])) {
                   first += 1;
                   if(first == str2.size()) {
                       return true;
                   }
               }
        }
        
        return false;
    }
};