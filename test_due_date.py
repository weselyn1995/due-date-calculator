import pytest
from datetime import datetime
from due_date import calculate_due_date

EXAMPLE_REPORT_DATETIME = datetime(2024, 3, 11, 14, 12)
EXAMPLE_TURNAROUND_HOURS = 16

def test_fuction_exists():
    calculate_due_date(EXAMPLE_REPORT_DATETIME, EXAMPLE_TURNAROUND_HOURS)

def test_wrong_input_type_submit_datetime():
    with pytest.raises(TypeError):
        calculate_due_date(20240311, EXAMPLE_TURNAROUND_HOURS)

def test_wrong_input_type_turnaround_hours():
    with pytest.raises(TypeError):
        calculate_due_date(EXAMPLE_REPORT_DATETIME, 'sixteen')

def test_wrong_input_value_submit_datetime_weekdays():
    with pytest.raises(ValueError):
        calculate_due_date(datetime(2024, 3, 9, 14, 12), EXAMPLE_TURNAROUND_HOURS)

def test_wrong_input_value_submit_datetime_working_hours():
    with pytest.raises(ValueError):
        calculate_due_date(datetime(2024, 3, 11, 0, 0), EXAMPLE_TURNAROUND_HOURS)

def test_wrong_input_value_turnaround_negative():
    with pytest.raises(ValueError):
        calculate_due_date(EXAMPLE_REPORT_DATETIME, -1)

def test_0_hour_turnaround():
    assert EXAMPLE_REPORT_DATETIME == calculate_due_date(EXAMPLE_REPORT_DATETIME, 0)

def test_1_hour_turnaround():
    assert datetime(2024, 3, 11, 15, 12) == calculate_due_date(EXAMPLE_REPORT_DATETIME, 1)

def test_1_day_turnaround():
    assert datetime(2024, 3, 12, 14, 12) == calculate_due_date(EXAMPLE_REPORT_DATETIME, 8)