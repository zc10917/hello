from uiautomator import Device


d = Device('192.168.56.101:5555')

d.screen.on()
d.press.home()

d(text="pay-demo").click()
d(className = "android.widget.EditText").set_text("33")
d.dump('dd.xml')
d.screenshot("homegggggggggggggggggggg.png")




