from __future__ import print_function

from scipy.ndimage import filters
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation


#matplotlib.rc("image",cmap="gray")
matplotlib.rc("image",cmap="hot")
##matplotlib.rc("image",cmap="RdYlGn")
##matplotlib.rc("image",cmap="BrBG")
#matplotlib.rc("image",cmap="copper")
#matplotlib.rc("image",cmap="afmhot")
#matplotlib.rc("image",cmap="autumn")
#matplotlib.rc("image",cmap="summer")

#matplotlib.rc("image",interpolation="nearest")

fig = plt.figure()

#plt.ion()
##plt.ioff()


im1 = plt.imshow(a, animated=True)

####plt.matshow())
#### wrong: extent=(xlo, xhi, ylo, yhi) ) 
##, interpolation="nearest")
##, cmap = plt.cm.gray)
#plt.show(block=False)


OR = logical_or
AND = logical_and


def updatefig(*args):

    global a,afade
    
    for jj in range(step1):
        n41 =   diam*diam*filters.uniform_filter(0.0+a,diam )   ##,mode='wrap')  )  
        n=n41.round()   
        birth = AND(  n>=bmin,  AND( n<=bmax, logical_not(a) )  )
        survi = AND(  n>=smin,  AND( n<=smax, a )  )
        a =  OR( birth , survi )  
    
    if bfade:
        afade = q*a + (1-q)*afade
        asho=afade
    else:
        asho=0+a
    
    print(step1)
    
    im1.set_array(asho)
    return im1,

ani = animation.FuncAnimation(fig, updatefig, blit=True) #interval=50, 
plt.show()


