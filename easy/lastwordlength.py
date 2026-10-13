class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        i = len(s)-1
        # this provides length of all characters except for the white spaces
        # while i>= 0:
        #     if (s[i]==" "):
        #         i-=1
        #     else:
        #         length+=1
        #         i-=1
        # return length 
        
        # this provides length of the last character
        while i>= 0 and s[i] == " " :
            i-=1
        while i>= 0 and s[i] != " " :
            length+=1
            i-=1
        return length

        # returns lenth of the 1st word 
        # j = 0
        # while j<=len(s)-1 and s[j] == " ":
        #     j+=1
        # while j<=len(s)-1 and s[j] != " ":
        #     length +=1
        #     j+=1
        # return length


length = Solution()
s = "cat world"
x =length.lengthOfLastWord(s)
print(x)