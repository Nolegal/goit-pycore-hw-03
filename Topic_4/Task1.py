from datetime import datetime


def get_days_from_today(date):
     #Обробка помилки
   try:
      #Формування об'єкту date_object
     date_object = datetime.strptime(date,"%Y-%m-%d")
     #Формування сьогоднішньої дати
     now = datetime.today()
     #Віднімання від сьогодні заданої дати
     result=now-date_object
      #Повернення результату в днях
     return result.days
     #Обробка помилки
   except ValueError:
        return f"{date} Date is not correct"

print(get_days_from_today("2033-33-33"))