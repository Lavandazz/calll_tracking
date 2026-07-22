import sys
from PySide6.QtWidgets import QApplication
from app.windows.login import LoginWindow
from PySide6.QtWidgets import QApplication
from config.db.database import sync_sessionmaker


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Создаём окно входа и показываем, передаем сессию работы с базой данных в конструктор
    window = LoginWindow(session_maker=sync_sessionmaker)
    window.show()

    # Запускаем цикл обработки событий
    sys.exit(app.exec())