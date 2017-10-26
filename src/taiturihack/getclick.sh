#!/bin/bash

MOUSE_ID=$(xinput --list | grep -i -m 1 'IBM' | grep -o 'id=[0-9]\+' | grep -o '[0-9]\+')

#
#STATE1=$(xinput --query-state $MOUSE_ID | grep 'button\[' | sort)
#while true; do
#    sleep 0.2
#    STATE2=$(xinput --query-state $MOUSE_ID | grep 'button\[' | sort)
#    comm -13 <(echo "$STATE1") <(echo "$STATE2")
#    STATE1=$STATE2
#done

STATE=$(xinput --query-state $MOUSE_ID | grep 'button\[1]' | sort)
if [[ $STATE == *"down"* ]]; then echo "1";
else echo "0";
fi
