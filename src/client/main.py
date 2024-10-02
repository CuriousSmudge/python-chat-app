from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Only needed for access to command line arguments
import sys


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.button_checked = True

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.setChecked(self.button_checked)
        self.button.clicked.connect(self.the_button_was_toggled)

        self.setMinimumSize(QSize(100, 100))

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

        self.times_pressed = 0

    def the_button_was_toggled(self, checked):
        self.button_checked = checked
        self.times_pressed += 1
        self.button.setText(f"I have been pressed {self.times_pressed} time/s\n You wont be able to press me after the 3rd click")

        if self.times_pressed > 3:
            self.button.setText("Cant click me again!!")
            self.button.setEnabled(False)

        print("checked?", self.button_checked)

# This code from https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
