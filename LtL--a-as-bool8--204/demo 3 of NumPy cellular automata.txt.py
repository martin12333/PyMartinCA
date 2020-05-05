martin@sdb3a45g:~$ ssh  -p 2223      -L 8888:localhost:8888         martin@127.0.0.1
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.18.0-15-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

544 packages can be updated.
321 updates are security updates.

Your Hardware Enablement Stack (HWE) is supported until April 2023.
Last login: Sat May  2 17:10:43 2020 from 10.0.2.2
martin@martin-VirtualBox:~$ cd grdr20/PyMartinCA/beta/205density-plot/
martin@martin-VirtualBox:~/grdr20/PyMartinCA/beta/205density-plot$ ipython
Python 2.7.17 (default, Nov  7 2019, 10:07:09) 
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: history
history

In [2]: history -g hist
15/47: history
26/19: history
26/23: history
26/28: history
36/1: history -g hist
72/13: history
   1: history
   2: history -g hist

In [3]: hist -g hist
15/47: history
26/19: history
26/23: history
26/28: history
36/1: history -g hist
72/13: history
   1: history
   2: history -g hist
   3: hist -g hist

In [4]: import numpy as np
   ...: 
   ...: from scipy.ndimage import filters
   ...: 

In [5]: #parameters are described at PARAMETERS.txt
   ...: # CGOL
   ...: r=1; bmin=3; bmax=3; smin=3; smax=4
   ...: 

In [6]: world=[
   ...: [0,1,0,0],
   ...: [0,0,1,0],
   ...: [1,1,1,0],
   ...: [0,0,0,0],
   ...: ] # a glider

In [7]: import scipy.ndimage 
   ...: 
   ...: 

In [8]: ?scipy.ndimage.*2d*


In [9]: ??scipy.ndimage.*2d*
Object `scipy.ndimage.*2d*` not found.

In [10]: ?scipy.ndimage.*2*


In [11]: ?scipy.ndimage.**

In [12]: ?scipy.ndimage.*1*
scipy.ndimage.convolve1d
scipy.ndimage.correlate1d
scipy.ndimage.gaussian_filter1d
scipy.ndimage.generic_filter1d
scipy.ndimage.maximum_filter1d
scipy.ndimage.minimum_filter1d
scipy.ndimage.spline_filter1d
scipy.ndimage.uniform_filter1d

In [13]: kernel = [[1, 1, 1],[ 1 ,1, 1],[ 1, 1, 1]]  # define neighbors
    ...: 

In [14]: kernel
Out[14]: [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

In [15]: kr=np.array(kernel)

In [16]: kr
Out[16]: 
array([[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]])

In [17]: ?scipy.ndimage.*conv*
scipy.ndimage.convolve
scipy.ndimage.convolve1d

In [18]: ?scipy.ndimage.convolve

In [19]: ?scipy.ndimage.filters.convolve

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
