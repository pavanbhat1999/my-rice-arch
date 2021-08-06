#!/bin/bash
df | awk 'FNR == 4 {print $4/1000000 "GB"}';

