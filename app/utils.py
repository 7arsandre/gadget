import json
from datetime import datetime


calendar_owner_mapping = {
    '48644c7a-975e-11e5-a090-c8e0eb18c1e9': 'Joanna Hef',
    '48cadf26-975e-11e5-b9c2-c8e0eb18c1e9': 'Danny Boy',
    '452dccfc-975e-11e5-bfa5-c8e0eb18c1e9': 'Emma Win'
}

def format_time(timestamp):
    """
    Parses ISO8601 into datetime format

    Parameters:
    timestamp (string): ISO8601

    Returns:
    datetime.datetime: parsed timestamp
    """

    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S')

def get_calendar(calendar_id):
    """
    Deserialize to a Python object

    Parameters:
    calendar_id (string): the id of ones calendar

    Returns:
    dict: calendar object
    """

    calendar_name = calendar_owner_mapping[calendar_id]

    with open(f'data/{calendar_name}.json') as f:
        return json.load(f)

def get_calendar_owner(calendar_id):
    """
    Returns name of calendar owner

    Parameters:
    calendar_id (string): the id of ones calendar

    Returns:
    string: name of calendar owner
    """

    return calendar_owner_mapping[calendar_id]

def print_timeslots(calendar_owner, available_timeslots, duration):
    """
    Print the available timeslots


    Parameters:
    calendar_owner (string): name of calendar owner
    available_timeslots (dict): object containing available timeslots
    duration (int): desired duration of timeslot
    """

    print('--------------------------------------------------------------------')
    print(f'The following {duration} minutes session is available with {calendar_owner}')
    print()
    for timeslot in available_timeslots:
        print('- ', timeslot.get('start'))
    print('--------------------------------------------------------------------')