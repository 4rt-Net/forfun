import pyautogui
import time

time.sleep(1)

# Set a general pause time (adjust as needed)
pyautogui.PAUSE = 0.5

def find_and_click_icon(icon_path, timeout=10):
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            # Locate the icon on the screen
            location = pyautogui.locateOnScreen(icon_path, confidence=0.9)
            
            if location is not None:
                # Center of the icon
                center_x, center_y = pyautogui.center(location)
                
                # Move the mouse to the center of the icon (with adjusted duration) and click
                pyautogui.moveTo(center_x, center_y, duration=0.5)  # Adjust the duration
                pyautogui.click()
                
                return True  # Icon found and clicked successfully
        except Exception as e:
            print(f"Error: {e}")
    
    return False  # Icon not found within the specified timeout

# Paths to your PNG icon files
icon_paths = ["template_1.png", "template_2.png", "template_3.png"]

while True:
    # Loop through each icon and click
    for icon_path in icon_paths:
        if find_and_click_icon(icon_path):
            print(f"Clicked on {icon_path}")
        else:
            print(f"Unable to find {icon_path}")

    # Pause for 5 seconds after clicking the third logo
    print("Pausing for 5 seconds...")
    time.sleep(5)
