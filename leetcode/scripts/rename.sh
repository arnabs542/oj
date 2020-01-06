#!/bin/bash

DIR=${1:-../}
echo "doing $DIR"

#find $DIR -name '99*.py'|while read f
find $DIR -name '*.cpp'|while read f
do
	#if [[ "$f" =~ "^[0-9]\+.\.+$" ]]
	if echo "$f"|egrep -o "[0-9]\..+"
	then
		echo "$f skipped";
	else
		num=`cat $f |head -n 10 |egrep '[0-9]+\. .+'|head -n 1 |sed -r 's/( \* )?([0-9]+)\. .+/\2/g'`
		if [[ ! -z $num ]]
		then
			#echo "git mv -v $f ../$num.$(basename $f)"
			git mv -v $f ../$num.$(basename $f)
		else
			echo "$f skipped";
		fi
	fi
done
