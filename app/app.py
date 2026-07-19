import sys
from PySide6.QtWidgets import QApplication
from app.windows.login import LoginWindow
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    print("sys.argv___",sys.argv)
    # Создаём окно входа и показываем
    window = LoginWindow()
    window.show()

    # Запускаем цикл обработки событий
    sys.exit(app.exec())