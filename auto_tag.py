import os
import sys

# python tag {version}  【传"d"为删除分支】  【传入project名字,默认为所有】 【传入是否需要上传,true为上传,默认不上传】
path = "/Users/zhongcheng/work/"
projects = ["cashier", "pay-common", "barcodecashier", "meituanpay", "wallet"]
git_tag = "git tag "
git_tag_d = "git tag -d "
git_tag_push_origin_tag = "git push origin --tags "
git_tag_push_origin_delete_tag = "git push origin --delete tag "
git_pull = "git pull"


def getVersion(tag):
    version = 'aar_v'
    for i in tag:
        if i != '.':
            version = version + i + '.'
        else:
            break
    version = version[0:len(version) - 1]
    version = version + '_' + tag

    return version


def tagProject(tag):
    if checkUpdate():
        for project in projects:
            os.chdir(path + project)
            os.system(git_tag + tag)


def delProjectTag(tag):
    for project in projects:
        os.chdir(path + project)
        os.system(git_tag_d + tag)


def checkUpdate():
    for project in projects:
        os.chdir(path + project)
        if not os.popen(git_pull).read().strip().startswith("Already up-to-date."):
            print("" + project + "似乎有更新。。。。。")
            return False

    print("无更新")
    return True


def upLoadTag(tag):
    for project in projects:
        os.chdir(path + project)
        os.system(git_tag_push_origin_tag + tag)


def delUpstreamTag(tag):
    for project in projects:
        os.chdir(path + project)
        os.system(git_tag_push_origin_delete_tag + tag)


def main():
    global projects
    if len(sys.argv) >= 2:
        tag = sys.argv[1]

    else:
        return
    mode = "添加"
    upLoad = False

    if len(sys.argv) >= 3:
        if sys.argv[2] == "d":
            mode = sys.argv[2]
        elif sys.argv[2] == "true":
            upLoad = True
        elif sys.argv[2] in projects:
            projects = [sys.argv[2]]
    if len(sys.argv) >= 4:
        if sys.argv[3] == "true":
            upLoad = True
        elif sys.argv[3] in projects:
            projects = [sys.argv[3]]
    if len(sys.argv) >= 5 and sys.argv[4] in projects:
        projects = [sys.argv[4]]

    print("path = " + path)
    print("tag = " + tag)
    print("mode = " + mode)
    print("修改的工程为: ")
    print(projects)
    print("是否上传: ")
    print(upLoad)
    print(" ")

    ok = input("输入y确认")
    if ok == "y":

        ver = getVersion(tag)

        if mode == "d":
            delProjectTag(ver)
        else:
            tagProject(ver)
        if upLoad:
            upLoadTag(ver)
            # delProjectTag(ver)


if __name__ == "__main__":
    main()

