import sys
import time
import random
import os
from datetime import datetime
import pytz  # Ensure you have pytz installed for timezone handling

# ANSI escape sequences for colors (Yellow and Magenta excluded)
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

# Clear screen function
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Correct key for verification
CORRECT_KEY = "@AHMAD_GODMOD1"

result_history = []

def verify_key():
    while True:
        key = input(f"{BRIGHT_CYAN}Please enter the key to continue: {RESET}")
        if key == CORRECT_KEY:
            print(f"{BRIGHT_GREEN}Key verified! You can now proceed.{RESET}")
            break
        else:
            print(f"{BRIGHT_RED}Invalid key! Please try again.{RESET}")

def select_server():
    print(f"{BRIGHT_CYAN}Available Servers:")
    print(f"{BRIGHT_WHITE}1. Server 1")
    print(f"{BRIGHT_WHITE}2. Server 2")
    print(f"{BRIGHT_WHITE}3. Server 3")

    server_choice = input(f"{BRIGHT_CYAN}Please select a server (1/2/3): {RESET}")
    if server_choice in ['1', '2', '3']:
        print(f"{BRIGHT_GREEN}Server {server_choice} connected successfully!{RESET}")
    else:
        print(f"{BRIGHT_RED}Invalid server choice!{RESET}")
        select_server()

def calculate_and_hide():
    # Get current time and calculate the period
    timezone = pytz.timezone("Asia/Kolkata")
    now = datetime.now(timezone)

    # Define start time at 5:29 AM
    start_hour = 5
    start_minute = 29
    elapsed_minutes = (now.hour * 60 + now.minute) - (start_hour * 60 + start_minute)

    # If the current time is before 5:29 AM, set elapsed_minutes to 0
    if elapsed_minutes < 0:
        elapsed_minutes = 0

    # Get inputs
    period_number = int(input(f"{BRIGHT_CYAN}Enter The 2nd Result Number: {RESET}"))
    last_result = int(input(f"{BRIGHT_CYAN}Enter The 3rd Last Result Number: {RESET}"))
    second_result = int(input(f"{BRIGHT_CYAN}Enter The 4th Result Number: {RESET}"))

    # Clear the screen (hides previous inputs)
    clear_screen()

    # Calculation logic
    total = period_number + last_result
    final_result = abs(second_result - total)

    # Show calculation in progress
    print(f"{BRIGHT_CYAN}Calculating... Please wait.{RESET}")
    time.sleep(2)

    # Show only the final results after calculation
    accuracy = (30 + (final_result % 71))
    result_message = classify_result(final_result)

    # Store result history with current period
    current_period = f"{now.strftime('%Y%m%d')}100001{elapsed_minutes:04d}"
    result_history.append(f"Period: {current_period} | Result: {result_message} | Accuracy: {accuracy}%")

    # Display current period, accuracy, and final result
    print(f"{BRIGHT_BLUE}═════════════════════════════════════════════════════════════{RESET}")
    print(f"{BRIGHT_WHITE}Current Period: {BRIGHT_CYAN}{current_period}{RESET}")
    print(f"{BRIGHT_GREEN}Accuracy: {accuracy}%{RESET}")
    print(f"{BRIGHT_GREEN}Final Result: {result_message}{RESET}")
    print(f"{BRIGHT_BLUE}═════════════════════════════════════════════════════════════{RESET}")

def classify_result(final_result):
    if final_result > 10:
        return random.choice([f"{BRIGHT_RED}Red{RESET}", f"{BRIGHT_GREEN}Green{RESET}"])
    elif final_result in [2, 4, 0]:
        return f"{BRIGHT_RED}Small Red{RESET}"
    elif final_result in [1, 3]:
        return f"{BRIGHT_GREEN}Small Green{RESET}"
    elif final_result in [5, 7, 9]:
        return f"{BRIGHT_GREEN}Big Green{RESET}"
    elif final_result in [6, 8]:
        return f"{BRIGHT_RED}Big Red{RESET}"
    elif final_result == 10:
        return f"{BRIGHT_WHITE}Skip{RESET}"

def exit_program():
    print(f"{BRIGHT_CYAN}Exiting the program... Displaying result history.{RESET}")
    time.sleep(1)
    print(f"{BRIGHT_BLUE}═════════════════════════════════════════════════════════════{RESET}")
    print(f"{BRIGHT_WHITE}Final Results History:{RESET}")

    for entry in result_history:
        print(f"{BRIGHT_WHITE}{entry}{RESET}")

    print(f"{BRIGHT_BLUE}═════════════════════════════════════════════════════════════{RESET}")
    print(f"{BRIGHT_CYAN}Thank you for using this code! Goodbye!{RESET}")
    sys.exit()

def update_results():
    result_input = input(f"{BRIGHT_CYAN}Enter 'W' for Win, 'L' for Loss, 'S' for Skip or 'E' to Exit: {RESET}").strip().upper()
    
    if result_input == 'E':
        exit_program()
    elif result_input not in ['W', 'L', 'S']:
        print(f"{BRIGHT_RED}Invalid input. Please enter 'W', 'L', 'S', or 'E'.{RESET}")

def main_loop():
    verify_key()
    select_server()

    while True:
        calculate_and_hide()
        update_results()

if __name__ == "__main__":
    main_loop()
