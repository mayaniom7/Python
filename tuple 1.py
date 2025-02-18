def numberofgirlsandboys():
    boy=('b1','b2','b3','b4','b5','b6')
    girl=[boy,'g1','g2','g3']
    countboys=0
    countgirls=0
    for i in girl:
         if isinstance(i,tuple):
            for j in i:
              countboys=countboys+1
         else:    
             countgirls=countgirls+1
    print(countboys)
    print(countgirls)

numberofgirlsandboys()
