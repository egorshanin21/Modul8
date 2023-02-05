from datetime import datetime, timedelta
import collections
import calendar

users = [{"name": "Boris", "birthday": datetime(1961, 4, 17)},
         {"name": "Max", "birthday": datetime(2014, 2, 9)},
         {"name": "Morgan", "birthday": datetime(1966, 2, 12)},
         {"name": "Jemisson", "birthday": datetime(1973, 2, 10)},
         {"name": "Jim", "birthday": datetime(1988, 2, 5)},
         {"name": "Denis", "birthday": datetime(1992, 1, 25)},
         {"name": "Boris", "birthday": datetime(1968, 2, 6)}]

def get_birthdays_per_week(users):
    now_day = datetime.now()
    result = {}
    for i in range(7):
        current_day = now_day + timedelta(days=i)
        for user in users:
            user_bt = user.get("birthday")
            user_name = user["name"]
            if (current_day.day, current_day.month) == (user_bt.day, user_bt.month):
                day_name = current_day.strftime('%A')
                if day_name == "Saturday":
                    new_d = current_day + timedelta(days=2)
                    if not new_d.date() > (now_day + timedelta(days=7)).date():
                        day_name = new_d.strftime('%A')
                    else:
                        continue
                if day_name == "Sunday":

                    new_d = current_day + timedelta(days=1)
                    if not new_d.date() > (now_day + timedelta(days=7)).date():
                        day_name = new_d.strftime('%A')
                    else:
                        continue
                if not result.get(day_name):
                    result[day_name] = [user_name]
                else:
                    result[day_name].append(user_name)
    for k, v in result.items():
        print(f"{k}: {', '.join(v)}")

get_birthdays_per_week(users)