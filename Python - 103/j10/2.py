import random

a = ["danesh" , "soltani" , "javazi"]
print(random.random())
print(random.randint(1 , 10))
print(random.randrange(1, 10 , 2))
print(random.choice(a))
print(random.choices(a , k=4))
print(random.uniform(1 , 5))
print(random.sample(a , 2))
random.shuffle(a)
print(a)