#!/bin/bash

PROJECT_DIR="$HOME/Projects/cloud-reporting-pipeline"

cd $PROJECT_DIR

source venv/bin/activate

python main.py >> logs/cron.log 2>&1

