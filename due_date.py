from datetime import datetime, timedelta

# Define working hours
WORKING_HOURS_START = 9 # 9AM
WORKING_HOURS_END = 17 # 5PM

def is_working_hour(hour):
    return WORKING_HOURS_START <= hour < WORKING_HOURS_END

def is_weekday(date):
    return date.weekday() < 5 # 1-4 are weekdays, 5-6 are Saturday and Sunday

def calculate_due_date(submit_datetime: datetime, turnaround_hours: int) -> datetime:
    """
    Args:
        - submit_datetime (datetime): The date and time when the issue was submitted
        - turnaround_hours (int): The number of working hours needed to resolve the issue

    Input requirements:
        - Working hours are from 9 AM to 5 PM, Monday to Friday
        - Turnaround time is positive and measured in whole hours
    """

    # Validate inputs
    if not isinstance(submit_datetime, datetime):
        raise TypeError('submit_datetime must be of type datetime')
    if not isinstance(turnaround_hours, int):
        raise TypeError('turnaround_hours must be an integer')

    if not submit_datetime.weekday() < 5: # 1-4 are weekdays, 5-6 are Saturday and Sunday
        raise ValueError('reports must be submitted on weekdays')
    if not WORKING_HOURS_START <= submit_datetime.hour < WORKING_HOURS_END:
        raise ValueError('reports must be submitted during working hours 9AM-5PM')
    if not turnaround_hours >= 0:
        raise ValueError('turnaround_hours must be 0 or more hours')

    # Process turnaround time in working hours
    while turnaround_hours > 0:
        submit_datetime += timedelta(hours = 1)
        if is_working_hour(submit_datetime.hour) and is_weekday(submit_datetime):
            turnaround_hours -= 1

    return submit_datetime