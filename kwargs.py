def hello(**kwargs):
    
   # print("hello" + kwargs['first'] + " " + kwargs['Last'])
    print("Hello",end=" ")
    
    for key,value in kwargs.items():
        print(value,end=" ")
    
hello(tittle="mr.",first="Bro",middle="dude",last="code")    