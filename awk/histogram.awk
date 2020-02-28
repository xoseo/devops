{	
	len = 10
	arr[int($1/len)]++
	next } 
END {
	min=0
	lenarr=length(arr)
	for (i=0; i<lenarr; i++) {
		if ( min == 100) {
			printf "%d :\t%d ",min,arr[i]
		} else {
			printf "%d - %d : %d ",min,min+len-1,arr[i]
		}
		for (j = 0; j < arr[i]; j++)
			printf "*"
		printf "\n"
		min += len
	}
}