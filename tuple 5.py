def tuple5():
    tuple=[(1,2),(),(3,4),()]
    print("original list=",tuple)
    for x in tuple:
        if len(x)==0:
            tuple.remove(x)
    print(tuple)

tuple5()    
