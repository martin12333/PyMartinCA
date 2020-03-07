
# In[2]:


from pylab import *
from scipy.ndimage import filters,measurements
import pygame
from pygame import surfarray
matplotlib.rc("image",cmap="gray")
matplotlib.rc("image",interpolation="nearest")
pygame.init()
OR = logical_or
AND = logical_and
def unif(lo,hi,size=1):
    if size==1: return rand()*(hi-lo)+lo
    if type(size)==int: return rand(size)*(hi-lo)+lo
    return rand(*size)*(hi-lo)+lo


# In[3]:


#w,h = 800,768
#w,h = 768,768
h=1024
w=h*2
#w=h
screen = pygame.display.set_mode((w,h))
surface = pygame.Surface((w,h),depth=8)

def animate(images,n=20):
    for i,image in enumerate(images):
        if i>=n: break
        #MN: parameter-map needs: adapt matrix orientation to pygame
        ######adaimage = transpose( fliplr( flipud( image)))
        adaimage = transpose( ( ( image)))
        ####print shape(image)
        #b = array(255*clip(image,0,1),'B')
        b = array(255*clip(adaimage,0,1),'B')
        # #b = array(clip(transpose(xx),0,255),'B')
        # #b = array(clip((yy),0,255),'B')
        pygame.surfarray.blit_array(surface,b[:w,:h])
        screen.blit(surface,(0,0))
        pygame.display.flip()
    return image

def random(p):
    #MN: parameter-map needs a change also here:
    # matrix orientation, not pygame
    return 1.0*(rand( h, w )<p)    
    #return 1.0*(rand(w,h)<p)

def iterate(f,a,n=100000):
    for i in range(n):
        yield a
        a = f(a)
        #MN
        print i
        a = f(a)
    yield a


### Parameter map

# In[*]:

# tab completion works

diam =5 
#diam =3 

#xlo=-9    #0
#xhi=99
#ylo=xlo
#yhi=xhi   

xlo=0    #0
xhiex=3
ylo=xlo
yhiex=xhiex  


blo= 34


# #x11 = floor(linspace(xlo, xhi + 0.999, w))
#x11 = (linspace(xhi + 0.999,xlo, h))
#4
#x11 = linspace(xlo, xhi + 0.999, w)
x11 = linspace(xlo, xhiex, w)

# #y11 = floor(linspace(yhi + 0.999 , ylo, h))
#y11 = (linspace(ylo, yhi + 0.999 , w))
#4 y11 =linspace(  ylo,  yhi + 0.999 , h)
#5
#y11 = linspace(yhi + 0.999 , ylo, h)
y11 = linspace(yhiex , ylo, h)

#(xx, yy) = meshgrid(x11, y11)
xx, yy = meshgrid(x11, y11)
 
bhi, blo = modf(xx) 
blo = 6 + blo
bhi = 6 + 6*bhi

#blo = 2 + blo
#bhi = 7*bhi

#blo = 6 + blo
#bhi = 8 + 4*bhi

#blo=7 - 1 + xx 
#blo = xx / 10.0    
#blo = yy/ 10.0
#bhi=frac()
# #bhi=fliplr(xx)  #xx
#bhi=mod(yy,10)
#bhi=mod(xx,10)

shi, slo = modf(yy) 
slo = 6 + slo
shi = 9 + 6*shi

#slo = 2 + slo
#shi = 9*shi

#slo = 6 + slo
#shi = 9 + 4*shi
#slo=7 - 1 + yy
#slo=xx / 10.0   #blo    #xx
#slo= yy / 10.0   #blo    #xx
# ####shi=flipud(yy)   # yy
#shi=mod(xx, 10)
#shi=mod(yy, 10)

###debgloby=0
def param_map_largtl(s):
    a = array(s!=0,'f')
    n = floor(0.5+diam*diam*filters.uniform_filter(a,diam,mode='wrap')  )
    #n = floor(0.5+3*3*filters.uniform_filter(a,3,mode='wrap')  )
    #n = floor(0.5+11*11*filters.uniform_filter(a,11,mode='wrap')  )
    birth = AND(  n>=blo,  AND( n<=bhi, logical_not(a) )  )
    survi = AND(  n>=slo,  AND( n<=shi, a )  )
    #return 1.0*AND(  n>=blo,  OR( n<=bhi, AND(n<=shi,a) )  )
    return 1.0* OR( birth , survi )  

print shape(random(0.5))
y=animate(iterate(param_map_largtl,random(0.5)),3000)
print shape(blo)
print shape(y)


# # In[56]:
# 
# #debgloby.shape
# #size(yy)
# #imshow(animate.func_dict.image)
# get_ipython().magic(u'dirs')
# #x=animate.func_dict.viewitems()
# numpy.size(yy,1)
# numpy.size(yy,0)
# print shape(transpose(yy))
# print shape(rand(w,h))
# #imshow(blo)
# #typename(blo)
# print shape(blo)
# print shape(yy)


# Out[56]:

#     (2048, 1024)
#     (2048, 1024)
#     (1024, 2048)
#     (1024, 2048)
# 

## RealLife:

# - further generalization
# - let the neighborhood go to infinity
# - continuum limit
# - Pivato: _RealLife: the continuum limit of Larger Than Life cellular automata_
# - http://arxiv.org/abs/math.DS/0503504
