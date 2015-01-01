#!/bin/bash

current="$1"

while [ "$current" -lt "$2" ]
do
wget http://emaildump/file.$current
((current += 1))
done

echo "done"
