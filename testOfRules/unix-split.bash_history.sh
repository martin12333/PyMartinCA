wc awk-random.csv 
man split
cd lifelib-input/
ll
mkdir parts-todo
cd parts-todo/
split --lines=48 --numeric-suffixes --suffix-length=4 --verbose ../../awk-random.csv 
ll
cd ../..
cd lifelib-input/parts-todo/
x=x0000
cd ../..
x=lifelib-input/parts-todo/x0000
echo $x
mv -v $x lifelib-input/parts-todo/part.csv
wc lifelib-input/parts-todo/part.csv
mv -v  lifelib-input/parts-todo/part.csv lifelib-input/parts-todo/done
for x in lifelib-input/parts-todo/x*; do echo $x; done
mc
ll
history 
mc ../..
mc
x=lifelib-input/parts-todo/x0000
mv -v $x lifelib-input/parts-todo/part.csv
#python3 testOfRules-from-csv-or-cube-or-random.py
python3 testOfRules-from-csv-or-cube-or-random.py
mc
history 
cd lifelib-input/parts-todo/
split --lines=48 --numeric-suffixes --suffix-length=4 --verbose ../convert--output0.csv 
cd ../..
history 
x=lifelib-input/parts-todo/x0000
mv -v $x lifelib-input/parts-todo/part.csv
python3 testOfRules-from-csv-or-cube-or-random.py
