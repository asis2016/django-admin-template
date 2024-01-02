#!/bin/bash


#demo "web scrapping"
#wget -p -k -nH -P docs/ 127.0.0.1:8000
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent -P docs/ -nH 127.0.0.1:8000

#git
echo "git commit message:"
read git_msg

git add .
git commit -m "${git_msg}"
git push