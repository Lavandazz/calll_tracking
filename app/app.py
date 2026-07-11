import sys

from PySide6.QtWidgets import QApplication
from app.windows.login import LoginWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Создаём окно входа и показываем
    login_window = LoginWindow()
    login_window.show()

    # Запускаем цикл обработки событий
    sys.exit(app.exec())