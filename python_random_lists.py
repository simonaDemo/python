import random
def random_generator():
    res = []
    for j in range(random.randint(1,11)):
        res.append(random.randint(0, 100))
    return res

a = random_generator()
b = random_generator()
print(a)
print(b)
new_list = []
if len(a) <= len (b):
    for i in a:
        if i in b:
            new_list.append(i)
    print (new_list)
else:
    for i in b:
      if i in a:
            new_list.append(i)
    print (new_list)

