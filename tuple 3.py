import datetime
def tuple3():
    d1=(1,9,2007)
    d2=(4,6,2004)
    date1=datetime.date(d1[2],d1[1],d1[0])
    date2=datetime.date(d2[2],d2[1],d2[0])
    print(type(date1))
    print(abs(date1-date2))

tuple3()    
