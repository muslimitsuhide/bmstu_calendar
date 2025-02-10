import datetime
from schedule_api import fetch_schedule
from event_generator import generate_ics

if __name__ == "__main__":
    schedule_url = input("Вставьте ссылку на свое расписание (вида: https://lks.bmstu.ru/schedule/XXX): ")
    
    try:
        schedule = fetch_schedule(schedule_url)
        start_date = datetime.date(2025, 2, 3)
        calendar = generate_ics(schedule, start_date)
        
        with open("schedule.ics", "w", encoding="utf-8") as f:
            f.writelines(calendar)

        print("Файл schedule.ics создан. Можете добавить его в свой календарь!")
    
    except Exception as e:
        print(f"{e}")
