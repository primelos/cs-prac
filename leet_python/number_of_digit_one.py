# Given an integer n, count the total number of digit 1 appearing in
#  all non-negative integers less than or equal to n.

# Example:

# Input: 13
# Output: 6 
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

class Solution:
    def countDigitOne(self, n: int) -> int:
        
        if n <= 0:
            return 0
    
        iCount = 0
        iFactor = 1
        iLowerNum, iCurNum, iHigherNum = 0, 0, 0
        
        while n // iFactor != 0:
            iLowerNum = n - (n // iFactor) * iFactor
            iCurNum = (n // iFactor) % 10
            iHigherNum = n // (iFactor * 10)
            
            if iCurNum == 0:
                iCount += iHigherNum * iFactor
            elif iCurNum == 1:
                iCount += iHigherNum * iFactor + (iLowerNum + 1)
            else:
                iCount += (iHigherNum + 1) *iFactor
            iFactor *= 10
        return iCount