import datetime

def add_gigasecond(past_date):
    """Return passed date plus 10^9 seconds."""
    gigasecond = datetime.timedelta(seconds=1e9)
    return past_date + gigasecond
