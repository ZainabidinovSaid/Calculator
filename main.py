# main.py
import sys
from PyQt6.QtWidgets import QApplication
from gui import CalculatorWindow  # Import the GUI class from gui.py

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application instance
    window = CalculatorWindow()   # Create the main window
    window.show()                 # Show the calculator window
    sys.exit(app.exec())           # Start the event loop
