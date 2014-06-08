#!/usr/bin/env bash
 
function optimize
{
    echo $1
    filesize=`stat -c %Z "$1"`
    if [[ $filesize -lt 10000 ]]; then
        jpegtran -copy none -optimize "$1" > "$1.bak"
        echo "pet"
    else
        jpegtran -copy none -progressive "$1" > "$1.bak"
        echo "grand"
    fi
    
    if [[ $filesize -lt `stat -c %Z "$1.bak"` ]]; then
        echo "compression plus lourde"
        rm "$1.bak"
    else
        echo "good!"
        mv "$1.bak" "$1"
    fi
}
find . -name '*.jpg' -type f -print0 |while read -d $'\0' i; do optimize "$i"; done

find . -name '*.png' -type f -print0 |while read -d $'\0' i; do optipng "$i"; done

