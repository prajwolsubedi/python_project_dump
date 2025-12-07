import time
import os
import sys
from datetime import datetime, timedelta
from playsound import playsound

now = datetime.now()
print(now)
def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def play_alarm():
    """Play alarm sound (beep)"""
    print("\n🔔 ALARM! ALARM! ALARM! 🔔\n")
    playsound("alarm.mp3")


def format_time(seconds):
    """Convert seconds to hours:minutes:seconds format"""
    # // is an integer division. It divides and ignores the decimal part
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def countdown(alarm_time):
    """Display countdown and return True if alarm should ring"""
    while True:
        now = datetime.now()
        remaining = (alarm_time - now).total_seconds()

        if remaining <= 0:
            return True

        clear_screen()
        print("=" * 40)
        print("         ALARM COUNTDOWN")
        print("=" * 40)
        print(f"\nCurrent time: {now.strftime('%I:%M:%S %p')}")
        print(f"Alarm set for: {alarm_time.strftime('%I:%M:%S %p')}")
        print(f"\nTime remaining: {format_time(remaining)}")
        print("\nPress Ctrl+C to cancel")
        print("=" * 40)
        time.sleep(1)


def main():
    print("=" * 40)
    print("      SIMPLE ALARM CLOCK")
    print("=" * 40)

    # Get alarm time from user
    try:
        now = datetime.now()
        print(f"\nCurrent time: {now.strftime('%I:%M:%S %p')}")

        hours = int(input("\nEnter alarm hour (0-23): "))
        minutes = int(input("Enter alarm minute (0-59): "))
        seconds = int(input("Enter alarm second (0-59): "))

        # Validate input
        if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
            print("Invalid time! Please enter valid hours, minutes, and seconds.")
            return

        # Create alarm time for today
        alarm_time = now.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)

        # If alarm time is in the past, set it for tomorrow
        if alarm_time <= now:
            alarm_time += timedelta(days=1)
            print(f"\nAlarm set for TOMORROW at {alarm_time.strftime('%I:%M:%S %p')}")
        else:
            print(f"\nAlarm set for TODAY at {alarm_time.strftime('%I:%M:%S %p')}")

        time.sleep(1)

        # Main alarm loop
        while True:
            try:
                # Countdown
                if countdown(alarm_time):
                    play_alarm()

                    # Ask for snooze
                    snooze = input("\nSnooze? (y/n): ").lower()
                    if snooze == 'y':
                        snooze_time = int(input("Snooze for how many minutes? "))
                        alarm_time = datetime.now() + timedelta(minutes=snooze_time)
                        print(f"\nSnoozing for {snooze_time} minute(s)...")
                        print(f"Alarm will ring at {alarm_time.strftime('%I:%M:%S %p')}")
                        time.sleep(1)
                    else:
                        print("\nAlarm dismissed!")
                        break

            except KeyboardInterrupt:
                print("\n\nAlarm cancelled!")
                sys.exit(0)

    except ValueError:
        print("\nInvalid input! Please enter numbers only.")
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled!")
        sys.exit(0)


if __name__ == "__main__":
    main()