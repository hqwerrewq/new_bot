import json
from datetime import datetime

import pytz

# with open('schedule_template.json', 'w', encoding='utf-8') as f:
#     json.dump(event_list, f, ensure_ascii=False)

with open('schedule_template.json', 'r', encoding="utf8") as file:
    schedule_templates = json.load(file)


async def get_prime_activity(time):
    today_of_the_week = datetime.now(pytz.timezone('Europe/Moscow')).weekday()
    moscow_date = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%d.%m')
    schedule_text = []
    for day_of_the_week in schedule_templates['schedule']['day']:
        if day_of_the_week == str(today_of_the_week):
            if datetime.now().isocalendar().week % 2 != 0 and day_of_the_week == "5":
                odd_week = schedule_templates['schedule']['day'][day_of_the_week].get('odd_week_text')
                format_odd_week = odd_week.replace('date', moscow_date)
                schedule_text.append(format_odd_week)
            else:
                even_week = schedule_templates['schedule']['day'][day_of_the_week].get('text')
                format_even_week = even_week.replace('date', moscow_date)
                schedule_text.append(format_even_week)

            if time is not None:
                result = ''.join(schedule_text)
                format_results = ((result
                                   .replace('20:00', time)
                                   .replace('19:45', time)
                                   .replace('19:30', time)
                                   .replace('20:15', time)
                                   .replace('date', moscow_date)))
                return format_results
            else:
                result = ''.join(schedule_text)
                return result
