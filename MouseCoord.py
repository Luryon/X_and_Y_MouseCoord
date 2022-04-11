
import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        coordinates = "X: " + str(x).ljust(4) + " Y: " + str(y).ljust(4)
        print(coordinates, end="")
        print("\b" * len(coordinates), end="", flush=True)

except KeyboardInterrupt:
    print("End of program...")
