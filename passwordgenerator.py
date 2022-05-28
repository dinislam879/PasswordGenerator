#Random Password Generator
import random

print('\033[1m' + "Random Password Generator")

length = int(input("Select length for your password:"))
pass_type = str(input("Password type (letters, numbers, mixed)"))
pass_amount = int(input("Password amount:"))
pass_type = pass_type.lower()
    
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 

numbers = ['1','2','3','4','5','6','7','8','9']

sym = ['$', '%', '&','(', ')', '*', '+', '-', 
'.', '/', ':', ';', '<', '=', '>', '?', '@', '\\']



def pass_make(leng):
    

    a = leng//3
    b = leng%3
    a = random.choices(letters, k=a) + random.choices(numbers, k=a) + random.choices(sym, k=a) + random.choices(numbers, k=b)

    c = random.shuffle(a)
    c =  "".join(a)  
    res = ''.join(str(e) for e in a)
    return res

count = 0
slash = 1
def numpass_make(leng):
    num = random.choices(numbers, k=leng)
    res = ''.join(str(e) for e in num)
    return res

def letterpass_make(leng):
    let = random.choices(letters, k=leng)
    res = ''.join(str(e) for e in let)
    return res

if pass_type == "mixed":
    while pass_amount > count:
        print(str(slash) + ":  " + pass_make(length))
        print("    ")
        count += 1
        slash += 1
    
elif pass_type == 'numbers':
    while pass_amount > count:
        print(str(slash) + ":  " + numpass_make(length))
        print(" ")
        count += 1

elif pass_type == "letters":
    while pass_amount > count:
        print(str(slash) + ":  " + letterpass_make(length))
        print(" ")
        count += 1