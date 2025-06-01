import pyautogui
import time
from PIL import ImageGrab

# The yellow confirmation color (R, G, B)
TARGET_YELLOW = (232, 213, 74)  
# How close colors need to be (higher = more lenient)
COLOR_TOLERANCE = 30  

def color_match(c1, c2, tolerance):
    """Check if two colors match within the given tolerance"""
    # Ensure we're comparing RGB values only (removing alpha if present)
    c1 = c1[:3] if len(c1) > 3 else c1
    c2 = c2[:3] if len(c2) > 3 else c2
    
    return all(abs(a - b) <= tolerance for a, b in zip(c1, c2))

def main():
    """Simple clicker that detects yellow under cursor, clicks once, and exits"""
    print("Marvel Rivals Auto Confirm - Running!")
    print("Place your cursor over the yellow confirm button")
    print("When the yellow button appears, it will be clicked automatically")
    print("Press Ctrl+C to quit\n")
    
    # Set up safety settings
    pyautogui.PAUSE = 0.1
    pyautogui.FAILSAFE = True  # Move mouse to corner to abort
    
    try:
        while True:
            # Get cursor position
            x, y = pyautogui.position()
            
            # Simple waiting message
            print("Waiting for yellow button to appear under cursor...", end='\r', flush=True)
            
            # Get pixel color under cursor
            pixel = ImageGrab.grab().load()[x, y]
            
            # Check if color matches our target yellow
            if color_match(pixel, TARGET_YELLOW, COLOR_TOLERANCE):
                print(f"\nYellow detected at ({x},{y}) - Clicking!")
                pyautogui.click()
                print("Click successful! Exiting.")
                break
            
            # Small delay between checks
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\nStopped by user")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()