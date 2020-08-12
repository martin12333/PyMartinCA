#!/bin/bash

#`#--dry-run` --update 

echo '========================================'
echo '========================================'
echo '========================================'
echo phys to virt

########luckybackup

####rsync -h --progress --stats -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/PyMartinCA/beta/JUPYTER/ martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/JUPYTER/

####rsync -h --progress --stats -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/PyMartinCA/beta/ martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/

####rsync -h --progress --stats -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/PyMartinCA/ martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/

rsync -h --progress --stats -r -tgo -p --update --protect-args -e "ssh -p 2223" /home/martin/Dropbox/grdr20/ martin@127.0.0.1:/home/martin/grdr20/

echo '========================================'
echo '========================================'
echo '========================================'
echo virt to phys
rsync -h --progress --stats -r -tgo -p --update --protect-args -e "ssh -p 2223"  martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/JUPYTER/   /home/martin/Dropbox/grdr20/PyMartinCA/beta/JUPYTER/

echo '========================================'
echo virt to phys
rsync -h --progress --stats -r -tgo -p --update --protect-args -e "ssh -p 2223"  martin@127.0.0.1:/home/martin/grdr20/PyMartinCA/beta/testOfRules/   /home/martin/Dropbox/grdr20/PyMartinCA/beta/testOfRules/


echo '========================================'
echo '========================================'
echo '========================================'
echo virt to phys

sshport=2223 ;  rsync  `#--dry-run`  --backup --backup-dir=$HOME/Documents/rsync.bak/   -v   -h  -r -tgo -p --update --files-from=$HOME/Dropbox/git...ls-files  --protect-args   -e "ssh -p $sshport" martin@127.0.0.1:/home/martin/  ~/Dropbox/$sshport/

echo '========================================'
echo '========================================'
echo '========================================'
