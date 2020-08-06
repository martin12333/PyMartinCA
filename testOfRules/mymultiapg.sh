
cut -f 15 -d \   |while read y
do
	#(

	cd ~/apgmera
	#pwd 

	#  time ./apgluxe -L 1 -t 1  --rule "$y"  -n 2000 #1000
	time ./apgluxe   </dev/null     -L 1 -t 1  --rule "$y"  -n 2000 #1000
	#)
done

cd ~/apgmera
#pwd 

mv -i -v --target-directory=oldlog/ log.*.txt

#cd ~
#cd grdr20/PyMartinCA/beta/testOfRules/
