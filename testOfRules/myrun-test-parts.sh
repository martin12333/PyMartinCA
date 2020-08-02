for x in lifelib-input/parts-todo/x*
do

    echo $x;
    wc lifelib-input/parts-todo/part.csv

    sleep 1

    mv -v $x lifelib-input/parts-todo/part.csv

    python3 testOfRules-from-csv-or-cube-or-random.py.417.py

    mv -v  lifelib-input/parts-todo/part.csv lifelib-input/parts-todo/done


done


