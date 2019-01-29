#! /bin/bash

file=$1
secondfile=$2

# initialize variables for the numbers that will be compared to eachother
first_num=''
second_num=''

# read the fasta file and loop through it
# looking for lines that start with > indicating a contig name
cat $file | while read line;
do
	#echo "$line"
	#if [ ! -z $(grep ">" "$line") ]; then echo "$line"; fi
	if [[ $line = \>* ]]
	then
		#echo "$line"
		
		# if a carrot ( > ) is found on the line
		# check if there is a number in that line surrounded by two _'s
		# example: "taxon_5_1.fq"

		if [[ $line = *_[1-9]_* ]]
		then
			#echo "$line has a number"


			# if a number is found, strip away the first portion of the name and the last portion of the name

			extractedNum="${line#*_}"     # Remove through first :
			extractedNum="${extractedNum%%_*}"  # Remove from next : to end of string
			#echo "$extractedNum"
			first_num="$extractedNum"
			#echo "begin first_num"
			#echo "$first_num"
			#echo "end first_num"

			# after stripping away the non-numeric portions of the name
			# loop through the file with the original names
			# seperate the number in the name and compare those numbers to eachother to find matches
			# if they match, replace the name in the fasta with the original name

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
					echo "replacing $line with $secondline"
					
					sed -i -e "s/$line/$secondline/g" $file
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
