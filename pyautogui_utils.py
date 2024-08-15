# -*- coding: utf-8 -*-
# creation date: 2024/8/7

import time
import pyautogui


def get_position(delay=3):
    print(f"Move ot the desired position within {delay} seconds...")
    time.sleep(delay)  # Wait for delay seconds to give you time to move the mouse
    x, y = pyautogui.position()  # Get the current mouse coordinates
    print(f"Current mouse coordinates: ({x}, {y})")


if __name__ == '__main__':
    get_position()