import time
from plyer import notification

def drink_water():
    """Sends a notification to remind the user to drink water."""
    
    notification.notify(
        title="Drink Water!",
        message="It's time to drink some water!",
        timeout=10,
    )

def main():
    """Starts the water reminder program."""
    interval = 60 * 60  # 1 hour
    while True:
        drink_water()
        time.sleep(interval)

if __name__ == "__main__":
    main()
