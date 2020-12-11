from datetime import *
#from pytz import timezone


current_timezone = datetime.now().astimezone().tzinfo
current_tz_name = datetime.now(current_timezone).tzname()

print(current_timezone)
print(datetime.now())
#print(datetime.now().astimezone(timezone('US/Eastern')))

print(datetime.now(current_timezone))
print(current_tz_name)

tz_name=datetime.now().astimezone().tzname()

earliest="2020-12-10 22:10:00"
earliest_utc = datetime.strptime(earliest, '%Y-%m-%d %H:%M:%S') \
    .replace(tzinfo=current_timezone) \
    .astimezone(timezone.utc)

print(datetime.strptime(earliest, '%Y-%m-%d %H:%M:%S'))
print(datetime.strptime(earliest, '%Y-%m-%d %H:%M:%S').replace(tzinfo=current_timezone))
print(earliest_utc)

print(datetime.today())
print("datetimenow with tzinfo : {0}".format(datetime.now()))