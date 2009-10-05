#!/bin/sh
MYFILE=`date +%H%M%S`
mkdir $LOLDATE
for i in `seq -w 1 $1`
do
python getlulz.py $2$i.html | grep -E '.(png|jpg|jpeg|pdf|gif)$' >> $LOLDATE/wget-this-file-$LOLDATE
echo $i of $1
done
