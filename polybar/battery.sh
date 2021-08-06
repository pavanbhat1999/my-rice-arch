#!/bin/bash

: "${BAT_TMP:=/tmp/batterytmp}"
: "${THRESHOLD:=70}"

let bat=/sys/class/power_supply/BAT0/capacity
if [[ -f "$BAT_TMP" ]]; then
        ((bat > THRESHOLD)) && rm -f "$BAT_TMP"
else
        ((bat <= THRESHOLD)) && {
                notify-send -u critical "WARNING: low battery"
                touch "$BAT_TMP"
        }
fi

echo "$bat%"
