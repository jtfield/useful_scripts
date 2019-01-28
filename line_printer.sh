#! /bin/bash

file=$1
secondfile=$2

first_num=''
second_num=''
cat $file | while read line;
do
	#echo "$line"
	#if [ ! -z $(grep ">" "$line") ]; then echo "$line"; fi
	if [[ $line = \>* ]]
	then
		#echo "$line"
		if [[ $line = *_[1-9]_* ]]
		then
			#echo "$line has a number"
			extractedNum="${line#*_}"     # Remove through first :
			extractedNum="${extractedNum%%_*}"  # Remove from next : to end of string
			#echo "$extractedNum"
			first_num="$extractedNum"
			#echo "begin first_num"
			#echo "$first_num"
			#echo "end first_num"
			cat $secondfile | while read secondline;
                        do
                                second_extract_num="${secondline#*_}"
                                second_extract_num="${second_extract_num%%_*}"
                                second_num="$second_extract_num"
				#echo "$first_num first num"
				#echo "$second_num second num"
				if [[ $first_num == $second_num ]]
				then
					echo "match"
					echo "replacing $secondline with $line"
					
					sed -i -e "s/$secondline/$line/g" $secondfile
				else
					echo "no match"
				fi
			done
		else
			echo "no number"
		fi
	else
		echo "no match"
	fi
	echo "BREAK BREAK BREAK"
done
