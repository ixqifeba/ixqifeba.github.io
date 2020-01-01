#!/usr/bin/env bash

# remove spaces, make lowercase
filename=`echo $@| tr ' ' '-' | tr '[:upper:]' '[:lower:]'`
title="$@"
date=`date +"%b %d %Y"`
filepath="./content/posts/${filename}.md"

sed -e "s/:title:/$title/" \
    -e "s/:slug:/$filename/" \
    -e "s/:date:/$date/" \
    ./utils/tmpl.md > "$filepath";

#start vim
vim "$filepath"
