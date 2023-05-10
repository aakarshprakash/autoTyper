import os
import random
import string
import pyautogui
import time
import ctypes

# Wait for 5 seconds before starting the script
time.sleep(5)

# Load the Windows user32.dll library
user32 = ctypes.WinDLL('user32')

# Define the LockWorkStation function
LockWorkStation = user32.LockWorkStation

# Loop to generate random PHP functions and type them into Visual Studio
while True:
    
    # Generate a random function name
    function_name = ''.join(random.choices(string.ascii_lowercase, k=10))

    # Generate a random function body
    function_body = f"return {random.randint(0, 100)};"

    # Combine the function name and body into a PHP function
    php_function = f"public function {function_name}() {{ {function_body} }}"
    
    # Generate a random string of text
    text = php_function
    
    # Type the text into Visual Studio
    pyautogui.write(text, interval=0.1)  # Set interval to 0.1 seconds
    pyautogui.press('enter')

    # Wait for 1 second before typing again
    time.sleep(1)

    # Check for mouse movement
    current_pos = pyautogui.position()
    time.sleep(1)
    if pyautogui.position() != current_pos:
        # Lock the screen if there is mouse movement
        LockWorkStation()
        break