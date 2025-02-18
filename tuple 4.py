def tuple4():
    foods=[('classic pizza',49),('margheritta pizza',109),('farmhouse pizza',249)]
    for x in foods:
        print(x)
        print(sorted(foods))
        import operator
    print(sorted(foods,key=operator.itemgetter(1),reverse=True))

tuple4()        
