# coding: utf-8


"""
Example configuration for statistics retrieval tasks:

from tasks import twitter
from tasks import foursq

tasks = [
    (twitter.followers_count, ('*','10')),
    (foursq.checkins, ('*/2'))
]

~~~~

A single task looks like:

    (foursq.checkins, ('*/2', '30'))
     -------^-------   -----^-----
       task name        intervals

    task name:  in tasks/ directory you will find .py files which have tasks.
                In this case, tasks/foursq.py has checkins method

    intervals:  these are in (hour, minute, second) format, tells program to
                when to execute these tasks.

                ('*', '30', '00')
                  |     |     |
                  |     |     +---- second (optional)
                  |     +---------- minute (optional)
                  +---------------- hour

                Examples: ('*',)            every hour
                          ('*/2',)          every 2 hours (e.g. 10:00, 12:00)
                          ('22', '30')      everyday at 22:30 (24-hour format)
                          ('*', '*/30')     every 30 mins (e.g. 10:00, 10:30)
                          ('0', '0')        every midnight
                          ('*', '*', '*/5') every 5 seconds

                NOTE: If you are going to use only hour part, do not forget
                comma at the end, e.g: ('*',)
"""

tasks = [
]

# Sample configuration:
#     You can just uncomment the part below.
#     Note that the last task does not have a comma at the end of the line.
#
# from tasks import twitter
# from tasks import kloutcom
# from tasks import foursq
# from tasks import fb
# from tasks import runkeeper
# from tasks import atelog
# from tasks import reporting
# from tasks import tmp102
# from tasks import lastfm
# from tasks import jawboneup

# tasks = [
#     (twitter.followers_count, ('*', '59')),
#     (twitter.tweets_count, ('*', '59')),
#     (foursq.checkins, ('*', '59')),
#     (fb.friends_count, ('*/2',)),
#     (runkeeper.activities_and_calories, ('*', '59')),
#     (runkeeper.sleeps, ('*',)),
#     (runkeeper.weight, ('*/2',)),
#     (kloutcom.score, ('*/2',)),
#     (tmp102.temperature, ('*', '*/20')),
#     (atelog.coffees, ('*',)),
#     (lastfm.tracks_listened, ('*', '59')),
#     (jawboneup.sleeps, ('*', '*/30')),
#     (jawboneup.steps, ('*', '*/30')),
#     (jawboneup.heart_rate, ('*', '*/30')),
#     (jawboneup.caffeine, ('*', '*/30')),
#     (reporting.generate_and_upload, ('*', '*/20')),
# ]
