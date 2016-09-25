import fileinput
import re
import sys

path = '/Users/zhongcheng/PycharmProjects/hello/1.txt'
pathR = '/Users/zhongcheng/PycharmProjects/hello/2.txt'
import ui


def init():
    with open(path, 'r') as f:
        line = f.readline()
        while line:
            do(line)
            line = f.read()


def do(line):
    i=0
    i+=1
    print(i)
    print(line)
    User = line.split('\t')
    # print(User)

    # if not len(User) == 0:
    #     User[1] = User[1].replace('\n', '')
    #     u = ui.start(User)
    #     if not u is None:
    #         with open(pathR, 'a') as write:
    #             write.write('\n')
    #             for key in u:
    #                 write.write(key + '\t')
    #             write.write('\n')
    #     print(u)


if __name__ == '__main__':
    init()
