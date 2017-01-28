#!/bin/bash
read N
(( 1 <= N && N <= 500 )) || echo error
count=0
sum=0
while [ $count -lt $N ]
do
	read x
	(( -10000 <= x && x <= 10000 )) || echo error
	(( count++ ))
	(( sum+=x ))
done
res=$(echo "$sum/$N" | bc -l)
printf "%.3f\n" $res
