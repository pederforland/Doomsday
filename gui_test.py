from PyQt6.QtWidgets import QApplication, QWidget
import sys

# One QApplication object per application
# sys.argv allows command line arguments for app
app = QApplication(sys.argv)

# Create a Qt widget, our window
window = QWidget()
window.show() # Window is hidden by default

# Start the event loop
app.exec()

# Application won't reach here until you exit and event loop as stopped
