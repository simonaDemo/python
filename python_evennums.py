import random
list = []
len_list = random.randint(5,20)                  #length of random list
while len(list) < len_list:
    list.append(random.randint(0,100))           # adding random number to list
print (list)
evenlist = [num for num in list if num % 2 == 0]    #choice of only even numbers (list comprehension)
print (evenlist)
