## this is the program to run my special 
## translator 
print()
print("This is a special translator!")

## take in input
# def thankunext(s):
#     return "blagh!!"

def thankunext(strung):

    tun_dict = {'a':'e', 'b':'c', 'c':'d', 'd':'f', 
    'e':'i', 'f':'g', 'g':'h', 'h':'j', 'j':'k', 'k':'l', 'l':'m','m':'n', 'n':'p',
    'o':'u', 'p':'q', 'q':'r', 'r':'s', 's':'t', 'i':'o',
    'u':'y', 't':'v', 'v':'w', 'w':'x', 'x':'z', 'y':'a'}

    strung = strung.lower()
    strang = ""
    for i in range(len(strung)):
        curr = strung[i]
        if curr not in tun_dict:
            strang += curr
        else:
            strang += tun_dict[curr]
    return strang

while(True):
    answer = input("Do you have a phrase to be translated into thankunext? [Y/N] :  ")
    answer = answer.upper()
    print()
    if( ((answer == 'Y' ) or (answer == 'YES') or (answer == 'Y '))):
        raw = input("Enter in a phrase to be translated:  ")
        print(raw, "-->", thankunext(raw))
        print()

    else:
        print("Okay, that is fine, as we say here -- 'HOOF CAO!'")
        print()
        print()
        break
   
        
   


## parse input

## return output 
## check if any more input 

## else, say good bye in thankyou next

## Hoof cao



