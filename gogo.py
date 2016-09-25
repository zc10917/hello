path = '/Users/zhongcheng/PycharmProjects/hello/3.txt'
pathR = '/Users/zhongcheng/PycharmProjects/hello/2.txt'
import ui
import codecs


def init():
    with codecs.open(path, 'r', 'ISO-8859-1') as f:
        line = f.readline()
        while line:
            do(line)
            line = f.readline()


def do(line):
    User = line.split('\t')
    if not len(User) == 0:
        User = User[0:2]
        print(User)
        u = ui.start(User)

        if not u is None:
            with open(pathR, 'a') as write:
                write.write('\n')
                for key in u:
                    write.write(key + '\t')
                write.write('\n')
        print(u)


if __name__ == '__main__':
    init()
