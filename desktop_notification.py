import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="ALAERT!",
            message="Take a break, Have a KITKAT!",
            timeout=10
        )
        time.sleep(1)