import argparse

from app.calendar import find_available_time

parser = argparse.ArgumentParser(description='Get available timeslots')
parser.add_argument('--duration', type=int, help='the length (duration in minutes) of the meeting')
parser.add_argument('--calendar_ids', type=str, nargs='*', help='the calendar ids')
parser.add_argument('--period', type=str, nargs=2, help='a period within to find availability (ISO8601 time interval, e.g --period 2007-03-01T13:00:00Z 2008-05-11T15:30:00Z )')

if __name__ == "__main__":
    args = parser.parse_args()
    find_available_time(args.calendar_ids,  args.duration, args.period)