{	
	count++
	len = 10
	arr[int($1/len)]++
	next } 
END {
	min=0
	lenarr=length(arr)
	for (i=0; i<lenarr; i++) {
		if ( min == 100) {
			#printf min ": " arr[i] " (" arr[i]/count*100 "%)"
			printf "%d :\t%d %f%% ",min,arr[i],arr[i]/count*100
		} else {
			#printf min " - " min+len-1 ": " arr[i] " (" arr[i]/count*100 "%)"
			printf "%d - %d : %d %f\%% ",min,min+len-1,arr[i],arr[i]/count*100
		}
		for (j = 0; j < arr[i]; j++)
			printf "*"
		printf "\n"
		min += len
	}
}
