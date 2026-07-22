from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QMessageBox, QComboBox
)
from PySide6.QtCore import Qt

class CandidateEditDialog(QDialog):
    def __init__(self, candidate_data=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавление кандидата" if candidate_data is None else "Редактирование кандидата")
        self.setModal(True)
        self.setMinimumWidth(450)
        self.setStyleSheet("""... (тот же стиль) ...""")

        self.result_data = None

        self.name_edit = QLineEdit()
        self.phone_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.resume_edit = QLineEdit()
        self.status_combo = QComboBox()
        self.status_combo.addItems(["Новый", "В работе", "Собеседование", "Отказ", "Нанят"])
        self.comment_edit = QLineEdit()
        self.source_edit = QLineEdit()

        if candidate_data:
            self.name_edit.setText(candidate_data.get("name_candidate", ""))
            self.phone_edit.setText(candidate_data.get("phone", ""))
            self.email_edit.setText(candidate_data.get("email", ""))
            self.resume_edit.setText(candidate_data.get("link_resume", ""))
            status = candidate_data.get("status", "Новый")
            idx = self.status_combo.findText(status)
            if idx >= 0:
                self.status_combo.setCurrentIndex(idx)
            self.comment_edit.setText(candidate_data.get("comment", ""))
            self.source_edit.setText(candidate_data.get("source", ""))

        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        form.addRow("ФИО:", self.name_edit)
        form.addRow("Телефон:", self.phone_edit)
        form.addRow("Email:", self.email_edit)
        form.addRow("Ссылка на резюме:", self.resume_edit)
        form.addRow("Статус:", self.status_combo)
        form.addRow("Комментарий:", self.comment_edit)
        form.addRow("Источник:", self.source_edit)
        layout.addLayout(form)

        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Сохранить")
        cancel_btn = QPushButton("Отмена")
        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addStretch()
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        layout.addLayout(btn_layout)

    def accept(self):
        data = {
            "name_candidate": self.name_edit.text().strip(),
            "phone": self.phone_edit.text().strip(),
            "email": self.email_edit.text().strip(),
            "link_resume": self.resume_edit.text().strip(),
            "status": self.status_combo.currentText(),
            "comment": self.comment_edit.text().strip(),
            "source": self.source_edit.text().strip(),
        }
        if not data["name_candidate"]:
            QMessageBox.warning(self, "Ошибка", "ФИО обязательно")
            return
        self.result_data = data
        super().accept()