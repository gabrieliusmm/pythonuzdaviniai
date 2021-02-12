#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
#And makes a new list of only the first and last elements of the given list.
#For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]
print("Old list:", a)
def newlist(list):
    new = []
    i = 0
    for x in list:
        i += 1
    new.append(list[0])
    new.append(list[i-1])
    print("New list:", new)

newlist(a)