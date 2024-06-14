import datetime

class SuperDate(datetime.datetime):

    def get_season(self):
        try:
            if self.month == 12 or 1 or 2:
                return 'Winter'
            if self.month == 9 or 10 or 11:
                return 'Autumn'
            if self.month == 6 or 7 or 8:
                return 'Summer'
            if self.month == 3 or 4 or 5:
                return 'Spring'
        except Exception as exc:
            print(f'Что-то пошло не так: {exc}')

    def get_time_of_day(self):
        try:
            if self.hour in range(0,6):
                return 'Night'
            if self.hour in range(6,12):
                return 'Morning'
            if self.hour in range(12,18):
                return 'Day'
            if self.hour in range(18,24):
                return 'Day'
        except Exception as exc:
            print(f'Что-то пошло не так: {exc}')

a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())