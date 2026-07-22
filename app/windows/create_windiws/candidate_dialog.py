from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QTextEdit, QComboBox, QPushButton
)
from PySide6.QtCore import Qt


class CandidateEditDialog(QDialog):
    def __init__(self, data=None, parent=None, session_maker=None):
        super().__init__(parent)
        self.session_maker = session_maker
        self.data = data or {}
        self.setWindowTitle("Редактирование кандидата" if data else "Новый кандидат")
        self.setModal(True)

        # Поля ввода
        self.name_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.link_resume_edit = QLineEdit()
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Новый", "В работе", "Собеседование", "Нанят", "Отказ"])
        self.comment_edit = QTextEdit()

        # Заполняем поля данными (если редактирование)
        self.load_data()

        # Собираем форму
        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.addRow("ФИО:", self.name_edit)
        form.addRow("Телефон:", self.phone_edit)
        form.addRow("Email:", self.email_edit)
        form.addRow("Статус:", self.status_combo)
        form.addRow("Ссылка на резюме:", self.link_resume_edit)
        form.addRow("Комментарий:", self.comment_edit)
        layout.addLayout(form)

        # Кнопки
        btn_box = QHBoxLayout()
        ok_btn = QPushButton("Сохранить")
        cancel_btn = QPushButton("Отмена")
        ok_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btn_box.addWidget(ok_btn)
        btn_box.addWidget(cancel_btn)
        layout.addLayout(btn_box)

        self.setLayout(layout)

    def load_data(self):
        if not self.data:
            return
        self.name_edit.setText(self.data.get("name_candidate", ""))
        self.phone_edit.setText(self.data.get("phone", ""))
        self.email_edit.setText(self.data.get("email", ""))
        self.link_resume_edit.setText(self.data.get("link_resume", ""))
        status = self.data.get("status", "")
        index = self.status_combo.findText(status)
        if index >= 0:
            self.status_combo.setCurrentIndex(index)
        self.comment_edit.setPlainText(self.data.get("comment", ""))

    @property
    def result_data(self):
        return {
            "name_candidate": self.name_edit.text().strip(),
            "phone": self.phone_edit.text().strip() or None,
            "email": self.email_edit.text().strip() or None,
            "link_resume": self.link_resume_edit.text().strip() or None,
            "status": self.status_combo.currentText(),
            "comment": self.comment_edit.toPlainText().strip() or None,
        }