#!/bin/sh

echo "Installing node modules : "
echo "npm install"
npm install

echo "Init git repository : "
echo "git init"
git init

echo "Installing Pico theme : "
echo "git submodule add https://github.com/negrel/hugo-theme-pico.git ./themes/pico"
git submodule add https://github.com/negrel/hugo-theme-pico.git ./themes/pico
git submodule add https://github.com/pacollins/hugo-future-imperfect-slim.git ./themes/hugo-future-imperfect-slim

./update.sh

node_modules/.bin/hugo --gc --minify
