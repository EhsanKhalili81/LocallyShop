from . import Jalali
from django.utils import timezone
from datetime import timedelta

def Jalali_Converter(time):
    time=timezone.localtime(time) + timedelta(hours=1)
    time_str = "{},{},{}".format(time.year,time.month,time.day)
    time_tuple = Jalali.Gregorian(time_str).persian_tuple()
    output = "{}/{}/{} , ساعت {}:{}".format( time_tuple[0] , time_tuple[1] , time_tuple[2] , time.hour , time.minute, )
    return output