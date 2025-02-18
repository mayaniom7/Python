def sepraterollnonameageofstudent():
    list=[('csk01','dhoni','41'),('csk02','gaikwad','27'),('csk03','jadeja','35')]
    age=[]
    name=[]
    rollno=[]
    for i in list:
            if isinstance(i,tuple):
                for j in i:
                    if isinstance(j,int):
                        age.append(j)
                    else:
                        if j.isalpha():
                            name.append(j)
                        else:   
                            rollno.append(j)
            else:
             break
    print(age)
    print(name)
    print(rollno)
sepraterollnonameageofstudent()     
                            
                        
