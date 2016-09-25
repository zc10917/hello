from uiautomator import device as d
import re

User = ['basketcase0612', 'liveforever06']
TIMEOUT = 100000

isCheck = False


def checkLogin():
    global isCheck
    goToMy()
    isCheck = d(text="Facebook").exists
    print(isCheck)
    return isCheck


def logout():
    d.press('back')
    d.press('back')
    if not d(text="我").exists:
        d.press('back')
    goToMy()
    money = getMoney()
    User.append(money)
    d(text="设置").click.wait()
    d(text="退出").click.wait()
    d(text="是的").click.wait()


def getLevelAndTime():
    d(text="游戏").wait.exists
    d(text="游戏").click.wait()
    d(className="android.widget.RelativeLayout")[2].wait.exists(timeout=TIMEOUT)
    d(className="android.widget.RelativeLayout")[2].click.wait()
    d(className="android.widget.Image", instance=1).wait.exists(timeout=TIMEOUT)
    d(className="android.widget.Image", instance=1).click.wait()
    d(index=0, className='android.webkit.WebView').wait.exists(timeout=TIMEOUT)
    d(index=0, className='android.webkit.WebView').child()[0].wait.exists(timeout=TIMEOUT)
    d(index=0, className='android.webkit.WebView').child()[0].child()[0].wait.exists(timeout=TIMEOUT)
    d(index=0, className='android.webkit.WebView').child()[0].child()[0].child()[0].wait.exists(timeout=TIMEOUT)

    levelAndTime = [
        d(index=0, className='android.webkit.WebView').child()[0].child()[0].child()[0].info['contentDescription'],
        "no recent login"]
    if not d(className='android.widget.ListView').exists:
        levelAndTime[1] = "recent login"
    return levelAndTime


def getMoney():
    goToMy()
    money = d(className="android.widget.TextView", instance=3).info['text']
    return money


def getInformation(User):

    levelAndTime = getLevelAndTime()

    User.append(levelAndTime[0])
    User.append(levelAndTime[1])


def goToMy():
    d(text="我").wait.exists(timeout=200)
    if d(text="我").exists:
        d(text="我").click.wait()


def changeDis():
    d(text="游戏").click.wait()
    if d(text="即将推出").exists:
        d(text="我").click.wait()
        d(text="设置").click.wait()
        d(text="语言和区域").click.wait()
        d.drag(400, 400, 400, 0, steps=5)
        d(text="地区").click.wait()
        d(text="确定").click.wait()
        d(text="台湾/香港/澳门").click.wait()


def login(User):
    global isCheck
    isCheck = False
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

    d(text="登录").click.wait(timeout=1000)

    isCheck = checkLogin()

    if isCheck:
        changeDis()
        getInformation(User)
    else:
        return


def start(User):
    global isCheck
    login(User)
    if isCheck:
        logout()
        return User
    else: return None


if __name__ == '__main__':
    # goToMy()
    # login(User=User)
    # d(className="android.widget.Image", instance=1).click.wait()
    # for view in (d(index = 0 ,className='android.webkit.WebView').child()[0].child()[0]):
    #     print(view.info)
    # login(User)
    # logout()
    changeDis()
    getMoney()





    # print(len( d(className = 'android.widget.ListView')))
