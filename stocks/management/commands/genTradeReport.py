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
        parser.add_argument('--month', nargs='?', type=str, help='specify the month to analyze')
        parser.add_argument('--ticker', nargs='?', type=str, help='specify the stock to analyze')


    def handle(self, *args, **options):
        logger.info("Generating trade report...")
        date = datetime.date.today()
        if options['date']!=None:
            date = options['date']
            logger.info('Target date: {}'.format(date))

        service = TradeReportService()
        service.generateReport()


        #send_mail('OmniTrader - {} trade record processed'.format(processed), '', 'omni.trader.2015@gmail.com',['andrewmorro@gmail.com'], fail_silently=False)
        return