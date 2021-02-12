user_input = input("Write a text: ")

def backwards_text(text):
    splitted = text.split()
    backwards = splitted[::-1]
    result = " ".join(backwards)
        
    return result

print(backwards_text(user_input))
print(user_input)