# beta ver

#NOTE: the showing of images does NOT currently work when running r2paramLtL.py from SPYDER v2.2


# evolved from
#http://nbviewer.ipython.org/github/martin12333/teaching-simso/blob/master/52-largerthanlife.ipynb
#https://github.com/thearn/game-of-life/blob/master/conway.py

from pylab import *
from scipy.ndimage import filters
import time
import matplotlib.pyplot as plt


diam =5 
#xlo= 7
#xhi=11
#ylo=  10
#yhi= 11
xlo= 10
xhi=11
ylo=  10
yhi= 10


#diam =3   
#xlo= 2 
#xhi= 4 
#ylo=3 
#yhi=5  

#h=180
#h=730 
h=360
#w=h*2
w=h

p=0.5
a = 1.0*(rand( h, w )<p)    



x11 = floor(linspace(xlo, xhi + 0.999, w))
y11 = floor(linspace(yhi + 0.999 , ylo, h))
xx, yy = meshgrid(x11, y11)

 
#blo = xx / 10.0    
blo=7 #3 

#bhi=mod(xx,10)
bhi=xx

#slo= yy / 10.0   #blo
slo = 7  #3

#shi=mod(yy, 10)
shi=yy


niter = 300    
sli=0.1
skipy=4 #2

q = 0.1
qqq=8
#q = 1. / 2.
afade = 0.1 * a
#averyold = 0*a


plt.ion()
#plt.ioff()

matplotlib.rc("image",cmap="gray")
#matplotlib.rc("image",cmap="hot")
##matplotlib.rc("image",cmap="RdYlGn")
##matplotlib.rc("image",cmap="BrBG")
#matplotlib.rc("image",cmap="copper")
#matplotlib.rc("image",cmap="afmhot")
#matplotlib.rc("image",cmap="autumn")
#matplotlib.rc("image",cmap="summer")
matplotlib.rc("image",interpolation="nearest")
##np.dstack()
##np.concatenate()
###(tup, axis=2)
####plt.matshow())
#plt.figure()
img_plot = plt.imshow(a, interpolation="nearest")
#, cmap = plt.cm.gray)
plt.show(block=False)

OR = logical_or
AND = logical_and

for i in range(niter):
    n = floor(0.5+diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
    birth = AND(  n>=blo,  AND( n<=bhi, logical_not(a) )  )
    survi = AND(  n>=slo,  AND( n<=shi, a )  )
    a = 1.0* OR( birth , survi )  
    #imshow(a)  
    ##matshow()
    ##drawnow()
    ###matplotlib.pyplot.show()
    if (i % skipy)==0:
        #asho = (2 * a + averyold )/3
        #imagesc(abs(y-yveryold)')
        #%imagesc((y-yveryold)')
        #asho = np.maximum( a , averyold /3 )
        #asho = np.maximum( a , averyold /3. )
        #asho = np.maximum( a , afade/3. )
        asho = np.maximum( a , qqq*afade )
        #asho = afade 
        afade = q*a + (1-q)*afade
        #averyold = a
        img_plot.set_data(asho)
        ###imshow(asho)
        ##show()
        plt.draw()
        time.sleep(sli)
        print i


##debug print shape(blo)
##debug numpy.size(yy,0)
##debug typename(blo)
