import time
import os
from datetime import datetime

# Define colors using ANSI escape codes
GREEN = "\033[92m"  # Green for success and connection steps
YELLOW = "\033[93m"  # Yellow for loading messages
RED = "\033[91m"  # Red for "big" or "small" result
WHITE = "\033[97m"  # White for headers
RESET = "\033[0m"  # Reset color to default

def display_server_connection():
    # Display "Connecting to server" with a smooth animation for 3 seconds in green
    print(f"{GREEN}Connecting to game server{RESET}", end="")

    # Simulate a processing animation for the connection
    for i in range(5):  # 5 iterations for processing effect
        dots = '.' * (i % 4)  # Cycle through 0 to 3 dots
        print(f"\r{GREEN}Connecting to game server{dots}{RESET}", end='', flush=True)
        time.sleep(1)

    # Simulate connection verification and loading steps
    print("\r" + " " * 40, end="\r")  # Clear the previous dots
    print(f"{GREEN}Verifying server data...{RESET}", end='', flush=True)
    time.sleep(2)  # Simulate some verification process

    print("\r" + " " * 40, end="\r")  # Clear the previous message
    print(f"{GREEN}Checking server connection...{RESET}", end='', flush=True)
    time.sleep(2)  # Simulate server connection checking

    # After the process, display "Server connected successfully" in green
    print(f"\n{GREEN}Server connected successfully!{RESET}")
    time.sleep(1.5)  # Pause to allow users to see the success message
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen to prepare for the next part

def display_period_and_timer():
    last_minute = None
    remaining_seconds = 59
    previous_period = None  # Track the previous period's result

    # Trend pattern: small, big, etc.
    pattern = ["small", "big", "big", "big", "small", "big", "small", "small", "big", "big", "small"]
    pattern_length = len(pattern)

    # List to keep track of period history
    period_history = []

    while True:
        now = datetime.utcnow()

        # Check if the minute has changed to update the period
        if now.minute != last_minute:
            last_minute = now.minute

            # Calculate total minutes since midnight
            total_minutes = now.hour * 60 + now.minute

            # Determine "big" or "small" for this minute based on the pattern
            current_pattern = pattern[total_minutes % pattern_length]

            # Format the period number for the 1-minute interval
            period_1m = now.strftime("%Y%m%d") + "1000" + str(10001 + total_minutes)

            # If there was a previous period, move it to history
            if previous_period is not None:
                period_history.insert(0, previous_period)
                # Ensure history does not exceed 20 entries
                if len(period_history) > 20:
                    period_history.pop()  # Remove the oldest entry

            # Set the current period as the previous period for the next cycle
            previous_period = f"{GREEN}{period_1m}{RESET} {RED}{current_pattern.upper()}{RESET}"

            # Clear the screen (works in most terminals)
            os.system('cls' if os.name == 'nt' else 'clear')

            # Print the current period with styled headings and alignment
            print("=" * 60)
            print(f"{WHITE}{' CURRENT PERIOD ':^60}{RESET}")
            print("=" * 60)
            print(f"  {GREEN}{period_1m}{RESET}")  # Current period in green
            print("=" * 60)

            # Display the result of the current period
            print(f"\n{WHITE}{' CURRENT PERIOD RESULT ':^60}{RESET}")
            print("=" * 60)
            print(f"  Result: {RED}{current_pattern.upper()}{RESET}")  # Display the result (big or small) in red
            print("=" * 60)

            # Add extra space before history for separation
            print("\n" * 3)  # Increased space before history section

            # Display the history of previous periods
            print(f"{WHITE}{' HISTORY ':^60}{RESET}")
            print("=" * 60)
            for period in period_history:
                print(f"  {GREEN}{period.split(' ')[0]}{RESET} {RED}{period.split(' ')[1]}{RESET}")  # History in red
            print("=" * 60)

            # Reset the remaining seconds to 59 at the start of a new minute
            remaining_seconds = 59

        # Format the countdown timer
        formatted_time = f"   {0:02}  :  {remaining_seconds:02}".replace("0", " ")

        # Display the countdown timer in green
        print(f"{GREEN}TIMER: {formatted_time}{RESET}", end='\r')

        # Decrease remaining seconds
        remaining_seconds -= 1

        # Reset the countdown at the end of the minute
        if remaining_seconds < 0:
            remaining_seconds = 59

        # Wait 1 second before updating again
        time.sleep(1)

# Run the server connection function
display_server_connection()

# Run the period and timer display function
display_period_and_timer()