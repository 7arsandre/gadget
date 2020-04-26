from datetime import timedelta

from app.utils import get_calendar, format_time,get_calendar_owner, print_timeslots

def available_appointment(appointments, timeslot_start, timeslot_end):
    """
    Checks if appointments for queried timeslot is taken or not

    Parameters:
    appointments (dict): object containing appointments
    timeslot_start (datetime.datetime): start date- and time of timeslotquery
    timeslot_end (datetime.datetime): end date- and time of timeslotquery

    Returns:
    boolean: appointment for queried timeslot taken or not
    """
    for appointment in appointments:
                appointment_start = format_time(appointment.get('start'))
                appointment_end = format_time(appointment.get('end'))
                if(appointment_start >= timeslot_start and appointment_end <= timeslot_end):
                    return False
    return True


def check_timeslots(timeslots, appointments, duration, period_to_search):
    """
    Checks if there exists available timeslots within the queried and desired period

    Parameters:
    timeslots (dict): object containing timeslots
    appointments (dict): object containing appointments
    duration (int): duration of queried appointment
    period_to_search (array): end date- and time of timeslotquery

    Returns:
    array: available timeslots for appointments
    """
    available_timeslots = []

    start_search = format_time(period_to_search[0])
    end_search = format_time(period_to_search[1])

    for timeslot in timeslots:
        timeslot_start = format_time(timeslot.get('start'))
        timeslot_end = format_time(timeslot.get('end'))
        timeslot_duration = timeslot_end - timeslot_start

        query_duration = timedelta(minutes=duration)

        if(query_duration != timeslot_duration):
            continue

        if(end_search > timeslot_start and end_search <= timeslot_end):
            # first part of timeslot matches
            if(available_appointment(appointments, timeslot_start, timeslot_end)):
                available_timeslots.append(timeslot)

        elif(start_search < timeslot_start and end_search >= timeslot_end):
            # 100% timeslot match
            if(available_appointment(appointments, timeslot_start, timeslot_end)):
                available_timeslots.append(timeslot)

        elif(start_search > timeslot_start and start_search < timeslot_end):
            # last part of timeslot matches
            if(available_appointment(appointments, timeslot_start, timeslot_end)):
                available_timeslots.append(timeslot)

    return available_timeslots


def find_available_time(calendar_ids, duration, period_to_search):
    """
    Goes through the the desired calendars to check if there's some available timeslots to book.
    Prints the result

    Parameters:
    calendar_ids (array): array containing calendar_ids
    duration (int): duration of queried appointment
    period_to_search (array): end date- and time of timeslotquery
    """
    for calendar_id in calendar_ids:
        calendar_owner = get_calendar_owner(calendar_id)

        calendar = get_calendar(calendar_id)
        available_timeslots = check_timeslots(calendar.get('timeslots'), calendar.get('appointments'), duration, period_to_search)

        if(len(available_timeslots) > 0 ):
            print_timeslots(calendar_owner, available_timeslots, duration)
        else:
            print(f'Found zero available timeslots with a duration of {duration} with {calendar_owner}')