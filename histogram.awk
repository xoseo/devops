{	
	len = 10
	arr[int($1/len)]++
	next } 
END {
	min=0
	for (i in arr) {
		if ( min == 100) {
			printf min ": " arr[i] " "
		} else {
			printf min " - " min+len-1 ": " arr[i] " "
		}
		for (j = 0; j < arr[i]; j++)
			printf "*"
		printf "\n"
		min += len
	}
}
