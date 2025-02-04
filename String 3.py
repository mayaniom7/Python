def RemoveStrings():
    s1=input("Enter a String:")
    s2=input("Enter another String:")
    if s2 in s1:
        sp=s1.find(s2)
        s1=s1[:sp]+s1[sp+len(s2):]
    print(s1)
    
RemoveStrings()
    
