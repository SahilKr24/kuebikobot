#!/bin/bash

gdrive upload --service-account credentials.json $1 -p ${DRIVE_FOLDER} --share --delete 