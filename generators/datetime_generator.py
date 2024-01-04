# -*- coding: utf-8 -*-

"""
#### Datetime range generator

##### Basic usage

for dt in datetime_range(datetime(2000, 1, 1), datetime(2000, 1, 10)):
    ...

##### Using step

for dt in datetime_range(datetime(2000, 1, 1), datetime(2000, 1, 10), step=timedelta(days=2)):
    ...

##### Reverse iteration

for dt in datetime_range(datetime(2000, 1, 10), datetime(2000, 1, 1), step=timedelta(days=-2)):
    ...
"""

# standard library
from datetime import datetime, timedelta


def datetime_range(start_datetime, end_datetime, step = None):
    """ Generator for a datetime range """

    # VALIDATIONS

    assert isinstance(start_datetime, datetime), 'start must be a datetime'
    assert isinstance(end_datetime, datetime), 'end must be a datetime'

    if isinstance(step, timedelta):
        step_seconds = step.total_seconds()

        assert step_seconds != 0, 'step must not be zero'

        if step_seconds > 0:
            assert start_datetime <= end_datetime, 'start must be less than end with positive step'

        elif step_seconds < 0:
            assert start_datetime >= end_datetime, 'start must be greater than end with negative step'

    _start_datetime = start_datetime
    _end_datetime = end_datetime
    _step = timedelta(seconds=1) if step is None else step

    current_datetime = _start_datetime

    if _step.total_seconds() > 0:
        while current_datetime <= _end_datetime:
            yield current_datetime
            current_datetime += _step
    else:
        while current_datetime >= _end_datetime:
            yield current_datetime
            current_datetime += _step
