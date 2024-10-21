import sys
import time
import random
import os
from datetime import datetime
import pytz  # Ensure you have pytz installed for timezone handling

# Try to import cfonts, and install if not already installed
try:
    from cfonts import render
except:
    os.system('pip install python-cfonts')
    from cfonts import render

# ANSI escape sequences for colors (Yellow and Magenta excluded)
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

# FPS warning system
fps_warning_threshold = 200
fps_round_count = 0
server_connected = False

# Clear screen function
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Correct key for verification
CORRECT_KEY = "@GODMOD57"

result_history = []

def show_welcome_message():
    # Display the welcome message using cfonts
    output = render('GODMOD', colors=['cyan', 'yellow'], align='center')
    print(output)

def verify_key():
    while True:
        key = input(f"{BRIGHT_CYAN}Please enter the key to continue: {RESET}")
        if key == CORRECT_KEY:
            print(f"{BRIGHT_GREEN}Key verified! You can now proceed.{RESET}")
            break
        else:
            print(f"{BRIGHT_RED}Invalid key! Please try again.{RESET}")

def select_server():
    global fps_round_count, server_connected
    fps_round_count = 0  # Reset the round count on server selection
    server_connected = True
    print(f"{BRIGHT_CYAN}Available Servers:")
    print(f"{BRIGHT_WHITE}1. Server 1")
    print(f"{BRIGHT_WHITE}2. Server 2")
    print(f"{BRIGHT_WHITE}3. Server 3")

    server_choice = input(f"{BRIGHT_CYAN}Please select a server (1/2/3): {RESET}")
    if server_choice in ['1', '2', '3']:
        print(f"{BRIGHT_GREEN}Server {server_choice} connected successfully!{RESET}")
        simulate_fps(server_choice)
    else:
        print(f"{BRIGHT_RED}Invalid server choice!{RESET}")
        select_server()

def simulate_fps(server_choice):
    global fps_round_count, server_connected
    while True:
        fps = random.randint(50, 150)  # FPS fluctuates between 50 and 150
        fps_round_count += 1

        # Dynamically show FPS after server selection
        print(f"{BRIGHT_WHITE}Connected to Server {server_choice} | FPS: {fps}{RESET}")
        time.sleep(1)  # Wait for 1 second before updating the FPS

        # After 15-20 rounds, FPS will exceed 200 and trigger a warning
        if fps_round_count >= random.randint(15, 20):
            fps = random.randint(200, 250)  # Fake FPS goes above 200
            print(f"{BRIGHT_RED}WARNING: FPS: {fps} | Server traffic is high!{RESET}")
            print(f"{BRIGHT_RED}Please don't use this code right now due to high server traffic.{RESET}")
            disconnect_server()  # Prompt for disconnection after warning
            break  # Exit the FPS loop after warning

def disconnect_server():
    global server_connected
    server_connected = False
    print(f"{BRIGHT_CYAN}Server disconnected due to high traffic.{RESET}")
    print(f"{BRIGHT_CYAN}Do you want to select a new server or exit?{RESET}")
    
    choice = input(f"{BRIGHT_CYAN}Enter 1 to select a new server or 2 to exit and see result history: {RESET}")
    
    if choice == '1':
        select_server()  # Restart server selection
    elif choice == '2':
        exit_program()  # End program and show result history
    else:
        print(f"{BRIGHT_RED}Invalid choice. Please try again.{RESET}")
        disconnect_server()  # Retry the disconnection prompt

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
    period_number = int(input(f"{BRIGHT_CYAN}Please enter the last period number: {RESET}"))
    last_result = int(input(f"{BRIGHT_CYAN}Please enter the last result number: {RESET}"))
    second_result = int(input(f"{BRIGHT_CYAN}Enter the 2nd result number: {RESET}"))

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
    print(f"{BRIGHT_CYAN}Thank you for using the program! Goodbye!{RESET}")
    sys.exit()

def update_results():
    result_input = input(f"{BRIGHT_CYAN}Enter 'W' for Win, 'L' for Loss, 'S' for Skip or 'E' to Exit: {RESET}").strip().upper()
    
    if result_input == 'E':
        exit_program()
    elif result_input not in ['W', 'L', 'S']:
        print(f"{BRIGHT_RED}Invalid input. Please enter 'W', 'L', 'S', or 'E'.{RESET}")

def main_loop():
    # Show welcome message using cfonts
    show_welcome_message()

    # Start key verification and other processes
    verify_key()
    select_server()

    while True:
        calculate_and_hide()
        update_results()

if __name__ == "__main__":
    main_loop()