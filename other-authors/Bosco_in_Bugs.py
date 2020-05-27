# Bosco_in_Bugs.py
# painfully slow Larger than Life Bugs rule simulator
# (pretty much only works for small single patterns like Bosco...)

import golly as g

g.addlayer()
g.new("Bosco")
g.putcells(g.parse("4b2o$2b6o$b3o3b2o$4o4bo$4o4b2o$4o2bob2o$9o$b8o$2b6o$3b5o!"))

if g.numstates()>2: g.exit("Please switch to a two-state rule.")

while 1:
  rmin=g.getrect()
  r=[rmin[0]-5,rmin[1]-5,rmin[2]+10,rmin[3]+10]
  newlist=[]
  for j in range(r[1],r[1]+r[3]):
    for i in range(r[0],r[0]+r[2]):     
      count=0
      for y in range(-5,6):
        for x in range(-5,6):
          count+=g.getcell(i+x,j+y)
      # for now, just hard-code the Bugs rule
      #   (we'll generalize later)
      #     (and speed things up a lot)
      # Bugs rule = R5,C0,M1, S34..58, B34..45,NM
      if g.getcell(i,j)==1:
        if count<34 or count>58: newlist+=[i,j,0]
      else:
        if count>=34 and count<=45: newlist+=[i,j,1]
  if len(newlist)%2==0: newlist+=[0]
  g.putcells(newlist,0,0,1,0,0,1,"copy") # use copy mode so the state-0 cells overwrite state-1 cells
  g.setgen("+1")
  g.update()
