#!/bin/bash


#demo "web scrapping"
wget -p -k -nH -P docs/ 127.0.0.1:8000


#git
echo "git commit message:"
read git_msg

git add .
git commit -m "${git_msg}"
git push