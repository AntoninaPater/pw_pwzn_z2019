def task_2():
    
    a = "\n"
    
    for i in range(0,5):

        a = a + "* " * i +"*" + "\n"
        
    b = ""
    for ii in range(4,0, -1):
        b = b +  "* " * (ii -1) +"*" + "\n"
        
    c = a+b
        
    return c


assert task_2() == '''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''