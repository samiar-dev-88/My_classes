import random

lis = [1 , 2 , 3 , 4 , 5]
print(random.random()) # 0 - 1 اعشاری
print(random.randint(1 , 6)) # بازه ای عددی
print(random.uniform(1 , 5)) # بازه ای اعشاری
print(random.randrange(1 , 10)) # range بازه ای با
print(random.choice([1 , 2 , 3 , 4 , 5])) # عضو رندوم
print(random.choices(["ali" , "reza" , "fatameh"] , k=3)) # عضو های رندوم با تکرار
print(random.sample(["ali" , "reza" , "fatameh"] , 3)) # عضو های رندوم بدون تکرار
random.shuffle(lis) # بر میزنه
print(lis)