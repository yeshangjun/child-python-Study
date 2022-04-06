# import turtle as t
import numpy as np
"""
九连环的规则:
1. 第n环上
n环为下状态，只有n-1环在上面，1:n-2环都在下面
2. 第n环下
n，n-1环为上状态，1:n-2都在下面
"""
UP = 1
DOWN = 0


class nCircle:
    """

    """
    def __init__(self, size, state):
        self.size = size
        self.state = state
        self.statelist = np.ones(self.size+1)*self.state
        # 为了方便理解，list[0]忽略，list[1:n+1]为n环状态
        self.count = 1

    def uninstallCircle(self, n):
        """

        :param n:
        :return:
        """
        # 拆卸环，该函数的作用是拆卸第n个环
        # n = self.size
        if n >= 3:
            if self.statelist[n-1] == DOWN:
                # 当第n-1个环已拆卸（状态1），调用安装环安装，安装第n-1个环
                self.installCircle(n-1)
            # 遍历第n-2,n-3……1个环，如果处于已安装状态（0），调用拆卸环函数，使对应环处于已拆卸状态（
            for i in range(n-2, 0, -1):
                if self.statelist[i] == UP:
                    self.uninstallCircle(i)
            self.statelist[n] = DOWN
            print('第', self.count, '步，取下第', n, '个环')
            self.count += 1
        elif n == 1:
            if self.statelist[n] == UP:
                self.statelist[n] = DOWN
                print('第', self.count, '步，取下第1个环')
                self.count += 1
        elif n == 2:
            if self.statelist[n - 1] == DOWN:
                self.installCircle(n - 1)
                self.statelist[n] = DOWN
                print('第', self.count, '步，取下第', n, '个环')
                self.count += 1
            elif self.statelist[n - 1] == UP:
                self.statelist[n] = DOWN
                print('第', self.count, '步，取下第', n, '个环')
                self.count += 1

    def installCircle(self, n):
        # 安装环，该函数的作用是安装第n个环
        # n = self.size
        if n >= 3:
            if self.statelist[n - 1] == DOWN:
                # 当第n-1个环已拆卸（状态1），调用安装环安装，安装第n-1个环
                self.installCircle(n - 1)
            # 遍历第n-2,n-3……1个环，如果处于已安装状态（0），调用拆卸环函数，使对应环处于已拆卸状态（
            for i in range(n - 2, 0, -1):
                if self.statelist[i] == UP:
                    self.uninstallCircle(i)
            self.statelist[n] = UP
            print('第', self.count, '步，安装第', n, '个环')
            self.count += 1
        elif n == 1:
            if self.statelist[n] == DOWN:
                self.statelist[n] = UP
                print('第', self.count, '步，安装第1个环')
                self.count += 1
        elif n == 2:
            if self.statelist[n - 1] == DOWN:
                self.installCircle(n - 1)
                self.statelist[n] = UP
                print('第', self.count, '步，安装第', n, '个环')
                self.count += 1
            elif self.statelist[n - 1] == UP:
                self.statelist[n] = UP
                print('第', self.count, '步，安装第', n, '个环')
                self.count += 1


if __name__ == '__main__':
    step = 9
    Nine = nCircle(step, UP)
    # Nine.size = 9
    # Nine.state = DOWN
    for it in range(step, 0, -1):
        Nine.uninstallCircle(it)
        # Nine.installCircle(i)
