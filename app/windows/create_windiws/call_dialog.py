from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QPushButton, QMessageBox, QComboBox,
    QDateTimeEdit
)
from PySide6.QtCore import Qt, QDateTime

class CallEditDialog(QDialog):
    def __init__(self, call_data=None, candidates=None, vacancies=None, users=None, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Добавление звонка" if call_data is None else "Редактирование звонка")
        self.setModal(True)
        self.setMinimumWidth(450)
        self.setStyleSheet("""... (тот же стиль) ...""")

        self.result_data = None

        # Выпадающие списки для выбора кандидата, вакансии и пользователя
        self.candidate_combo = QComboBox()
        if candidates:
            for cand in candidates:
                self.candidate_combo.addItem(cand.name_candidate, cand.id)

        self.vacancy_combo = QComboBox()
        if vacancies:
            for vac in vacancies:
                self.vacancy_combo.addItem(vac.name_vacancy, vac.id)

        self.user_combo = QComboBox()
        if users:
            for usr in users:
                self.user_combo.addItem(usr.username, usr.id)

        self.date_edit = QDateTimeEdit()
        self.date_edit.setDateTime(QDateTime.currentDateTime())
        self.date_edit.setCalendarPopup(True)

        self.status_combo = QComboBox()
        self.status_combo.addItems(["Не дозвонился", "Отказ", "Заинтересован", "Приглашён на собеседование", "Нанят"])

        self.source_edit = QLineEdit()
        self.comment_edit = QLineEdit()
        self.resume_edit = QLineEdit()
        self.duration_edit = QLineEdit()

        if call_data:
            # Заполнить поля, если есть данные
            if call_data.get("id_candidate"):
                idx = self.candidate_combo.findData(call_data["id_candidate"])
                if idx >= 0:
                    self.candidate_combo.setCurrentIndex(idx)
            if call_data.get("id_vacancy"):
                idx = self.vacancy_combo.findData(call_data["id_vacancy"])
                if idx >= 0:
                    self.vacancy_combo.setCurrentIndex(idx)
            if call_data.get("id_user"):
                idx = self.user_combo.findData(call_data["id_user"])
                if idx >= 0:
                    self.user_combo.setCurrentIndex(idx)
            if call_data.get("date_call"):
                self.date_edit.setDateTime(call_data["date_call"])
            status = call_data.get("status", "")
            idx = self.status_combo.findText(status)
            if idx >= 0:
                self.status_combo.setCurrentIndex(idx)
            self.source_edit.setText(call_data.get("source", ""))
            self.comment_edit.setText(call_data.get("comment", ""))
            self.resume_edit.setText(call_data.get("link_resume", ""))
            self.duration_edit.setText(str(call_data.get("duration_minutes", "")))

        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        form.addRow("Кандидат:", self.candidate_combo)
        form.addRow("Вакансия:", self.vacancy_combo)
        form.addRow("Менеджер:", self.user_combo)
        form.addRow("Дата/время:", self.date_edit)
        form.addRow("Результат:", self.status_combo)
        form.addRow("Источник:", self.source_edit)
        form.addRow("Комментарий:", self.comment_edit)
        form.addRow("Ссылка на резюме:", self.resume_edit)
        form.addRow("Длительность (мин):", self.duration_edit)
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
        try:
            duration = int(self.duration_edit.text()) if self.duration_edit.text().strip() else None
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Длительность должна быть числом")
            return

        data = {
            "id_candidate": self.candidate_combo.currentData(),
            "id_vacancy": self.vacancy_combo.currentData(),
            "id_user": self.user_combo.currentData(),
            "date_call": self.date_edit.dateTime().toPython(),
            "status": self.status_combo.currentText(),
            "source": self.source_edit.text().strip(),
            "comment": self.comment_edit.text().strip(),
            "link_resume": self.resume_edit.text().strip(),
            "duration_minutes": duration,
        }
        if not data["id_candidate"] or not data["id_vacancy"] or not data["id_user"]:
            QMessageBox.warning(self, "Ошибка", "Выберите кандидата, вакансию и менеджера")
            return
        self.result_data = data
        super().accept()