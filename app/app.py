import sys
from PySide6.QtWidgets import QApplication
from app.utils.chek_or_create_user_role import check_default_role
from app.windows.login import LoginWindow
from PySide6.QtWidgets import QApplication
from config.db.database import sync_sessionmaker




if __name__ == "__main__":
    check_default_role(sync_sessionmaker)
    
    app = QApplication(sys.argv)
    # Создаём окно входа и показываем, передаем сессию работы с базой данных в конструктор
    window = LoginWindow(session_maker=sync_sessionmaker)
    window.show()

    # Запускаем цикл обработки событий
    sys.exit(app.exec())