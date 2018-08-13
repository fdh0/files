# /usr/bin/env sh
DATA=$(cd `dirname $0`; pwd)

rm -rf ./train.txt

echo "Create train.txt..."

touch train.txt

find . -name 'cat*' | cut -d '/' -f2  | sed  's/$/& 1/' > train.txt
find . -name 'fish*' | cut -d '/' -f2 | sed  's/$/& 2/' >> train.txt
echo "Done.."
