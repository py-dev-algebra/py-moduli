import datetime as dt
import locale

danasnji_datum = dt.date.today()
print(f'\nDanasnji datum je: {danasnji_datum}')

sadasnji_ternutak = dt.datetime.now()
print(f'\nSadasnji trenutak je: {sadasnji_ternutak}')

#region
# dan_u_tjednu = dt.date.weekday(danasnji_datum)
# print(f'\nDanas je {dan_u_tjednu + 1}. dan u tjednu.')
# 
# match dan_u_tjednu:
#     case 0:
#         print(f'\nDanas je PONEDJELJAK, {dan_u_tjednu + 1}. dan u tjednu.')
#     case 1:
#         print(f'\nDanas je UTORAK, {dan_u_tjednu + 1}. dan u tjednu.')
#     case 2:
#         print(f'\nDanas je SRIJEDA, {dan_u_tjednu + 1}. dan u tjednu.')
#     case 3:
#         print(f'\nDanas je CETVRTAK, {dan_u_tjednu + 1}. dan u tjednu.')
#     case 4:
#         print(f'\nDanas je PETAK, {dan_u_tjednu + 1}. dan u tjednu.')
#     case 5:
#         print(f'\nDanas je SUBOTA, {dan_u_tjednu + 1}. dan u tjednu.')
#     case 6:
#         print(f'\nDanas je NEDJELJA, {dan_u_tjednu + 1}. dan u tjednu.')

# locale.setlocale(locale.LC_TIME, 'hr-HR')
# # locale.setlocale(locale.LC_TIME, 'sr-RS')
# # locale.setlocale(locale.LC_TIME, 'de-DE')
# # locale.setlocale(locale.LC_TIME, 'fr-FR')
# # locale.setlocale(locale.LC_TIME, 'ja-JP')
# # locale.setlocale(locale.LC_TIME, 'zh-CN')

# print(f'Danas je {danasnji_datum.strftime("%A").capitalize()}')
# # print(f'Danas je {danasnji_datum.strftime("%A")[ : 4]}')
# print(f'Danas je {danasnji_datum.strftime("%a").upper()}')

# locale.setlocale(locale.LC_TIME, '')
# print(f'Danas je {danasnji_datum.strftime("%A").capitalize()}')
# # print(f'Danas je {danasnji_datum.strftime("%A")[ : 4]}')
# print(f'Danas je {danasnji_datum.strftime("%a").upper()}')
#endregion

# print(f'Danas je {danasnji_datum.strftime("%Y")}')
# print(f'Danas je \'{danasnji_datum.strftime("%y")}')
# print(f"Danas je '{danasnji_datum.strftime("%y")}")

# print(f"\nDanas je {danasnji_datum.strftime("%j")}. dan u godini.\n")
# print(f"\nDanas je {danasnji_datum.strftime("%j")[1 : ]}. dan u godini.\n")

# print(f'Danas je {danasnji_datum.strftime("%d.%m.%Y. %H:%M:%S")}')
# print(f'Danas je {sadasnji_ternutak.strftime("%d.%m.%Y. %H:%M:%S")}')

# print(f'Danas je {sadasnji_ternutak.strftime("%B")}')
# print(f'Danas je {sadasnji_ternutak.strftime("%b")}')

# print(f'Danas je {sadasnji_ternutak.strftime("%c")}')

# locale.setlocale(locale.LC_TIME, 'hr_HR')
# print(f'Danas je {sadasnji_ternutak.strftime("%A").capitalize()}, {sadasnji_ternutak.strftime("%d")}. {sadasnji_ternutak.strftime("%B").capitalize()} {sadasnji_ternutak.strftime("%Y")}.')
# locale.setlocale(locale.LC_TIME, '')

# all_locales = locale.locale_alias.keys()
# print(all_locales)
