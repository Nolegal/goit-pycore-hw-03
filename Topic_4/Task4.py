from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
 
 
 
 
  for user in users:
   birthday=datetime.strptime(user["birthday"], "%Y.%m.%d").date()
   today = datetime.today().date()
   birthday_this_year=birthday.replace(year=today.year)
   user.update({"congratulation_date":birthday})
   if birthday_this_year<today:
    user["congratulation_date"]=birthday_this_year+timedelta(days=365)
   elif birthday.weekday()==5:
    user["congratulation_date"]=birthday_this_year+timedelta(days=2)
   elif birthday.weekday()==6:
    user["congratulation_date"]=birthday_this_year+timedelta(days=1)
   else:
    user["congratulation_date"]=birthday_this_year
    
  return users

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Andre Jack", "birthday": "2024.06.15"},
    {"name": "Fredro Starr", "birthday": "2024.06.16"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)


