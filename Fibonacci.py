#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
class Solution:
    def Fibonacci(self , n: int) -> int:
        # write code here
        fib_x = 0
        if n == 1 or n == 2:
            fib_x = 1
        else:
            fib_1 = 1
            fib_2 = 1
            for i in range(3, n+1):
                fib_x = fib_1 + fib_2
                fib_2 = fib_1
                fib_1 = fib_x
        return fib_x
