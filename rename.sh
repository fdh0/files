#!/bin/bash
name=0
for files in `ls --file-type *.jpg *.png *.jpeg *.bmp`
do
    # 指定后缀名
    ext=".jpg"
    # 指定文件名(这里采用加1的方式)
    name=$(echo "$name + 1"|bc)
    # 拼接成完整文件名
    filename='cat'_$name$ext
    # 修改文件名
    mv $files $filename
done
