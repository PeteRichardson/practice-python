#!/usr/bin/env python

''' ClockUtils.py - Utility functions related to clocks'''

DEGREES_PER_MINUTE = 360/60.0
DEGREES_PER_HOUR   = 360/12.0

def minute_angle(minute):
    return (DEGREES_PER_MINUTE * minute) % 360  # degrees = degrees per minute * minutes

def integer_hour_angle(hour):
    return (DEGREES_PER_HOUR * hour) % 360   # degrees = degrees per hour * hours

def hour_delta_caused_by_minute(minute):
    return (minute/60.0 * DEGREES_PER_HOUR) % DEGREES_PER_HOUR

def hour_angle(hour, minute):
    ''' angle of the integer hour + amount past the hour because of minutes'''
    return (integer_hour_angle(hour) + hour_delta_caused_by_minute(minute))
    

def hand_angle(hour, minute):    
    return abs(hour_angle(hour, minute) - minute_angle(minute))

