import time
from MusicController import MusicController
from LightStrip import LightStrip

time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

# Initialize MusicController
music_controller = MusicController()

# Initialize LightStrip
mylightstrip = LightStrip("My light strip", 2, 16)

# Function to run both MusicController and LightStrip
def run_combined():
    music_controller.run()  
    while True:
        mylightstrip.on()
        time.sleep(1)
        mylightstrip.off()
        time.sleep(1)

# Run the combined function
run_combined()





