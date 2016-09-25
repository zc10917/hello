#!/usr/bin/env python

# python pay_auto_commit.py {project} {version} [{branch}] [{path}]

import re
import sys
import os
import os.path
import string
import fileinput

__project_name__ = {"pay-common": 0, "meituanpay": 1, "cashier": 2, "barcodecashier": 3, "wallet": 4, "pay-demo": 5}
__project_code__ = {0: "pay-common", 1: "meituanpay", 2: "cashier", 3: "barcodecashier", 4: "wallet", 5: "pay-demo"}


def commit_project(path, project_name):
    print('{project} start prepare'.format(project=project_name))
    os.chdir("./" + project_name)
    if os.popen("git stash").read().strip().startswith('No loacal changes to save'):
        need_save = False
    else:
        need_save = True
    if len(sys.argv) > 3:
        branch = sys.argv[3]
    else:
        branch = 'develop'
    if os.popen('git checkout {branch}'.format(branch=branch)).read().strip().startswith('Already on'):
        is_change_branch = True
    else:
        is_change_branch = False
    os.system('git checkout -b auto_update_{version}'.format(version=sys.argv[2]))
    change_version(project_name)
    os.system('git add .')
    os.system('git commit -m \'update version {version}\''.format(version=sys.argv[2]))
    branchName = sys.argv[2]

    os.system('stash pull-request '+branchName+' origin/occc -T '+'\"branchName\"'+' @chenbosheng')
    print('{project} commit complete'.format(project=project_name))
    os.system(('git tag aar_{version}'.format(version=sys.argv[2])))
    os.system('git push origin auto_update_{version}:auto_update_{version} --tags'.format(version=sys.argv[2]))
    os.system('git checkout develop')
    if need_save:
        os.system("git stash pop")
    os.chdir("../")


def change_version(project):
    for line in fileinput.FileInput("gradle.properties", inplace=True):
        if line.strip().startswith('VERSION_NAME'):
            line = 'VERSION_NAME={version}\n'.format(version=sys.argv[2])
        if line.strip().startswith('VERSION_CODE'):
            line = 'VERSION_CODE={version}\n'.format(version=string.replace(sys.argv[2], '.', ''))
        sys.stdout.write(line)
        if __project_name__[project] - 1 >= 0:
            project_name = __project_code__[__project_name__[project] - 1] if __project_name__[project] != 2 else 'pay'
            for line2 in fileinput.FileInput('library/build.gradle', inplace=True):
                if line2.find('com.meituan.android.{project_name}:'.format(project_name=project_name)) > 0:
                    line2 = re.sub(r'(\d+).(\d+)', sys.argv[2], line2)
                sys.stdout.write(line2)


if __name__ == '__main__':
    if len(sys.argv) > 4:
        path = sys.argv[4]
    else:
        path = '/Users/zhongcheng/work'
    os.chdir(path)
    print(path)
    if sys.argv[1] == 'all':
        for i in range(0, 5):
            commit_project(path, __project_code__[i])
    else:
        project_code = __project_name__[sys.argv[1]]
        commit_project(path, __project_code__[project_code])
