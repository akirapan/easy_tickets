# easy tickets

## Overview

This script automates the process of securing tickets by simulating mouse movements and clicks at specific screen coordinates. The script is designed to run at a specific time, click on designated areas, and handle the page refreshes and confirmations required during the ticket purchasing process.

## Prerequisites

- **Python 3.x**
- **pyautogui** module: Install via pip if you haven't already:
  ```bash
  pip install pyautogui
  ```

## How It Works

1. **Positioning**: The script starts by allowing you to position your mouse over the target area. It captures your current mouse coordinates and uses them in subsequent actions.

2. **Timing**: The script checks the current time and waits until a specified time (e.g., 12:00 or 16:00) before initiating the clicks.

3. **Click Automation**: 
   - It clicks on specific coordinates to select options or navigate through pages.
   - The script handles multiple clicks and ensures the page has been switched by double-clicking in some cases.
   - It also manages scrolling (if needed) and confirms actions at regular intervals.

4. **Looping**: Repeats the process for a specified number of iterations to maximize the chances of securing a ticket.

## Disclaimer

This script is intended for personal use only. Be aware of the terms and conditions of the ticketing service you are using. Automated scripts might violate those terms, so use it responsibly.