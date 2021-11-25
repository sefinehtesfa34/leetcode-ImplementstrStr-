class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        self.needle=needle.lower()
        self.haystack=haystack
        val=0
        if len(self.needle)==0:
            return 0
        if not self.needle in self.haystack:
            return -1
        return self.haystack.index(self.needle)
        
                    
                
            
        
