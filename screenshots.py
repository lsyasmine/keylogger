import time
import os
import pyscreenshot as ImageGrab
import schedule
from datetime import datetime

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def take_screenshot():
    print("Taking screenshot...")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    timestamp_for_filename = timestamp.replace(":", "_").replace(" ", "_")
    image_name = f"screenshot-{timestamp_for_filename}"

    create_directory("./screenshots")  # Ensure the directory exists

    screenshot = ImageGrab.grab()

    filepathloc = f"./screenshots/{image_name}.png"

    screenshot.save(filepathloc)

    print("Screenshot taken...")

    return filepathloc

def main():
    s = 10
    for k in range(s):
        schedule.every(5).seconds.do(take_screenshot)
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == '__main__':
    main()



