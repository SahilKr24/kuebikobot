#!/bin/bash

rclone copy downloads/"${1}" gdrive:"${DRIVE_FOLDER_NAME}"
rclone link gdrive:"${DRIVE_FOLDER_NAME}"/"${1}"
rm -rf downloads/"$1"