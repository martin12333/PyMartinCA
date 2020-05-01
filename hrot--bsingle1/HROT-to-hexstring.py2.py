import numpy as np
#from  numpy import zeros

# M0 ... HROT
r=3#2
d=2*r+1



#atable1=np.zeros( (d*d,1) , dtype=int)
atable1=np.zeros( d*d , dtype=int)


atable1[9:19]=1


#print(list(atable1.ravel()))
#print(atable1.ravel())
#('[0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0]')
print(atable1)

x=0
for i in range(d*d):
    if atable1[i] != 0:
        x=x|(1<<i)
        
#523776
#(x)

uintx2=x
uintx=x>>1

#hexstring1=format(uintx, '06x')
hexstring1=format(uintx, '0'+    str(r*(r+1))        +'x')

#('03ff00')
print(hexstring1)




