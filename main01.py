import time
from plyer import notification
import threading

def posturealert():
    while True:
        notification.notify(
            title="Posture alert",
            message="Sit with your back straight",
            timeout=2
        )
        time.sleep(20*60)  # posture alerts every 20 minutes

def hydrationalert():
    while True:
        notification.notify(
            title="Hydration alert",
            message="Please drink some water",
            timeout=2
        )
        time.sleep(30*60)  # hydration alerts every 30 minutes

def eyeexercises():
    while True:
        notification.notify(
            title="Eye exercise alert",
            message="Please do some eye movements",
            timeout=2
        )
        time.sleep(45*60)  # eye exercise alerts every 45 minutes

def prolongedusage():
    while True:
        notification.notify(
            title="Prolonged use alert",
            message="You've been using your device for 2 hours, please take a short break",
            timeout=2
        )
        time.sleep(2*60*60)  # prolonged use alerts every 2 hours

if __name__ == "__main__":
    # Create and start threads for each alert
    posture_thread = threading.Thread(target=posturealert)
    hydration_thread = threading.Thread(target=hydrationalert)
    eye_thread = threading.Thread(target=eyeexercises)
    prolonged_thread = threading.Thread(target=prolongedusage)

    posture_thread.start()
    hydration_thread.start()
    eye_thread.start()
    prolonged_thread.start()

    # Optional: Wait for threads to complete (they run indefinitely)
    # posture_thread.join()
    # hydration_thread.join()
    # eye_thread.join()
    # prolonged_thread.join()
