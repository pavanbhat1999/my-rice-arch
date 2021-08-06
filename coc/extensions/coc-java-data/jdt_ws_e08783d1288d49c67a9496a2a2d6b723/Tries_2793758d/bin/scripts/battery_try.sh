#!/bin/bash
CURRENT_BAT=$(cat /sys/class/power_supply/BAT0/capacity);
while true;do
    
    if [ $CURRENT_BAT -lt 30 ]
    then
        notify-send "Low battery"
    fi
    sleep 10
done
    
