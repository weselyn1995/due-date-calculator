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

    if not is_weekday(submit_datetime):
        raise ValueError('reports must be submitted on weekdays')
    if not is_working_hour(submit_datetime.hour):
        raise ValueError('reports must be submitted during working hours 9AM-5PM')
    if not turnaround_hours >= 0:
        raise ValueError('turnaround_hours must be 0 or more hours')

    due_date = submit_datetime
    remaining_hours = turnaround_hours

    # Process due date
    while remaining_hours > 0:
        # Advance time by 1 hour
        due_date += timedelta(hours = 1)
        
        # Only count working hours toward turnaround time
        if is_working_hour(due_date.hour) and is_weekday(due_date):
            remaining_hours -= 1
    
    return due_date