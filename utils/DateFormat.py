import datetime
import time


@classmethod
class DateFormat():
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
