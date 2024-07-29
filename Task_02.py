
#Task no 2- designing a arithmetic calculator for performing arithmetic operations on 2 digits


print("--------CALCULATOR FOR 2 DIGIT CALCULATION--------")
print("please choose and enter the suitable option\npress 1 for addition\npress 2 for subtraction\npress 3 for multiplication \npress 4 for division")

a=int(input("your selection :"))

b=int(input("enter the first number :"))
c=int(input("enter the second number :"))

if(a==1):
    print("the sum is "+" "+str(b+c))
elif(a==2):
    print("the output is"+" "+str(b-c))
elif(a==3):
     print("the output is"+" "+str(b*c))
elif(a==4):
     print("the output is"+" "+str(b/c))
else:
    print("invalid selection ! please try again later ")