print("x         y\n-------------")
def x(start, stop, step):

    while start <=stop:
        y=start**2
        print(f"{start}    {y}")
        start +=step
       
x(-10, 10, 0.5)