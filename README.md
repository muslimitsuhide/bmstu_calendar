# Расписание в формате iCalendar

Этот скрипт позволяет получить расписание занятий с сайта ЛКС МГТУ Н.Э.Баумана и сохранить его в формате `.ics` для удобного добавления в календарь.

## 📌 Как использовать

1. **Склонируйте репозиторий**:

   ```sh
   git clone https://github.com/muslimitsuhide/bmstu_calendar.git
   cd bmstu_calendar
   ```

2. **Создайте виртуальное окружение и активируйте его**:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # для macOS/Linux
   venv\Scripts\activate  # для Windows
   ```

3. **Установите зависимости**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Запустите скрипт**:

   ```sh
   python main.py
   ```

5. **Вставьте ссылку на рассписание своей группы с сайта**: https://lks.bmstu.ru/schedule/

6. **На этом все:) Скрипт создаст файл schedule.ics, который можно импортировать в Google Календарь, Apple Calendar и т.д.**
