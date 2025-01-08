1. Fix error regarding https://ta-lib.github.io/ta-lib-python/install.html

2.YFinace Documentation
https://algotrading101.com/learn/yahoo-finance-api-guide/

3. NIFTY 500 stocks list
https://www.nseindia.com/products-services/indices-nifty500-index


RUNNING The Programme
1. To run the program after logout from GCP vm
./cron.sh
2./run.sh or python main.py

=================== TROUBLE SHOOTING STOCK MUTUAL FUND ANALYZERS =================
Python Libraries used
1. Yfinance
2. Ta-Lib
3. pip install beautifulsoup4




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
==================================================================================


================= TROUBLE SHOOTING Stock news analyzer  =================
1.pip install feedparser
==================================================================================



================= TROUBLE SHOOTING Trend Analyzer =================
1. pip install trendspy
==================================================================================



================= TROUBLE SHOOTING AI Model =================
Python packages
1. pip install jupyter
2. pip install phidata yfinance googlesearch-python
3. pip install pycountry
4. pip install google-genai
5. pip install google-generativeai
6. Search and interpret news articles.
7. pip install crawl4ai


Enable Google Gemini api
https://www.youtube.com/watch?v=BKT1CyXrfks
==================================================================================

