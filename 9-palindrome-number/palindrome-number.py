class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        new_x = str(x)

        x_list = []

        for char in new_x:
            x_list.append(char)

        y_list = x_list[:]

        y_list.reverse()

        if x_list == y_list:
            return True
        else:
            return False


