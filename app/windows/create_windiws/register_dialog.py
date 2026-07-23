from PySide6.QtWidgets import QDialog, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox
from app.utils.hash_pass import hash_password
from config.db.models import User, Role, UserRole
from app.db.user_db import UserDB



class RegisterDialog(QDialog):
    def __init__(self, session_maker, parent=None):
        super().__init__(parent)
        self.session_maker = session_maker
        self.setWindowTitle("Регистрация")
        self.setModal(True)
        self.setFixedSize(350, 280)

        layout = QVBoxLayout(self)

        form = QFormLayout()
        self.username_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.telephone_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.confirm_edit = QLineEdit()
        self.confirm_edit.setEchoMode(QLineEdit.Password)

        form.addRow("Логин:", self.username_edit)
        form.addRow("Email:", self.email_edit)
        form.addRow("Телефон:", self.telephone_edit)
        form.addRow("Пароль:", self.password_edit)
        form.addRow("Подтвердите пароль:", self.confirm_edit)
        layout.addLayout(form)

        btn_layout = QVBoxLayout()
        register_btn = QPushButton("Зарегистрироваться")
        cancel_btn = QPushButton("Отмена")
        register_btn.clicked.connect(self.register)
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(register_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def register(self):
        username = self.username_edit.text().strip()
        email = self.email_edit.text().strip() or None
        telephone = self.telephone_edit.text().strip() or None
        password = self.password_edit.text().strip()
        confirm = self.confirm_edit.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Ошибка", "Логин и пароль обязательны")
            return
        if password != confirm:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают")
            return
        if len(password) < 4:
            QMessageBox.warning(self, "Ошибка", "Пароль должен быть не менее 4 символов")
            return

        with self.session_maker() as session:
            # Проверяем существование пользователя
            user_db = UserDB(session)
            if user_db.get_user_by_username(username):
                QMessageBox.warning(self, "Ошибка", "Пользователь с таким логином уже существует")
                return

            # Хешируем пароль
            hashed = hash_password(password)

            # Создаём пользователя
            new_user = User(
                username=username,
                email=email,
                telephone=telephone,
                hashed_password=hashed
            )
            session.add(new_user)
            session.flush()   # чтобы получить id

            # Получаем или создаём роль 'user'
            role = session.query(Role).filter(Role.role == 'user').first()
            if not role:
                role = Role(role='user')
                session.add(role)
                session.flush()

            # Привязываем роль
            user_role = UserRole(user_id=new_user.id, role_id=role.id)
            session.add(user_role)
            session.commit()

        QMessageBox.information(self, "Успех", "Регистрация завершена. Теперь можно войти.")
        self.accept()