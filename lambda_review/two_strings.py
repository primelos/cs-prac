# Given two strings, determine if they share a common substring. A substring may be as small as one character.

# For example, the words "a", "and", "art" share the common substring a. The words "be" and "cat" do not share a substring.

# Function Description

# Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

# twoStrings has the following parameter(s):

# s1, s2: two strings to analyze .
# Input Format

# The first line contains a single integer p, the number of test cases.

# The following p pairs of lines are as follows:

# The first line contains string s1.
# The second line contains string s2.
# Constraints

# s1 and s2 consist of characters in the range ascii[a-z].
# 1<= p <=10
# 1<= a1, s2 <= 10^5

# Output Format

# For each pair of strings, return YES or NO.

# Sample Input

# 2
# hello
# world
# hi
# world
# Sample Output

# YES
# NO
# Explanation

# We have  pairs to check:

# , . The substrings  and  are common to both strings.
# , .  and  share no common substrings.


# def two_strings(s1, s2):
#     data = set()
#     for char in s1:
#         data.add(char)
#     for i in range(len(s2)):
#         if s2[i] in data:
#             return 'Yes'
#     return 'No'

# def two_strings(s1, s2):
#     new_set = set(s1)
#     for char in s2:
#         if char in new_set:
#             return 'Yes'
#     return 'No'

def two_strings(s1, s2):
    s1_dict = {}
    answer =[]
    s1_subs = allSubstring(s1)
    s2_subs = allSubstring(s2)
    for sub in s2_subs:
        if sub in s1_subs:
            answer.append(sub)
        else:
            return None
    return answer
def allSubstring(s):
    set_str = set()
    
    for i in range(len(s)):
        for j in range(i + 1, len(s)+1):
            set_str.add(s[i:j])
    return set_str


print(two_strings("string", "ring"))