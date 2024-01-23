import datetime as dt
# import dateutil.tz as du_tz
from dateutil import tz

sadasnji_trenutak = dt.datetime.now()
# du.tz.gettz('Europe/Zagreb')
tz_tokyo = tz.gettz('Asia/Tokyo')
tz_ny = tz.gettz('America/New_York')
tz_la = tz.gettz('America/Los_Angeles')
tz_london = tz.gettz('Europe/London')

sadasnji_trenutak_tokyo = sadasnji_trenutak.astimezone(tz_tokyo)
sadasnji_trenutak_ny = sadasnji_trenutak.astimezone(tz_ny)
sadasnji_trenutak_la = sadasnji_trenutak.astimezone(tz.gettz('America/Los_Angeles'))
sadasnji_trenutak_london = sadasnji_trenutak.astimezone(tz_london)
print('Tokyo', sadasnji_trenutak_tokyo.strftime('%A, %d.%m.%Y. %H:%M'))
print('New York', sadasnji_trenutak_ny.strftime('%A, %d.%m.%Y. %H:%M'))
print('Los Angeles', sadasnji_trenutak_la.strftime('%A, %d.%m.%Y. %H:%M'))
print('London', sadasnji_trenutak_london.strftime('%A, %d.%m.%Y. %H:%M'))
