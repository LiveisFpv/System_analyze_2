from PyQt6.QtWidgets import QApplication
import sys

from views.main_window import MainWindow
from models.matrix import Matrix
from controllers.main_controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()

    model = Matrix()

    # Создаем Controller и передаем в него View и Model
    controller = MainController(main_window, model)

    main_window.show()

    sys.exit(app.exec())
