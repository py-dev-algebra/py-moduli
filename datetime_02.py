from datetime import datetime as dt
from datetime import timedelta


sadasnji_trenutak = dt.now()
print('Sadasnji ternutak', sadasnji_trenutak.strftime('%A, %d.%m.%Y. %H:%M'))

# 01.02.2024.
datum_termina = dt(year=2024, month=2, day=1, hour=20, minute=45)
print('Datum termina', datum_termina.strftime('%A, %d.%m.%Y. %H:%M'))
# razlika = datum_termina - sadasnji_trenutak
# print(razlika)

# Unos datuma u ovom obliku: '01.02.2024. 20:45'
# datum_termina_str = input('Upisite datum termina (dan.mjesec.godina. sat:minuta): ')
# novi_datum_termina = dt.strptime(datum_termina_str, '%d.%m.%Y. %H:%M')
# # print(novi_datum_termina)
# print('Novi datum termina', novi_datum_termina.strftime('%A, %d.%m.%Y. %H:%M'))

termina_za_15_dana = sadasnji_trenutak + timedelta(days=15, hours=10)
print('Termin za 15 dana', termina_za_15_dana.strftime('%A, %d.%m.%Y. %H:%M'))
termina_za_2_tjedna = sadasnji_trenutak + timedelta(weeks=2)
print('Termin za 2 tjedna', termina_za_2_tjedna.strftime('%A, %d.%m.%Y. %H:%M'))
