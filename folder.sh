#!/bin/bash
gdrive upload downloads/"$1" -r -p "<drive folder id>"
rclone link googledrive:"$1"
rm -rf downloads/"$1"