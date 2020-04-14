from __future__ import print_function

from scipy.ndimage import filters
import time

import matplotlib.pyplot as plt

pygame.init()

screen = pygame.display.set_mode((w,h))
surface = pygame.Surface((w,h),depth=8)

OR = logical_or
AND = logical_and

for i in range(niter):

    n41 =   diam*diam*filters.uniform_filter(0.0+a,diam )   ##,mode='wrap')  )  
    n=n41.round()   
    birth = AND(  n>=bmin,  AND( n<=bmax, logical_not(a) )  )
    survi = AND(  n>=smin,  AND( n<=smax, a )  )
    a =  OR( birth , survi )  
    if (i % step1)==0:

        if bfade:
            afade = q*a + (1-q)*afade
            asho=afade
        else:
            asho=0+a
            
        ada51= logical_xor(a, averyold)  
        averyold =a 
        
        adaimage = transpose( ( ( asho)))
        b = array(255*clip(adaimage,0,1),'B')

        pygame.surfarray.blit_array(surface,b[:w,:h])
        screen.blit(surface,(0,0))
        pygame.display.flip()

        time.sleep(sleep1)

        if (i % step2)==0:
            am51=(0.0+a).mean()
            sam51='{:.3f}'.format(am51)
            dam51=ada51.mean()
            sdam51='{:.3f}'.format(dam51)
            print( i, sam51, sdam51)

