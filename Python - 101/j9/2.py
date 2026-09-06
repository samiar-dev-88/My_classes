import random

print(random.random())
print(random.randint(0,10))
print(random.randrange(0,11,2))
print(random.choice("Hello"))
print(random.choices("Python",k=10))
print(random.uniform(1,10))
print(random.sample("Python",3))
a = "Python"
random.shuffle(a)
print(a)