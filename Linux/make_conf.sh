#!/bin/bash
usage () {
	echo "Usage: $0 [options]
	OPTIONS:
	-t | --template - path to template
	-r | --result - path to converted result
	"
}

argnum () {
if [[ $# -ne 4 ]]; then
	echo "Передано неверное число аргументов!"
	exit 1
fi
}

make_config () { 
argnum $*

while [[ -n "$1" ]]; do
	case "$1" in
		-t | --template )
			template="$2"
			shift 2
			;;
		-r | --result )
			result="$2"
			shift 2
			;;
		* )
		usage
		exit 2
			;;
	esac
done

if [[ -z "$template" ]]; then
	echo "Не указан параметр -t"
	usage
	exit 3
elif [[ -z "$result" ]]; then
	echo "Не указан параметр -r"
	usage
	exit 3
fi

if [[ ! -f "$template" ]] && [[ ! -r "$template" ]]; then
	echo "File not found or reading not allowed"
	exit 4
fi

re='\{\%[[:space:]]*([0-9A-Za-z_\-]+)[[:space:]]*\%\}*'

cat "$template" | while read l || [[ -n $l ]]; do
	while [[ "$l" =~ $re ]] ; do
	   	VAR0=${BASH_REMATCH[0]}
	   	VAR1=${!BASH_REMATCH[1]}
		l=${l//$VAR0/$VAR1}
	done
	echo $l >> "$result"
done

}

