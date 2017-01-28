#!/bin/bash
read x
read y
read z
if [ $x -ge 1 ] && [ $y -ge 1 ] && [ $z -ge 1 ] && [ $x -le 1000 ] && [ $y -le 1000 ] && [ $z -le 1000 ]
then
	if [ $x == $y ] && [ $y == $z ]
	then
		echo "EQUILATERAL"
	elif [ $x == $y ] || [ $y == $z ] || [ $z == $x ]
	then
		echo "ISOSCELES"
	else
		echo "SCALENE"
	fi
else
	echo "values out of valid range"
fi
