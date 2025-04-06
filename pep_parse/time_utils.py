import datetime as dt

TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


def get_formatted_time():
    now = dt.datetime.now()
    return now.strftime(TIME_FORMAT)
