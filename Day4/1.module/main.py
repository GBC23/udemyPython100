import random
import myModule # myModule.py 를 import # 무조건 같은 폴더 안에 있어야 import가 가능하다.

random_integer = random.randint(1,10)
print(random_integer)

print(myModule.pi)

randomFloat = random.random()
print(round(randomFloat,2))

print(randomFloat*10/2)

loveScore = random.randint(1, 100)
print(f'Your love score is {loveScore}')

