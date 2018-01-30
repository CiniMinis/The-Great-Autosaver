"""
    The Great Autosaver
    by Jonathan Kalish
"""
from pyautogui import hotkey
import time

TIME_TO_WAIT = 30
YES_ANSWERS = ['YES', 'Y']


def save():
    """
        saves with ctrl s
    """
    hotkey('ctrl', 's')


def eclipse_save():
    """
        saves all in eclipse with ctrl shift s
    """
    hotkey('ctrl', 'shift', 's')


reply = raw_input("Are you using eclipse?")

while True:
    time.sleep(TIME_TO_WAIT)
    print "Saving!"
    if reply.upper() in YES_ANSWERS:
        eclipse_save()
    else:
        save()
