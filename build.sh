hugo
rm -rf ../duereg.github.io/hockey/ ../duereg.github.io/images/ ../duereg.github.io/pages/ ../duereg.github.io/posts/ ../duereg.github.io/scripts/ ../duereg.github.io/styles/ ../duereg.github.io/vendor/
cp -r ./public/* ../duereg.github.io
cd ../duereg.github.io
git add -A
git commit -m 'newest version'
git push origin master
