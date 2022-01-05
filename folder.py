import os
from datetime import date, timedelta


def allsundays(year):
    d = date(year, 1, 1)  # January 1st
    d += timedelta(days=8 - d.weekday())  # First Sunday
    while d.year == year:
        yield d
        d += timedelta(days=7)


folder_names = [
    '01. January',
    '02. February',
    '03. March',
    '04. April',
    '05. May',
    '06. June',
    '07. July',
    '08. August',
    '09. September',
    '10. October',
    '11. November',
    '12. December',
]


def create_folders():
    for folder in folder_names:
        os.mkdir(folder)


if __name__ == '__main__':
    create_folders()

    months = {count: month for (count, month) in enumerate(folder_names, start=1)}

    for d in allsundays(2021):
        print(d.strftime('%m-%d-%Y'))
        sub = d.strftime('%m-%d-%Y')
        folder_name = months.get(d.month)
        os.mkdir(os.path.join(folder_name, sub))
        print(d.month, folder_name)
