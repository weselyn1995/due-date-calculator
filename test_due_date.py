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