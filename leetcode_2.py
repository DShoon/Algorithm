class Solution(object):
    def palindrome(self, user_input):
        strs = []
        for char in user_input:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True


word1 = "asdsa"
word2 = "this is not real"
word3 = "Asdsa"

solution = Solution()
res = solution.palindrome(word1)
print(res)

res2 = solution.palindrome(word2)
print(res2)

res3 = solution.palindrome(word3)
print(res3)
