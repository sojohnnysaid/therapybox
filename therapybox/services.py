import datetime
import datedelta
from django.forms.widgets import DateInput

def get_min_calendar_date():
    today = datetime.date.today()

    # today = today + datedelta.datedelta(days=+2) # test with other days

    tuesday = 1 # days are numbered Monday=0 Sunday=6
    min = today + datetime.timedelta(days=(tuesday - today.weekday() + 7 ) %7 )

    if today.weekday() == tuesday:
        # add another week of lead time
        min = today + datetime.timedelta(days=(tuesday - today.weekday() + 7 ) %7 + 7)

    return min


def get_max_calendar_date():
    return datetime.date.today() + datedelta.datedelta(months=2)


def get_custom_date_input():
    return DateInput(attrs={'type': 'date', 'min': get_min_calendar_date(), 'max': get_max_calendar_date(), 'step': '7'})