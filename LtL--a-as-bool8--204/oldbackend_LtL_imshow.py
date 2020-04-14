from scipy.ndimage import filters
import time
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

####plt.matshow())
#plt.figure()
img_plot = plt.imshow(a)
#### wrong: extent=(xlo, xhi, ylo, yhi) ) 
#, interpolation="nearest")
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
        if bfade:
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
        else:
            asho=a
        img_plot.set_data(asho)
        ###imshow(asho)
        ##show()
        plt.draw()
        time.sleep(sli)
        print i


##debug print shape(blo)
##debug numpy.size(yy,0)
##debug typename(blo)
