from gpiozero import DigitalInputDevice, Motor, PWMOutputDevice
from time import sleep

# Initialize digital input devies for reading DO signals
encoder_left_do = DigitalInputDevice(5) # GPIO pin connected to the digital output (DO) of the left encoder
encoder_right_do = DigitalInputDevice(6) # GPIO pin connected to the digital output (DO) of the right encoder

# Define motors
motor_left = Motor(forward=17, backward=18) # Motor pins for left motor
motor_right = Motor(forward=22, backward=23) # Motor pins for right motor

speed_controller_left = PWMOutputDevice(27) # GPIO pin for left motor speed controller
speed_controller_right = PWMOutputDevice(24) # GPIO pin for right motor speed controller

# Constants
ROTATION_ANGLE = 45 # Target rotation angle in degrees
ROTATION_COUNT = 100 # Number of rotation events to detect (adjust as needed)
MOTOR_SPEED = 0.5 # Adjust motor speed (0 to 1)


# Variables to track rotatoin events for each wheel
left_rotation_events = 0
right_rotation_events = 0

# Function to handle rotation events for the left wheel
def handle_left_rotation():
    global left_rotation_events
    left_rotation_events += 1
    print("Left rotation detected:", left_rotation_events)
    
# Function to handle rotation events for the right wheel
def handle_right_rotation():
    global right_rotation_events
    right_rotation_events += 1
    print("right rotation detected:", right_rotation_events)
    
# Set callback functions for rotation detection
encoder_left_do.when_activated = handle_left_rotation
encoder_right_do.when_activated = handle_right_rotation

# Function to turn left
def turn_left():
    motor_left.backward()
    motor_right.forward()
    speed_controller_left.value = MOTOR_SPEED
    speed_controller_right.value = MOTOR_SPEED
    
# Main loop to monitor rotation events
try:
    print("Turning left by 45 degrees...")
    turn_left()
    
    while left_rotation_events < ROTATION_COUNT or right_rotation_events < ROTATION_COUNT:
        sleep(0.1) # Check rotation events periodically
        
    printf("45-degree turn completed.")
    motor_left.stop()
    motor_right.stop()
    speed_controller_left.value = 0
    speed_contrller_right.value = 0
    
except KeyboardInterrupt:
    print("Program terminated by user")
    motor_left.stop()
    motor_right.stop()
    speed_controller_left.value = 0
    speed_contrller_right.value = 0
