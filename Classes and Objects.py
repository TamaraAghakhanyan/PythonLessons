# Class

class MyRouter(object):
    "This is a class that describes the characteristics of the router"
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial number of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)


'''router1 = MyRouter("R1", "2600", "123456", "12.4")
router1
<__main__.MyRouter object at 0x104d77a90>
router1.model
'2600'
router1.serialno
'123456'
router1.ios
'12.4'
router1.print_router("27.06.2023")
The router name is:  R1
The router model is:  2600
The serial number of:  123456
The IOS version is:  12.4
The model and date combined:  260027.06.2023
router1.print_router(" 27.06.2023")
The router name is:  R1
The router model is:  2600
The serial number of:  123456
The IOS version is:  12.4
The model and date combined:  2600 27.06.2023
router2 = MyRouter("R2", "2700", "1234", "13")
router2
<__main__.MyRouter object at 0x104d87340>
router2.ios
'13'
router2.model
'2700'
router2.serialno
'1234'
router2.routername
'R2'
router2.print_router(" 28.07.2023")
The router name is:  R2
The router model is:  2700
The serial number of:  1234
The IOS version is:  13
The model and date combined:  2700 28.07.2023
router2.ios
'13'
router2.ios = "13.1"
router2.ios
'13.1'
getattr(router2, "ios")
'13.1'
setattr(router2, "ios", "13.2")
getattr(router2, "ios")
'13.2'
hasattr(router2, "ios")
True
hasattr(router2, "Android")
False
delattr(router2, "ios")
getattr(router2, "ios")
Traceback (most recent call last):
  File "/Applications/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
AttributeError: 'MyRouter' object has no attribute 'ios'
hasattr(router2, "ios")
False
isinstance(router2, MyRouter)
True'''


# Inheritance
