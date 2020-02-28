#!/bin/bash

eval $(cat file_mover.conf)
touch "$LOGFILENAME"
PID=$$
for file in $(find "$SOURCEDIR" -type f -size +0c -printf "%f\n"); do

	if $( echo $(tail -n 1  "$SOURCEDIR/$file" 2>/dev/null)| uuidparse -o TYPE -n | grep -v invalid 1>/dev/null)
	then
		[[ -e $SOURCEDIR/$file ]] && mv -u "$SOURCEDIR/$file" /tmp/ 2>/dev/null|| continue
		new_file=$(awk -v date=$(date +%Y-%m-%d) 'NR==1 {print $1"-"$2"_"$3"-"date}' "/tmp/$file")
		mv -u "/tmp/$file" "$TARGETDIR/$new_file" 2>/dev/null
		echo "$PID File $file moved to $TARGETDIR/$new_file" >> "$LOGFILENAME"
	else
		continue
	fi

done
