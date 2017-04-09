# Setup cron
configure the right timezone on the box

# Jobs to run on the server
1. Sync up stock list(daily)
35 18 * * 1,2,3,4,5 /opt/OmniTrader/scripts/sync_stock_list.sh