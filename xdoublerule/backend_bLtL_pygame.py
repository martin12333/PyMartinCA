
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
    ####n41 = floor(0.5+diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
    #n41 = floor(0.5+diam*diam*filters.uniform_filter(a,diam ))   ##,mode='wrap')  )
    ###n42 = floor(0.5+diam*diam*filters.uniform_filter(n41,diam,mode='wrap')  )
    ##n=n41 #n42
    un = floor(0.5+diam*diam*filters.uniform_filter(da,diam ))   ##,mode='wrap')  )
    dn = floor(0.5+diam*diam*filters.uniform_filter(ua,diam ))   ##,mode='wrap')  )
    
    ubirth = AND(  un>=ubmin,  AND( un<=ubmax, logical_not(ua) )  )
    usurvi = AND(  un>=usmin,  AND( un<=usmax, ua )  )

    dbirth = AND(  dn>=dbmin,  AND( dn<=dbmax, logical_not(da) )  )
    dsurvi = AND(  dn>=dsmin,  AND( dn<=dsmax, da )  )
    
    ua = 1.0* OR( ubirth , usurvi )  
    da = 1.0* OR( dbirth , dsurvi )  
    
    a=0.7*ua + 0.3*da

    ##n753 = (diam*diam*filters.uniform_filter(n752,diam,mode='wrap')  )
    ##n754 = (diam*diam*filters.uniform_filter(n753,diam,mode='wrap')  )
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
            
        da51=a - averyold
        averyold = a
        
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
        am51=a.mean()
        sam51='{:.3f}'.format(am51)
        ada51=abs(da51)
        dam51=ada51.mean()
        sdam51='{:.3f}'.format(dam51)
        if (i % skip2)==0:
            print i, sam51, sdam51


##debug print shape(bmin)
##debug numpy.size(yy,0)
##debug type(bmax)

