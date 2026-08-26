user_name = input("The user name: ") #کاربر اسمش رو وارد میکنه
kala_name = input("The kala name: ") #کاربر نام کالا رو وارد میکنه
kala_price = int(input("The kala price: ")) #کاربر قیمت کالا را وارد میکنه

takhfif_value = kala_price * 0.05 #یه متغیر میسازیم که 5 درصد اون قیمت کالا باشه به عنوان مقدار تخفیف
maliat_value = kala_price * 0.10 #دوباره یه متغیر دیگه میسازیم که 10 درصد اون قیمت کالا باشه به عنوان مقدار مالیات

answer = kala_price - takhfif_value + maliat_value #تخفیف رو از قیمت کل کم میکنیم و مالیات را به آن اضافه میکنیم تا قیمت نهایی مشخص بشه 

# خروجی
print("Welome {}".format(user_name)) 
print("The price osssbbhf {} is {}".format(kala_name , answer))sdsdgsdg