#!/bin/bash

#for ((;;)); do xdotool type --window 16777222 "$(shuf -n1  /usr/share/dict/words) 4576"; sleep 2; done
for ((;;)); do 
	win="$(xdotool search --name taituri)"
	if [ win!="" ]; then
		xdotool type --window ${win} "qwerytiuiopasdfghkjlzxcvbnm,.-1234567890 "
		xdotool key --window ${win} Return
	fi
	sleep 2
done
