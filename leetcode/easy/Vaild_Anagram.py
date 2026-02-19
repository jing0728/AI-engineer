
##sort both strings and compare them. If they are equal, they are anagrams.O(n log n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
          return sorted(s) == sorted(t)#The sorted() function sorts the characters of both strings and compares the sorted lists. If they are equal, the original strings are anagrams.


#hash map O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False#len different return false
        
        count={}#hash map

        for c in s:
            count[c]=count.get(c,0)+1#count s get into hash map
        
        for c in t:
            if c not in count:
                return False
            count[c]-=1#compare with t if same then it's anagram
            if count[c]<0:
                return False
        
        return True
    
#counter O(n)
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)#Counter counts the frequency of each character in both strings and compares the resulting dictionaries. If they are equal, the strings are anagrams.
