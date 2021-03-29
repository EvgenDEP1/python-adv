#!/bin/sh

echo "Starting time_messenger docker"
python3 "$KPK_BIN/iTTime_messenger/manage.py" runserver 0.0.0.0:8000
