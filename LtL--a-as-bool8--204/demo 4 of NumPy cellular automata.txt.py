
In [4]: import numpy as np

In [5]: #parameters are described at PARAMETERS.txt
   ...: # CGOL
   ...: r=1; bmin=3; bmax=3; smin=3; smax=4

In [7]: import scipy.ndimage 


In [13]: kernel = [[1, 1, 1],[ 1 ,1, 1],[ 1, 1, 1]]  # define neighbors

In [15]: kr=np.array(kernel)

In [16]: kr
Out[16]: 
array([[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]])


In [20]: scipy.ndimage.convolve(a,kr)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-20-845572c24220> in <module>()
----> 1 scipy.ndimage.convolve(a,kr)

NameError: name 'a' is not defined

In [21]: world
Out[21]: [[0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]

In [22]: a=np.array(world)

In [23]: scipy.ndimage.convolve(a,kr)
Out[23]: 
array([[2, 3, 3, 1],
       [4, 5, 4, 2],
       [3, 4, 3, 2],
       [3, 3, 2, 1]])

In [24]: n=scipy.ndimage.convolve(a,kr)

In [25]: n
Out[25]: 
array([[2, 3, 3, 1],
       [4, 5, 4, 2],
       [3, 4, 3, 2],
       [3, 3, 2, 1]])

In [26]: 
    ...: OR = np.logical_or
    ...: AND = np.logical_and
    ...: 

In [27]: world=[
    ...: [0,0,0,0],
    ...: [0,1,0,0],
    ...: [0,1,0,0],
    ...: [0,1,0,0],
    ...: [0,0,0,0],
    ...: ] # a blinker
    ...: 

In [28]: a=np.array(world)

In [29]: n=scipy.ndimage.convolve(a,kr)

In [30]: n
Out[30]: 
array([[1, 1, 1, 0],
       [2, 2, 2, 0],
       [3, 3, 3, 0],
       [2, 2, 2, 0],
       [1, 1, 1, 0]])

In [31]: birth = AND(  n>=bmin,  AND( n<=bmax, np.logical_not(a) )  )
    ...: 
    ...: 

In [32]: birth
Out[32]: 
array([[False, False, False, False],
       [False, False, False, False],
       [ True, False,  True, False],
       [False, False, False, False],
       [False, False, False, False]], dtype=bool)

In [33]: survi = AND(  n>=smin,  AND( n<=smax, a )  )
    ...: 
    ...: 

In [34]: survi
Out[34]: 
array([[False, False, False, False],
       [False, False, False, False],
       [False,  True, False, False],
       [False, False, False, False],
       [False, False, False, False]], dtype=bool)

In [35]: a =  OR( birth , survi )  
    ...: 
    ...: 

In [36]: a
Out[36]: 
array([[False, False, False, False],
       [False, False, False, False],
       [ True,  True,  True, False],
       [False, False, False, False],
       [False, False, False, False]], dtype=bool)

In [37]: 
