# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

class Solution:
    '''
    x = 16
    [0,x]  check ever number from 0 to x 
    
    '''

    def mySqrt(self, x: int) -> int:
        
        # using BINARY search
        min, max = 0, x
        res = 0
        while min <= max:
            mid = int(( min + max ) / 2)
            squared = mid * mid
            if squared == x:
               return mid
            elif squared > x:
                print('greater')
                max = mid - 1
            else:
                print('hit')
                min = mid + 1
                res = mid

        return res
       
  
        #    using a FOR loop
        '''   
            if isinstance(x, str) == True:
                return 'no letters'
            else:
                for i in range(0, x + 1): # x + 1 is needed so that we don't return -1 with input 0
                    print('i',i)
                    squared = i * i
                    if squared == x:
                        return i
                    elif squared > x:
                        return i - 1
                
                return None
        '''


newtest = Solution()

print(newtest.mySqrt(21))

