#!/bin/bash


#git
echo "git commit message:"
read git_msg

git add .
git commit -m "${git_msg}"
git push