import imp
#import importlib
import pmc_backend

imp.reload(pmc_backend)

exec_backend=pmc_backend.exec_backend

global a

a=0

exec_backend()
###e x e c f i l e ('backend.py')
