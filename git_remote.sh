#!/bin/bash

cd $1

git remote add waxes27 https://github.com/waxes27/$2
git push waxes27
rm -rf ../$1
cd ..
