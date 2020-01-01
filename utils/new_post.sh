#!/usr/bin/env bash

# remove spaces, make lowercase
filename=`echo $@| tr ' ' '-' | tr '[:upper:]' '[:lower:]'`
title="$@"
date=`date +"%b %d %Y"`

sed -e "s/:title:/$title/" \
    -e "s/:slug:/$filename/" \
    -e "s/:date:/$date/" \
    ./utils/tmpl.md > "./content/posts/${filename}.md"
