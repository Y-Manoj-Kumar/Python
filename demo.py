# #For doing math calculation we need to add "import math"
# print(max(12,33,432,4323,645333))

# # All about indexing [start:stop:step]
# #step = for reversing the string we have to use negative values

# Company = "Tata Consultancy Service"
# first_name = Company[0::2]
# print(first_name)
# #Slicing43
# slice = slice(5,-8)
# print(Company[slice]) #here the slice should be in a "Square Brakcet"

#Conditional Statement
# marks = int(input("How many marks you get in physics: "))

# if(marks >= 35):
#     print("Very Lucky guy You got a pass marks with border marks")
# elif(marks < 35):
#     print("Better luck next time you got failed in this exam")
# else:
#     print("Please rewrite the exam")

# role = input("what's your position in this company ? ")
# from multiprocessing import Manager

 
# role = input("Enter your position in yor company?" )

# if role == "Manager".lower():
#     print("Hooo that's great ")
# elif role == "Developer".lower():
#     print("Need to develop your skills more as per future technology")
# else:
#     print("go get a job ")


def demo(num):
    if num<1:
        return 0
    elif num%2 == 0:
        return demo(num-1)
    else:
        return num+demo(num-2)

print(demo(8))




 
