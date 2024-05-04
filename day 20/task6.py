a = int(input ("enter first number: "))
b = int(input ("enter second number: "))
my_list = []
listt = []
if a > b:
    for i in range ( b, a):
        listt.append(i)
        print(listt)
elif b > a:
    for t in range( a, b):
        my_list.append(t)
        print(my_list)

