# This is the bash script to update all git repos under current directory
#!/bin/bash

dirlist=$(find `pwd` -maxdepth 1 -type d)

for dir in $dirlist
do
cd $dir
git pull origin master
cd ..
done

