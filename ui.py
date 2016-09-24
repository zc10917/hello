import time
from uiautomator import device as d

User = ['basketcase0612', 'liveforever06']


def checkLogin():
    return d(text="Facebook").exists


def getInformation():
    d(text="游戏").click.wait()
    d(id="android:id/tabs").child()[2].click.wait()
    d(text="我的战绩").click.wait()
    d(classmethod="android.webkit.WebView").child()[0].child()[0].child()[0].child()[2].click.wait()




def doNext():
    pass


def goToMy():
    if d(text="我").exists:
        d(text="我").click()


def login(User):
    d.screen.on()
    goToMy()

    userUI = d(text="用户名/Email/手机号码").child(className='android.widget.EditText')
    passwordUI = d(text="密码").child(className='android.widget.EditText')

    userUI.click()
    userUI.set_text(None)
    userUI.set_text(User[0])

    passwordUI.click()
    for i in range(1, 15):
        d.press("delete")
    passwordUI.set_text(User[1])

    d(text="登录").click.wait()
    oldtime = time.time()
    print(oldtime)
    ischecked = checkLogin()

    if ischecked:
        print("ischecked")
        # getInformation()
    else:
        print("nochecked")
        # doNext()


if __name__ == '__main__':
    # login(User=User)
    # d(className="android.widget.RelativeLayout")[2].click.wait()
    d(className="android.webkit.WebView").child()[0].child()[0].click.wait()

