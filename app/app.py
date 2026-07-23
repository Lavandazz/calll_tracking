import sys
from PySide6.QtWidgets import QApplication, QMessageBox, QDialog
from sqlalchemy import text  
from app.windows.login import LoginWindow
from app.windows.db_settings import DbSettingsWindow
from app.utils.chek_or_create_user_role import check_default_role
from config.settings import create_sessionmaker_from_settings
from config.load_settings_db import load_settings_from_qsettings



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 1. Пытаемся загрузить настройки из QSettings
    settings_obj = load_settings_from_qsettings()

    # 2. Если нет сохранённых настроек или они невалидны — показываем окно ввода
    if settings_obj is None:
        settings_dialog = DbSettingsWindow()
        if settings_dialog.exec() != QDialog.Accepted:
            sys.exit(0)  # пользователь закрыл окно или отменил
        # После сохранения в диалоге перечитываем настройки
        settings_obj = load_settings_from_qsettings()
        if settings_obj is None:
            QMessageBox.critical(None, "Ошибка", "Не удалось сохранить настройки.")
            sys.exit(1)

    # 3. Создаём sessionmaker на основе загруженных настроек
    try:
        session_maker = create_sessionmaker_from_settings(settings_obj)
        # Проверяем подключение
        with session_maker() as session:
            session.execute(text("SELECT 1"))
    except Exception as e:
        QMessageBox.critical(None, "Ошибка подключения",
                             f"Не удалось подключиться к БД:\n{str(e)}\n"
                             "Пожалуйста, проверьте настройки.")
        # Можно предложить открыть окно настроек повторно
        settings_dialog = DbSettingsWindow()
        if settings_dialog.exec() == QDialog.Accepted:
            # повторяем попытку (можно перезапустить приложение или сделать цикл)
            # Для простоты — завершим с сообщением, чтобы пользователь перезапустил
            QMessageBox.information(None, "Инструкция", "Перезапустите приложение после сохранения настроек.")
            sys.exit(0)
        else:
            sys.exit(1)

    # 4. Подготовка БД (роли, таблицы) — передаём session_maker
    check_default_role(session_maker)

    # 5. Запускаем окно логина
    login_window = LoginWindow(session_maker=session_maker)
    login_window.show()

    sys.exit(app.exec())