
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
    if False: #bltl :
        n = floor(0.5+diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
        birth = AND(  n>=blo,  AND( n<=bhi, logical_not(a) )  )
        survi = AND(  n>=slo,  AND( n<=shi, a )  )
        a = 1.0* OR( birth , survi )  
    elif False: #r62
        #nbig=floor(0.5  + 2*diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
        nbig=( 2*diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
        #nsmall = floor(0.5 + alpha03* d03*d03* ( filters.uniform_filter(a,d03,mode='wrap')  ))
        nsmall = ( alpha03* d03*d03* ( filters.uniform_filter(a,d03,mode='wrap')  ))
        n=nbig - nsmall
        ##n = floor(0.5 +  diam*diam* ( - a /9.0 +  2*filters.uniform_filter(a,diam,mode='wrap')  ))
        #n = floor(0.5 - a + 2*diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
        a = 1.0* AND( n>=xx , n<=yy )  
    elif False: #r69 l1x
        n69=diam*diam*filters.uniform_filter(a,diam,mode='wrap')
        n=n69
        a70=(a>=0.5)
        birth = AND(  n>=blo,  AND( n<=bhi, logical_not(a70) )  )
        survi = AND(  n>=slo,  AND( n<=shi, a70 )  )
        b70 = 1.0* OR( birth , survi )  
        #
        a = beta70*b70 + nbeta70*a
    elif False: #r70
        norm70=diam*diam/((1-alf70)*diam*diam +  (alf70)*di70*di70  )
        ###print norm70
        n60 =  (1-alf70)*diam*diam*filters.uniform_filter(a,diam,mode='wrap')  
        n70 =  (alf70)*di70*di70*filters.uniform_filter(a,di70,mode='wrap')  
        n=(n60+n70) * norm70
        a70=(a>=0.5)
        birth = AND(  n>=blo,  AND( n<=bhi, logical_not(a70) )  )
        survi = AND(  n>=slo,  AND( n<=shi, a70 )  )
        b70 = 1.0* OR( birth , survi )  
        #
        a = beta70*b70 + nbeta70*a
    elif True: #r75 l2x
        n751 = (diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
        n752 = (diam*diam*filters.uniform_filter(n751,diam,mode='wrap')  )
        #n753 = (diam*diam*filters.uniform_filter(n752,diam,mode='wrap')  )
        #n754 = (diam*diam*filters.uniform_filter(n753,diam,mode='wrap')  )
        n=n752
        a70=(a>=0.5)
        birth = AND(  n>=blo,  AND( n<=bhi, logical_not(a70) )  )
        survi = AND(  n>=slo,  AND( n<=shi, a70 )  )
        b70 = 1.0* OR( birth , survi )  
        a = beta70*b70 + nbeta70*a
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
        adaimage = transpose( ( ( asho)))
        ####print shape(image)
        #b = array(255*clip(image,0,1),'B')
        b = array(255*clip(adaimage,0,1),'B')
        # #b = array(clip(transpose(xx),0,255),'B')
        # #b = array(clip((yy),0,255),'B')
        pygame.surfarray.blit_array(surface,b[:w,:h])
        screen.blit(surface,(0,0))
        pygame.display.flip()
        time.sleep(sli)
#        print i, norm70
        print i

##debug print shape(blo)
##debug numpy.size(yy,0)
##debug typename(blo)

