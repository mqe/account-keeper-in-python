#!/bin/bash
#this is a comment-the first line sets bash as the shell script
printf '\e[8;100;81t'
printf '\e[3;0;0t'
mydir="$(dirname "$BASH_SOURCE")"
cd "$mydir/files" /tmp
python accounts.py all;
exit;