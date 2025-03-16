# Due Date Calculator - Emarsys Homework

A Python utility for calculating resolution due dates for issue tracking systems, respecting business hours.

## Purpose

This calculator computes when an issue will be resolved based on:
- When it was submitted
- How many working hours are needed to resolve it

The calculator only counts standard business hours (9 AM - 5 PM, Monday - Friday) toward resolution time and automatically skips evenings, nights, and weekends.

## Requirements

- Python 3.6 or higher
- Only uses Python standard library (datetime)

## Installation

No installation required beyond Python itself. Simply copy the module into your project:

```bash
# Clone the repository
git clone https://github.com/weselyn1995/due-date-calculator.git
```

## Usage

```bash
from datetime import datetime
from due_date_calculator import calculate_due_date

# Create a submit datetime (must be during working hours on a workday)
submit_time = datetime(2025, 3, 11, 14, 12)  # Tuesday at 2:12 PM

# Calculate when the issue will be resolved (16 working hours later)
due_date = calculate_due_date(submit_time, 16)

print(f"Issue will be resolved by: {due_date}")
# Output: Issue will be resolved by: 2025-03-13 14:12:00
```

## Testing

The repository includes a test suite in `test_due_date.py` using the pytest framework. These tests verify correct handling of various scenarios including same-day resolution, overnight calculations, weekend skipping, and input validation.

To run the tests:

```bash
# Install pytest
pip install pytest

# Run tests
pytest test_due_date.py
```
