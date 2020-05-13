###global a

a=10
aa=[10]
#aaa={a:10}
###10:10
aaa={'a':10}
def exec_backend():

    global a

    a+=1
    aaa['a']+=1
    
    #a+=2
    #a+=3
    print(a)
    print(id(a))
    print(__name__)
    print(aa)
    print(aaa)
    
