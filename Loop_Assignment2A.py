'''Write a program to print multiplication table of a given number'''

num=int(input("the number which you want to multiples"))
print("the multiplication of ",num, "number is:")
for i in range(1,11):

    print(num,'x',i,'=',num*i)