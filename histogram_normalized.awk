{	
	count++
	len = 10
	arr[int($1/len)]++
	next } 
END {
	min=0
	for (i in arr) {
		if ( min == 100) {
			printf min ": " arr[i] " (" arr[i]/count*100 "%)"
		} else {
			printf min " - " min+len-1 ": " arr[i] " (" arr[i]/count*100 "%)"
		}
		for (j = 0; j < arr[i]; j++)
			printf "*"
		printf "\n"
		min += len
	}
}
