# Gadget
>  🎶 dum du du du dum inspector Gadget

Inspects calendardata and returns available timeslots 🕵🏻‍♂️

You're able to choose among these calendar ids:
- 48644c7a-975e-11e5-a090-c8e0eb18c1e9
- 48cadf26-975e-11e5-b9c2-c8e0eb18c1e9
- 452dccfc-975e-11e5-bfa5-c8e0eb18c1e9

The first possible timeslot starts at _2019-04-23T08:00:00_ and the last ends at _2019-04-27T20:00:00_.
A timeslot is either of 15 or 30 minutes of length.


## Getting started

Make sure you have [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today) installed

```sh
$ pipenv shell
$ python -m app.main --duration <NUMBER> --calendar_ids <ID_1> <ID_2> ... <ID_N>  --period <START_TIME> <END_TIME>

# An example
$ python -m app.main --duration 30 --calendar_ids 452dccfc-975e-11e5-bfa5-c8e0eb18c1e9 48cadf26-975e-11e5-b9c2-c8e0eb18c1e9 48644c7a-975e-11e5-a090-c8e0eb18c1e9 --period 2019-04-23T12:15:00 2019-04-24T12:30:00
```