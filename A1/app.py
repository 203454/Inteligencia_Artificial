from PySide2.QtWidgets import QApplication
from controllers.main_window import MainFormWindow

if __name__ == "__main__":
    app = QApplication()
    window = MainFormWindow()
    window.show()

    app.exec_()