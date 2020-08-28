# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string 
# inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra 
# white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not
#  contain any digits and that digits are only for those repeat 
# numbers, k. For example, there won't be input like 3a or 2[4].

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:

# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"

class Solution:
    def decodeString(self, s: str) -> str:
        letters, number, stack = '', 0, []

        for i in s:
            if i == '[':
                stack.append([letters, number])
                letters = ''
                number = 0
            elif i.isdigit():
                number = (number * 10) + int(i)
            elif i == ']':
                temp = stack.pop()
                one = temp[0]
                two = temp[1] * letters
                letters = one + two
            else:
                letters += i


        return letters

test = Solution()
print(test.decodeString('2[d3[a2[bc]]]'))