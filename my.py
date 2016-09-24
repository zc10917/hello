import os
from multiprocessing.dummy import Pool
import sys

git_clone = "git clone "
git_checkout = "git checkout "
git_pull = "git pull "
develop = "develop"
master = "master"

usrName = "zhongcheng02"
path = "/Users/zhongcheng/test/"

pool = Pool(4)

projects = ["cashier", "meituanpay", "pay-common", "wallet", "barcodecashier", "pay-demo"]

urls = []
for packageName in projects:
    if packageName == "pay-demo":
        urls.append("http://" + usrName + "@git.sankuai.com/scm/android/" + packageName + ".git")
    else:
        urls.append("http://" + usrName + "@git.sankuai.com/scm/as/" + packageName + ".git")


def clonePackage(url):
    os.chdir(path)
    dir = url.split("/")[-1].split(".")[0]
    if os.path.exists(path + dir):
        return

    os.system(git_clone + url)


def checkoutBranch(project, p=path, branch=develop):
    os.chdir(p + project)
    if project == "pay-demo":
        os.system(git_checkout + master)
        return
    else:
        os.system(git_checkout + branch)


def pullProjects(project):
    os.chdir(path + project)

    os.system(git_pull)




print("finish")
if __name__ == "__main__":
    if len(sys.argv)>=2:
        path = sys.argv[1]
    if len(sys.argv)>=3:
        usrName = sys.argv[2]

    pool.map(clonePackage, urls)
    pool.map(checkoutBranch, projects)
    pool.map(pullProjects, projects)
