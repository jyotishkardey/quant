1. Fix error regarding https://ta-lib.github.io/ta-lib-python/install.html

2.YFinace Documentation
https://algotrading101.com/learn/yahoo-finance-api-guide/

3. NIFTY 500 stocks list
https://www.nseindia.com/products-services/indices-nifty500-index


RUNNING The Programme
./run.sh

TROUBLE SHOOTING
1. To update nifty 500 universe update the file ind_nifty500list.csv from NSE website
2. Ta-lib so error loading in GCP. Since the compute node is reset after 20 min of unuse and the storage is not persistent,
run install-ta-Lib.sh 
3. Error with Twillo whatsapp library 
The export of following variables does not work correctly from script
export TWILIO_ACCOUNT_SID=
export TWILIO_AUTH_TOKEN=
4. Cron Commands
crontab -e
sudo service cron start
sudo service cron status

Export them manually
