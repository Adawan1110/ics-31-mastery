# Last updated: 1/23/2026, 9:11:43 AM
1class Solution(object):
2    def isPalindrome(self, x):
3        """
4        :type x: int
5        :rtype: bool
6        """
7
8        new_x = str(x)
9
10        x_list = []
11
12        for char in new_x:
13            x_list.append(char)
14
15        y_list = x_list[:]
16
17        y_list.reverse()
18
19        if x_list == y_list:
20            return True
21        else:
22            return False
23
24
25