def calcu_1(a , b):
    return a + b
def calcu_2(a , b):
    return a * b

answer = calcu_2(calcu_1(10 , 20), 8)
print(answer)