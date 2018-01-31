"""
    The Great Autosaver
    by Jonathan Kalish
"""
import pyautogui
import time

DEFAULT_TIME_TO_WAIT = 60
YES_ANSWER = "Yes"
NO_ANSWER = "No"
MAIN = '__main__'


def save():
    """
        saves with ctrl s
    """
    pyautogui.hotkey('ctrl', 's')


def save_all():
    """
        saves all with ctrl shift s
    """
    pyautogui.hotkey('ctrl', 'shift', 's')


def main():
    """
        main method
        handles customization
    """
    # asks if you want to use save-all
    save_all_reply = pyautogui.confirm(text='Do you want to use save-all? (ctrl + shift + s)',
                                       title='Save All', buttons=[YES_ANSWER, NO_ANSWER])
    # gets the save interval
    time_to_wait = pyautogui.prompt(text='How long to wait between saves? (in seconds, default = 60)',
                                    title='Save Interval', default='')
    # if cancel was pressed
    if (time_to_wait is None) or (time_to_wait == ''):
        time_to_wait = DEFAULT_TIME_TO_WAIT

    # forever
    while True:
        # wait time given
        time.sleep(float(time_to_wait))
        print "Saving!"
        # checks if to save_all
        if save_all_reply == YES_ANSWER:
            save_all()
        else:
            save()

if __name__ == MAIN:
    main()
