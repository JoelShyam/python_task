print("two more questions baby\n")
q1=input("does it belong inside , outside or both?  ")
q2=input("is it alive?  ")
if (q1=="inside")and(q2=="alive"):
    print("houseplant")
if q1=='inside'and q2=='not alive':
    print("showcurtain")
if q1=='outside'and q2=='alive':
    print("bison")
if q1=='outside'and q2=='not alive':
    print("billboard")
if q1=='both'and q2=='alive':
    print("dog")
if q1=='both'and q2=='not alive':
    print("cellphone")    
if (q1!='inside'or q1!='outside'or q1!='both'or q2!='alive'or q2!='not alive'):
     print("sorry could'nt guess what you are thinking of")