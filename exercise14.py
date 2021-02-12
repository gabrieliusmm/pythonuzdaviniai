#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

names = ["Michele", "Robin", "Sara", "Michele"]


def loop_list(names):
    
    new_list = []
    #k = 0
    for y in names:
        new_list.append(y)
    for x in range(len(new_list)):
        
        for i in range(x+1, len(new_list)):
            if new_list[x] == new_list[i]:
                del new_list[i]
                #print(new_list[x])
                #print("hello")
                #new_list.pop()
    


    return new_list

def set_list(names):
    new_list = []
    for x in names:
        new_list.append(x)
    new_list = set(new_list)
    new_list = list(new_list)
    return new_list

first_list = loop_list(names)
second_list = set_list(names)


print(first_list)
print(set_list(names))
print(names)