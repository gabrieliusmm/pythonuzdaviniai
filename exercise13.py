#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
#Take this opportunity to think about how you can use functions.
#Make sure to ask the user to enter the number of numbers in the sequence to generate.
#(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
#The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

user_input = int(input("How many Fibonnaci numbers do you want to generate?: "))
def Fibonnaci_Generator(number):
    list = []
    i = 1
    if number >= 1:
        list.append(1)
    for x in range(1,number):
        list.append(i)
        i = i + list[x-1]


    
    return list
        
print(Fibonnaci_Generator(user_input))