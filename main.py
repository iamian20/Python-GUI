import sys
from PyQt6 import uic
from PyQt6.QtWidgets import *
from backend.Register import benedicto_MainWindow
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = benedicto_MainWindow()
    main_window.show()
    sys.exit(app.exec())
    