try: #قطعه کد
    a = int(input())
except ValueError as error: #ذخیره در متغیر
    print("Error value:" , error)
except TypeError: #با نوع ارور
    print("Error type")
except: #همه نوع ارور
    print("Error")
else: #اگر ارور نداد
    print("Whitout Error")
finally: #در هر صورت اجرا میشه 
    print("App finished")