from ics import Calendar, Event
import datetime
import uuid

WEEKDAYS = {1: "MO", 2: "TU", 3: "WE", 4: "TH", 5: "FR", 6: "SA", 7: "SU"}

def generate_ics(schedule, start_date):
    calendar = Calendar()
    event_ids = {}
    
    for lesson in schedule:
        day = lesson["day"]
        start_time = lesson["startTime"]
        end_time = lesson["endTime"]
        week_type = lesson["week"]
        subject = lesson["discipline"]["fullName"]
        audience = lesson["audiences"][0]["name"] if lesson["audiences"] else "Не указана"
        teachers = ", ".join([f"{t['lastName']} {t['firstName']} {t['middleName']}" for t in lesson["teachers"]]) or "Не указан"

        event_key = f"{subject}-{start_time}-{end_time}-{day}-{week_type}"
        if event_key not in event_ids:
            event_ids[event_key] = str(uuid.uuid4())

        if week_type == "ch" or week_type == "zn":
            rrule = f"FREQ=WEEKLY;INTERVAL=2;BYDAY={WEEKDAYS[day]}"
        elif week_type == "all":
            rrule = f"FREQ=WEEKLY;INTERVAL=1;BYDAY={WEEKDAYS[day]}"
        else:
            continue
        
        event = Event()
        event.name = subject
        event.begin = datetime.datetime.combine(start_date, datetime.datetime.strptime(start_time, "%H:%M").time()).replace(tzinfo=datetime.timezone(datetime.timedelta(hours=3)))
        event.end = datetime.datetime.combine(start_date, datetime.datetime.strptime(end_time, "%H:%M").time()).replace(tzinfo=datetime.timezone(datetime.timedelta(hours=3)))
        event.location = f"Аудитория: {audience}"
        event.description = f"Преподаватель: {teachers}"
        event.rrule = rrule
        event.uid = event_ids[event_key]
        
        calendar.events.add(event)

    return calendar
