import datetime

TIME_FORMAT_LOG = "%Y-%m-%d/%H:%M:%S"
CURRENT_DATETIME = datetime.datetime.now().strftime(TIME_FORMAT_LOG)
print(CURRENT_DATETIME)
print(datetime.datetime.strptime(CURRENT_DATETIME, TIME_FORMAT_LOG))