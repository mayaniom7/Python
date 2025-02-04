def upper(str):
    newstr=" "
    for ch in str:
        if 'a' <= ch <= 'z':
           newstr+=chr(ord(ch)-32)
        else:
            newstr+= chr
    print(newstr)
s=input("enter the string:")
upper(s)
        
