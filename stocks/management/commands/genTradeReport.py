from django.core.management.base import BaseCommand, CommandError
from stocks.models import *

import logging
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from stocks.services.TradeReportService import TradeReportService
import datetime


logger = logging.getLogger('stocks.management.genTradeReport')

class Command(BaseCommand):

    
    def add_arguments(self, parser):
        parser.add_argument('--date', nargs='?', type=str, help='specify the date to analyze')
        parser.add_argument('--startdate', nargs='?', type=str, help='specify the start date to analyze')
        parser.add_argument('--enddate', nargs='?', type=str, help='specify the end date to analyze')
        parser.add_argument('--month', nargs='?', type=str, help='specify the month to analyze')
        parser.add_argument('--ticker', nargs='?', type=str, help='specify the stock to analyze')


    def handle(self, *args, **options):
        logger.info("Generating trade report...")
        startdate = datetime.date.today()
        enddate = datetime.date.today()

        if options['date']!=None:
            startdate = options['date']
            enddate = options['date']
            logger.info('Target date: {}'.format(date))
        elif options['startdate']!=None and options['enddate']!=None:
            startdate = options['startdate']
            enddate = options['enddate']
            

        service = TradeReportService()
        service.setDate(startdate,enddate)
        service.generateReport()


        #send_mail('OmniTrader - {} trade record processed'.format(processed), '', 'omni.trader.2015@gmail.com',['andrewmorro@gmail.com'], fail_silently=False)
        return