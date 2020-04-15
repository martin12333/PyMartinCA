from __future__ import print_function

from scipy.ndimage import filters
import time

from pylab import *
import matplotlib.pyplot as plt


#matplotlib.rc("image",cmap="gray")
#matplotlib.rc("image",cmap="hot")
##matplotlib.rc("image",cmap="RdYlGn")
##matplotlib.rc("image",cmap="BrBG")
#matplotlib.rc("image",cmap="copper")
#matplotlib.rc("image",cmap="afmhot")
#matplotlib.rc("image",cmap="autumn")
#matplotlib.rc("image",cmap="summer")

#matplotlib.rc("image",interpolation="nearest")


plt.ion()
#plt.ioff()


#img_plot = plt.imshow(a)
#plt.show(block=False)


####plt.matshow())
##plt.figure()
#### wrong: extent=(xlo, xhi, ylo, yhi) ) 
##, interpolation="nearest")
##, cmap = plt.cm.gray)



OR = logical_or
AND = logical_and


plotysum=zeros( (niter,1) )

for j in xrange(ns):

    p=0.5#0.3#0.5 #0.25 #0.16
    a = zeros( ( h, w ), dtype=bool) 
    
    a[ h0 : h0+h2 , w0 : w0+w2 ] = (rand( h2, w2 )<p) 

    
    afade = 0.1 * a
    averyold = a 


    #plotx=zeros( (niter,1) )
    ploty=zeros( (niter,1) )

    for i in xrange(niter):

        n41 =   diam*diam*filters.uniform_filter(0.0+a,diam )   ##,mode='wrap')  )  
        n=n41.round()   
        birth = AND(  n>=bmin,  AND( n<=bmax, logical_not(a) )  )
        survi = AND(  n>=smin,  AND( n<=smax, a )  )
        a =  OR( birth , survi )  

        as51=(0.0+a).sum()
        ploty[i]=as51

        if (i % step1)==0:

            if bfade:
                afade = q*a + (1-q)*afade
                asho=afade
            else:
                asho=0+a
                
            ada51= logical_xor(a, averyold)  
            averyold =a 
            
            ##adaimage = transpose( ( ( asho)))
            ##b = array(255*clip(adaimage,0,1),'B')

            ###imshow(asho)
            #show()


            #img_plot.set_data(asho)
            #plt.draw()


            ##time.sleep(sleep1)
            

            if (i % step2)==0:
                am51=(0.0+a).mean()
                sam51='{:.5f}'.format(am51)
                dam51=ada51.mean()
                sdam51='{:.5f}'.format(dam51)
                print( i, sam51, sdam51)


    plot(ploty,'x')
    plotysum += ploty
    
    
    
    
