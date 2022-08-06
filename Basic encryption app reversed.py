

def crypted(sentence): 
    encryption = ""
    for element in sentence:
        if element in "1":
            encryption = encryption + "a"
        elif element in "2":
            encryption = encryption + "b"
        elif element in "3":
            encryption = encryption + "c"
        elif element in "4":
            encryption = encryption + "d"
        elif element in "5":
            encryption = encryption + "e"
        elif element in "6":
            encryption = encryption + "f"
        elif element in "7":
            encryption = encryption + "g"
        elif element in "8":
            encryption = encryption + "h"
        elif element in "9":
            encryption = encryption + "i"
        elif element in "0":
            encryption = encryption + "j"
        elif element in "/":
            encryption = encryption + "k"
        elif element in "?":
            encryption = encryption + "l"
        elif element in "#":
            encryption = encryption + "m"
        elif element in "@":
            encryption = encryption + "n"
        elif element in "$":
            encryption = encryption + "o"
        elif element in "%":
            encryption = encryption + "p"
        elif element in "!":
            encryption = encryption + "q"
        elif element in ";":
            encryption = encryption + "r"
        elif element in "^":
            encryption = encryption + "s"
        elif element in "&":
            encryption = encryption + "t"
        elif element in "*":
            encryption = encryption + "u"
        elif element in "(":
            encryption = encryption + "v"
        elif element in ")":
            encryption = encryption + "w"
        elif element in "_":
            encryption = encryption + "x"
        elif element in "-":
            encryption = encryption + "y"
        elif element in ":":
            encryption = encryption + "z"
       
        else:
            encryption = encryption + element
            
    return encryption


print(crypted(input("What do you want to encrypt: ")))


"&85 !*93/ 2;$)@ 6$_ 0*#%^ $(5; &85 ?1:- 4$7."

