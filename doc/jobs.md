# Setup cron
configure the right timezone on the box

# Jobs to run on the server
1. Sync up stock list(daily)
35 18 * * 1,2,3,4,5 /opt/OmniTrader/scripts/sync_stock_list.sh

2. TODO: Stock report via patterns job

3. TODO: tag updating job
POC:
scrapy shell http://stockpage.10jqka.com.cn/600340/
response.xpath('//dl[@class="company_details"]/dd')[1].xpath('@title').extract()
