from decimal import *
import golly as g
def setrange(x):
	#ltlrangeconvert.py
	#A script to change the range
	#but keep MOST of the dynamics
	#DISCLAIMER: Drastic range changes will remove the dynamics.
	#Thanks to Dean Hickerson's algorithm!
	#By Saka.
	getcontext().prec = 8
	fullrule = g.getrule()
	sections = fullrule.split(",")
	r = sections[0]
	b = sections[4]
	s = sections[3]
	c = sections[1]
	m = sections[2]
	n = sections[5]
	#Filter n so :Txxx don't get involved
	nlist = n.split(":")
	npure = nlist[0]
	#Aaand filter r so the R is gone
	rpure = int(r[1:])
	#Getting bmin and bmax outta that string...
	bpure = b.translate(None,"B")
	blist = b[1:].split("..")
	bmin = int(blist[0])
	bmax = int(blist[1])
	#Now for smin and smax...
	spure = s.translate(None,"S")
	slist = s[1:].split("..")
	smin = int(slist[0])
	smax = int(slist[1])
	#Input time
	try:
		rangeto = x
	except:
		rangeto=g.prompt("","5")
	rangetostr = str(rangeto)
	#Now for calculations!
	meaningoflife = (2*Decimal(rangeto)+1)**2/(2*Decimal(rpure)+1)**2
	newbmin = str(int(round(bmin*meaningoflife))) #Huh. Decimal to number to integer to string
	newbmax = str(int(round(bmax*meaningoflife)))
	newsmin = str(int(round(smin*meaningoflife)))
	newsmax = str(int(round(smax*meaningoflife)))
	newrule = "R"+rangetostr+","+c+","+m+","+"S"+newsmin+".."+newsmax+","+"B"+newbmin+".."+newbmax+","+npure
	g.setrule(newrule)
g.reset()
g.getevent()
base=100
down=range(base,0,-1) #descending
up=range(base,500) #ascending
x=up+range(500,0,-1)
for i in x:
	setrange(i)
	g.show(str(i))
	for j in xrange(1):
		g.step()
		g.fit()
		g.update()
		a=g.getevent()
		skipcheck=True
		while not skipcheck and a!="key space none":
			if(a=="key z none"):
				g.setstep(g.getstep()-1)
				g.update()
			elif(a=="key x none"):
				g.setstep(g.getstep()+1)
				g.update()
			a=g.getevent()
