# -*- coding: utf-8 -*-
# creation date: 2024/8/7

import pyautogui
import time
from datetime import datetime


def get_time_now():
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    return current_time


# Wait a few seconds to switch to the target window
time.sleep(3)

# Starting time point
if get_time_now() > '120000':
    t = '160000'
else:
    t = '120000'

while True:
    if get_time_now() >= t:
        break

# Click on a specific area (x, y)
x_click = 636
y_click = 769

# Double-click to ensure page switch
pyautogui.click(x_click, y_click)
pyautogui.click(x_click, y_click)
# time.sleep(0.1)

# Scroll down by a certain amount
scroll_distance = -30  # Negative value means scrolling down, positive value means scrolling up
# pyautogui.scroll(scroll_distance)

claim_click_x = 855
claim_click_y = 405

confirm_click_x = 723
confirm_click_y = 503

for i in range(400):
    pyautogui.click(claim_click_x, claim_click_y)
    # pyautogui.scroll becomes ineffective after page refresh, and the refresh time is unknown, so temporarily disabled
    # if i < 40:
    #     pyautogui.scroll(scroll_distance)
    if i % 10 == 0:
        pyautogui.click(confirm_click_x, confirm_click_y)
