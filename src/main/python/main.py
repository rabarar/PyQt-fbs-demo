from fbs_runtime.application_context import ApplicationContext
from PyQt5.QtWidgets import *

import sys

class AppContext(ApplicationContext):           # 1. Subclass ApplicationContext

    def on_button_clicked(self):
        self.alert = QMessageBox()
        self.alert.setText('You clicked the button!')
        self.alert.exec_()

    def run(self):                              # 2. Implement run()
        self.window = QMainWindow()
        self.window.setWindowTitle('Hello World!')
        self.window.resize(250, 150)
        
        self.button = QPushButton('Click')
        self.button.clicked.connect(self.on_button_clicked)
        self.button.show()

        self.window.show()
        return self.app.exec_()                 # 3. End run() with this line


if __name__ == '__main__':
    appctxt = AppContext()                      # 4. Instantiate the subclass
    exit_code = appctxt.run()                   # 5. Invoke run()
    sys.exit(exit_code)
