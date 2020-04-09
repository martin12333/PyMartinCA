
from scipy.ndimage import filters
import time
import pygame
from pygame import surfarray

pygame.init()
#plt.ioff()

screen = pygame.display.set_mode((w,h))
surface = pygame.Surface((w,h),depth=8)

OR = logical_or
AND = logical_and

for i in range(niter):
    n41 =   diam*diam*filters.uniform_filter(0.0+a,diam )   ##,mode='wrap')  )  ###around
    ##n41 = floor(0.5+diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
    #n42 = floor(0.5+diam*diam*filters.uniform_filter(n41,diam,mode='wrap')  )
    n=n41.round()   #n42
    birth = AND(  n>=bmin,  AND( n<=bmax, logical_not(a) )  )
    survi = AND(  n>=smin,  AND( n<=smax, a )  )
    a =  OR( birth , survi )  ###1.0*
    ##n753 = (diam*diam*filters.uniform_filter(n752,diam,mode='wrap')  )
    ##n754 = (diam*diam*filters.uniform_filter(n753,diam,mode='wrap')  )
    #imshow(a)  
    ##matshow()
    ##drawnow()
    ###matplotlib.pyplot.show()
    if (i % step1)==0:
        if bfade:
            #asho = (2 * a + averyold )/3
            ####asho = np.maximum( a , averyold /3 )
            ####asho = np.maximum( a , averyold /3. )
            #asho = np.maximum( a , afade/3. )
            ###asho = np.maximum( a , qqq*afade )
            #asho = afade 
            afade = q*a + (1-q)*afade
            asho=afade
        else:
            asho=0+a
            
        ada51= logical_xor(a, averyold)  ## da51=   0 +a - averyold
        averyold =a ##0+a
        
        adaimage = transpose( ( ( asho)))
        #####print shape(image)
        #b = array(255*clip(image,0,1),'B')
        b = array(255*clip(adaimage,0,1),'B')
        # #b = array(clip(transpose(xx),0,255),'B')
        # #b = array(clip((yy),0,255),'B')
        pygame.surfarray.blit_array(surface,b[:w,:h])
        screen.blit(surface,(0,0))
        pygame.display.flip()
        time.sleep(sleep1)
#        #print i, norm70
        am51=(0.0+a).mean()
        sam51='{:.3f}'.format(am51)
        ####ada51=abs(da51) # calls .__abs__
        ##ada51=np.abs(da51)
        dam51=ada51.mean()
        sdam51='{:.3f}'.format(dam51)
        if (i % step2)==0:
            print( i, sam51, sdam51)


##debug #print shape(bmin)
##debug numpy.size(yy,0)
##debug type(bmax)

