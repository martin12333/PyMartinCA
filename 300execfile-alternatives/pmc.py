import sys
import os

#import imp
import importlib

############

#import r0 as p

pnamepy = sys.argv[-1]
r0py=os.path.split(pnamepy)[-1]
r0name=os.path.splitext(r0py)[0]

print(r0name)

if r0name!='pmc':
    p=importlib.import_module(r0name)

###########

###import pmc_backend
###from  pmc_backend import *

###imp.reload(pmc_backend)

###exec_backend=pmc_backend.exec_backend


a=p.a0

#def exec_backend():

    #global a

a+=1

#a+=2
#a+=3
print(a)
print(id(a))
#print(__name__)

