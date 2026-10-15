import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtWidgets import QWidget

def add_item():
    # آیتم اضافه کند
    pass

def delete_item():
    # آیتم انتخاب شده را حذف کند
    pass

def edit_item():
    # آیتم را با مقادیر جدید جا به جا میکند
    pass

def close_app():
    # برنامه را ببندد
    pass


app = QApplication(sys.argv) # ساخت برنامه
window = QWidget() # ساخت پنجره
window.setWindowTitle("سیستم خرید") # اسم برنامه
window.resize(500, 500) # اندازه پنجره

# ویجت ها

window.show() # نمایش پنجره
sys.exit(app.exec_()) # اجرا برنامه