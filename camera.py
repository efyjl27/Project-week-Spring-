from picamera import PiCamera
from time import sleep

# Initialize camera
camera = PiCamera()

#Set camera resolution
camera.resolution = (1280, 720)

try:
    # Start preview
    camera.start_preview()
    sleep(5) #adjust sleep duration as needed

    # Capture image
    camera.capture('/home/pi/Pictures/image.jpg') # Save image to specified path
    
finally:
    # Close camera preview and release resources
    camera.stop_preview()
    camera.close()
