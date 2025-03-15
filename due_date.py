from datetime import datetime


def calculate_due_date(submit_datetime: datetime, turnaround_hours: int) -> datetime:

    # Validate inputs
    if not isinstance(submit_datetime, datetime):
        raise TypeError('submit_datetime should be of type datetime')
    if not isinstance(turnaround_hours, int):
        raise TypeError('turnaround_hours should be an integer')
    
    pass