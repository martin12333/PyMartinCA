from __future__ import print_function

from scipy.ndimage import filters
import time

from pylab import *
import matplotlib.pyplot as plt

print(ndbmin* ndbmax* ndsmin* ndsmax)

print((1-pskip)*ndbmin* ndbmax* ndsmin* ndsmax)

#matplotlib.rc("image",cmap="gray")
#matplotlib.rc("image",cmap="hot")
##matplotlib.rc("image",cmap="RdYlGn")
##matplotlib.rc("image",cmap="BrBG")
#matplotlib.rc("image",cmap="copper")
#matplotlib.rc("image",cmap="afmhot")
#matplotlib.rc("image",cmap="autumn")
#matplotlib.rc("image",cmap="summer")

#matplotlib.rc("image",interpolation="nearest")


plt.ion()
#plt.ioff()


#img_plot = plt.imshow(a)
#plt.show(block=False)


####plt.matshow())
##plt.figure()
#### wrong: extent=(xlo, xhi, ylo, yhi) ) 
##, interpolation="nearest")
##, cmap = plt.cm.gray)



OR = logical_or
AND = logical_and


plotysum=zeros( (niter,1) )

for j in xrange(ns):


    for dbmax in range(ndbmax):

        bmax=bmax0+dbmax

        for dsmax in range(ndsmax):

            smax=smax0+dsmax


            for dbmin in range(ndbmin):

                bmin=bmin0+dbmin

                for dsmin in range(ndsmin):

                    smin=smin0+dsmin


                    if   rand()<pskip  or  bmax<bmin or (smax+1) < smin: continue ##  break
                    

                    p=0.5#0.3#0.5 #0.25 #0.16
                    #a = zeros( ( h, w ), dtype=bool) 
                    a=(rand( h, w )<p) 
                    
                    #a[ h0 : h0+h2 , w0 : w0+w2 ] = (rand( h2, w2 )<p) 

                    
                    afade = 0.1 * a
                    averyold = a 
                    averyold = 0 
                    aold120=0
                    aold420=0
                    aold840=0
                    
                    
                    
                    plotx=zeros( (niter,1) )
                    ploty=zeros( (niter,1) )
                    plotz=zeros( (niter,1) )
                    
                    dam51=0


                    for i in xrange(1,niter):

                        n41 =   diam*diam*filters.uniform_filter(0.0+a,diam )   ##,mode='wrap')  )  
                        n=n41.round()   
                        birth = AND(  n>=bmin,  AND( n<=bmax, logical_not(a) )  )
                        survi = AND(  n>=smin,  AND( n<=smax, a )  )
                        a =  OR( birth , survi )  

                        #as51=(0.0+a).sum()
                        am51=(0.0+a).mean()



                        plotx[i]=i
                        ploty[i]=am51 #as51

                        if (i % step1)==0:

                            if bfade:
                                afade = q*a + (1-q)*afade
                                asho=afade
                            else:
                                asho=0+a
                                
                            ada51= logical_xor(a, averyold)  
                            averyold =a 

                            oldi=i
                            olddam51=dam51
                            dam51=ada51.mean()
                            
                            plotz[i]=dam51

                            if dam51 == 0 : break
                            
                            ##adaimage = transpose( ( ( asho)))
                            ##b = array(255*clip(adaimage,0,1),'B')

                            ###imshow(asho)
                            #show()


                            #img_plot.set_data(asho)
                            #plt.draw()


                            ##time.sleep(sleep1)
                            
                            
                        if (i % 120)==0:
                            if (a==aold120).all():
                                print('p120:')
                                print(i,am51,dam51,bmin,bmax,smin,smax)
                                break
                            aold120=a

                        if (i % 840)==0:
                            if (a==aold840).all():
                                print('p840:')
                                print(i,am51,dam51,bmin,bmax,smin,smax)
                                break
                            aold840=a




                        if (i % step2)==0:
                            sam51='{:.3f}'.format(am51)
                            sdam51='{:.3f}'.format(dam51)
                            #print( i, sam51, sdam51)
                            
                            if am51 >0.250:#175: #0.200 :
                                break #################250


                    dam51=olddam51
                    sam51='{:.3f}'.format(am51)
                    sdam51='{:.3f}'.format(dam51)
                    #if dam51>0.005 and dam51<0.150 and am51>0.005 and am51<0.150:
                    #if dam51>0.001 and dam51<0.150 and am51>0.001 and am51<0.150:
                    #if dam51>0.000 and dam51<0.150 and am51>0.000 and am51<0.150 and oldi>70:
                    #if dam51>0.000 and dam51<0.150 and am51>0.000 and am51<0.150 and oldi>150:
                    #if dam51>0.001 and dam51<0.150 and am51>0.000 and am51<0.150 and oldi>450:
                    #if dam51>0.000 and dam51<0.150 and am51>0.000 and am51<0.150 and oldi>450:
                    #if  am51>0.000 and am51<0.175 and oldi>400:
                    if  dam51<0.150 and am51>0.000 and am51<0.175 and oldi>200:
                        print(oldi,sam51,sdam51,bmin,bmax,smin,smax)
                    
                    
                    if am51<0.999:#500:#100: #500: #0.200 :
                        plot(ploty[:oldi],'x')
                        #plot(ploty,'x-')
                        #plot(plotz,'x')
                        #plot( ploty[niter0:], plotz[niter0:],'x')
                    
                    
                    
                    
                    ##plotysum += ploty
                    
                    
                    
                    
