

def check_string(a):
    
    First_word = a.strip().split()[0]

    if First_word.startswith("The"):
        return "Yes!"
    else:
        return "No!"


str1 = "The"
str2 = "Thumbs up"
str3 = "Theatre can be boring"




print(check_string(str1))
print(check_string(str2))
print(check_string(str3))

