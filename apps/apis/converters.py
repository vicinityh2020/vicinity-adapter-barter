import string
import random
from datetime import datetime


class Convert:
    """Class for converting different types of data."""
    @staticmethod
    def seconds_to_time(seconds):
        minute, sec = divmod(seconds, 60)
        hours, minute = divmod(minute, 60)
        hour_minutes = "%d:%02d" % (hours, minute)
        response = datetime.strptime(hour_minutes, '%H:%M').time()
        return response

    @staticmethod
    def time_to_seconds(time):
        return (time.hour * 3600) + (time.minute * 60) + (time.second * 1)

    @staticmethod
    def generate_unique_res():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))
