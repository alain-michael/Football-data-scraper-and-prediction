import subprocess
import time

# Define the file paths for odds.py, main.py, and the combining script
odds_script = "odds.py"
main_script = "main.py"
combine_script = "test.py"
outcome_script = "Yvalue.py"

# Define the time interval in seconds (300 seconds = 5 minutes)
interval = 300

while True:
    # Get the current time
    current_time = time.localtime()
    current_minutes = current_time.tm_hour * 60 + current_time.tm_min
    current_seconds = current_time.tm_sec

    # Calculate the next multiple of 5 minutes
    next_interval = (current_minutes // 5 + 1) * 5
    # Calculate the delay in seconds
    delay_seconds = (next_interval - current_minutes) * 60 - current_seconds

    # Run odds.py immediately
    subprocess.run(["python", odds_script])

    # Wait for the specified delay
    time.sleep(delay_seconds)

    # Run main.py
    subprocess.run(["python", main_script])

    # Run combine_script
    subprocess.run(["python", combine_script])

    # Run outcome_script
    subprocess.run(["python", outcome_script])

    # Sleep for another interval before repeating the process
    time.sleep(interval)
