import fileinput
import sys
path = '/Users/zhongcheng/PycharmProjects/hello/test'
# with open(path, 'r') as f:
#     lines = f.readlines()
# with open(path, 'w') as fp:
#     for line in lines:
#         if line.startswith('a = '):
#             fp.write(line.replace('a = \d', 'a = 3'))
#         else:
#             fp.write(line)

for line in fileinput.FileInput("test", inplace=True):
    if line.strip().startswith('d = '):
        line  = 'c = 22\n'
    sys.stdout.write(line)






# with open(path,'w') as write:
#     if line.startswith('a='):
#         write.write('a = 3')
#     else: write.write(line)
