class Solution(object):
    def palindrome(self, user_input):
        for i in range(len(user_input)//2):
            if user_input[i] != user_input[len(user_input)-1-i]:
                return False
            else:
                pass
        return True


word1 = "asdsa"
word2 = "this is not real"

solution = Solution()
res = solution.palindrome(word1)
print(res)

res2 = solution.palindrome(word2)
print(res2)
