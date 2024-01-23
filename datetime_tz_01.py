import datetime as dt
# import dateutil.tz as du_tz
from dateutil import tz

sadasnji_trenutak = dt.datetime.now()
# du.tz.gettz('Europe/Zagreb')
tz_tokyo = tz.gettz('Asia/Tokyo')

sadasnji_trenutak_tokyo = sadasnji_trenutak.astimezone(tz_tokyo)
print(sadasnji_trenutak_tokyo)
