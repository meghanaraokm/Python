from datetime import *

current_timezone = datetime.now().astimezone().tzinfo
current_tz_name = datetime.now(current_timezone).tzname()

print(current_timezone)
print(datetime.now())
print(datetime.now().astimezone())

print(datetime.now(current_timezone))
print(current_tz_name)

tz_name=datetime.now().astimezone().tzname()
print(tz_name)

