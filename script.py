import pyautogui
import argparse
import time

POSITION = (755, 294)
SAVEPOSITION = (31, 355)

#Instructions:
'''
Has one positional argument, which should specify the number of entries.
Interrupt by placing mouse to upper left corner of screen.
'''
def main():
    # For interrupting
    pyautogui.PAUSE = 1
    pyautogui.FAILSAFE = True

    # Parse cl arguments
    parser=argparse.ArgumentParser()
    parser.add_argument('entries', type=int, help="Number of entries to delete")
    args = parser.parse_args()

    pyautogui.scroll(3000)
    pyautogui.click(POSITION)

    for i in range(args.entries):
        pyautogui.typewrite('\n', 0.1)
        pyautogui.hotkey('alt','8')
        time.sleep(0.1)

    print("Saving...")
    pyautogui.click(SAVEPOSITION)
    time.sleep(2)
    print("All done!")
    return 0

if __name__ =='__main__':
    main()
