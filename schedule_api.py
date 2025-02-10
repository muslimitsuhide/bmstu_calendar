import requests

def fetch_schedule(schedule_url):
    schedule_id = schedule_url.split("schedule/")[-1]
    API_URL = f"https://lks.bmstu.ru/lks-back/api/v1/schedules/groups/{schedule_id}/public"
    
    response = requests.get(API_URL)
    data = response.json()

    if "data" not in data or "schedule" not in data["data"]:
        raise ValueError("Ошибка: не найдено расписание в ответе API")
    
    return data["data"]["schedule"]
