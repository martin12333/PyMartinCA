
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
        print i


##debug print shape(blo)
##debug numpy.size(yy,0)
##debug typename(blo)
