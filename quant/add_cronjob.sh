#!/bin/bash

sudo service cron status
cron_running=`echo $?`	

if [ $cron_running -ne 0 ]; then
sudo service cron start
# Define your cron job
CRON_JOB="0 4 * * 2-6 /home/jyotishkardey/quant/cron.sh"

# Add the cron job to the crontab
(crontab -l; echo "$CRON_JOB") | crontab -

# Print a success message
echo "Cron job added successfully!"
fi
