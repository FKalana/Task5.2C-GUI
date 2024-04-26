import RPi.GPIO as GPIO  # Importing the GPIO library for Raspberry Pi
GPIO.setmode(GPIO.BOARD)  # Setting the GPIO pin numbering mode to BOARD
GPIO.setwarnings(False)  # Disable GPIO warnings
GPIO.setup(11, GPIO.OUT)  # Setting up pin 11 as an output
GPIO.setup(13, GPIO.OUT)  # Setting up pin 13 as an output
GPIO.setup(15, GPIO.OUT)  # Setting up pin 15 as an output

# Creating PWM objects for each LED
blue = GPIO.PWM(11, 100)  # Pin 11, frequency 100 Hz
red = GPIO.PWM(13, 100)   # Pin 13, frequency 100 Hz
yellow = GPIO.PWM(15, 100)  # Pin 15, frequency 100 Hz

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600, 600, 600, 600)  # Setting window geometry
        self.setWindowTitle("LED Toggle")  # Setting window title
        self.initUI()  # Initializing the UI
        
    def initUI(self):
        # Creating sliders for each LED
        self.b = QtWidgets.QSlider(self)
        self.b.setValue(0)  # Setting initial value of the slider
        self.bText = QtWidgets.QLabel(self)
        self.bText.setText("Blue")  # Setting text for the blue LED
        self.bText.move(210,30)  # Positioning the text label
        self.b.move(180,0)  # Positioning the slider
        self.b.valueChanged.connect(self.blue)  # Connecting slider value change to blue function
        
        self.r = QtWidgets.QSlider(self)
        self.r.setValue(0)  # Setting initial value of the slider
        self.rText = QtWidgets.QLabel(self)
        self.rText.setText("Red")  # Setting text for the red LED
        self.rText.move(340,30)  # Positioning the text label
        self.r.move(180,10)  # Positioning the slider
        self.r.valueChanged.connect(self.red)  # Connecting slider value change to red function
        
        self.y = QtWidgets.QSlider(self)
        self.y.setValue(0)  # Setting initial value of the slider
        self.yText = QtWidgets.QLabel(self)
        self.yText.setText("Yellow")  # Setting text for the yellow LED
        self.yText.move(300,0)  # Positioning the text label
        self.y.valueChanged.connect(self.yellow)  # Connecting slider value change to yellow function
        
        self.e = QtWidgets.QPushButton(self)
        self.e.setText("Quit")  # Setting text for the quit button
        
    def blue(self, value):
        blue.start(value)  # Starting PWM for the blue LED with the specified duty cycle
        
    def red(self, value):
        red.start(value)  # Starting PWM for the red LED with the specified duty cycle
        
    def yellow(self, value):
        yellow.start(value)  # Starting PWM for the yellow LED with the specified duty cycle

def window():
    app = QApplication(sys.argv)
    win = MyWindow()  # Creating instance of MyWindow class
    win.show()  # Displaying the window
    sys.exit(app.exec_())  # Exiting the application when window is closed

window()  # Calling the window function to run the application
