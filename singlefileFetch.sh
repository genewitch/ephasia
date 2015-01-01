#!/bin/bash

current="$1"

while [ "$current" -lt "$2" ]
do
echo http://dreamt.org/ytsejamarchives/1000/ytsejam.$current
((current += 1))
done

echo "done"
