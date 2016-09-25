from uiautomator import device as d
import re

User = ['basketcase0612', 'liveforever06']
TIMEOUT = 100000

isCheck = False


def checkLogin():
    global isCheck
    goToMy()
    isCheck = not d(text="用户名/Email/手机号码").exists
    return isCheck


def logout():
    print('------开始退出------')
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
    print('------已退出------')



def getLevelAndTime():
    d(text="游戏").wait.exists
    d(text="游戏").click.wait()
    print('------进入游戏------')
    d(className="android.widget.RelativeLayout")[2].wait.exists(timeout=TIMEOUT)
    d(className="android.widget.RelativeLayout")[2].click.wait()
    print('------进入lol------')
    d(className="android.widget.Image", instance=1).wait.exists(timeout=TIMEOUT)
    d(className="android.widget.Image", instance=1).click.wait()
    print('------进入我的战绩------')
    d(index=0, className='android.webkit.WebView').wait.exists(timeout=TIMEOUT)
    d(index=0, className='android.webkit.WebView').child()[0].wait.exists(timeout=TIMEOUT)
    d(index=0, className='android.webkit.WebView').child()[0].child()[0].wait.exists(timeout=TIMEOUT)
    d(index=0, className='android.webkit.WebView').child()[0].child()[0].child()[0].wait.exists(timeout=TIMEOUT)

    levelAndTime = [
        d(index=0, className='android.webkit.WebView').child()[0].child()[0].child()[0].info['contentDescription'],
        "no recent login"]
    print('------获取到等级------')
    if not d(className='android.widget.ListView').exists:
        levelAndTime[1] = "recent login"
    return levelAndTime


def getMoney():
    goToMy()
    print('------获取到游戏币------')
    money = d(className="android.widget.TextView", instance=3).info['text']
    return money


def getInformation(User):
    print('------开始获取信息------')

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
        print('------开始更换区域------')
        d(text="我").click.wait()
        d(text="设置").click.wait()
        d(text="语言和区域").click.wait()
        d.drag(400, 400, 400, 0, steps=5)
        d(text="地区").click.wait()
        d(text="确定").click.wait()
        d(text="台湾/香港/澳门").click.wait()
        print('------更换区域成功------')


def login(User):
    print('------开始登录------')
    print(User)
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

    d(text="登录").click.wait()

    isCheck = checkLogin()

    if isCheck:
        print("------登录成功------")
        changeDis()
        getInformation(User)
    else:
        print("------登录失败------")
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
