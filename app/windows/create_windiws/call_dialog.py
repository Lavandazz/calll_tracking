from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout,
    QLineEdit, QTextEdit, QComboBox, QPushButton,
    QDateTimeEdit, QSpinBox, QMessageBox
)
from PySide6.QtCore import Qt, QDateTime
from sqlalchemy.orm import sessionmaker
from app.db.candidate_db import CandidateDB      # предположим, есть
from app.db.vacancy_db import VacancyDB
from app.db.user_db import UserDB               # предположим, есть
from app.db.call_db import CallDB


class CallEditDialog(QDialog):
    def __init__(self, data=None, parent=None, session_maker: sessionmaker = None):
        super().__init__(parent)
        self.session_maker = session_maker
        self.data = data or {}
        self.setWindowTitle("Редактирование звонка" if data else "Новый звонок")
        self.setModal(True)

        # Поля ввода
        self.candidate_combo = QComboBox()
        self.vacancy_combo = QComboBox()
        self.user_combo = QComboBox()
        self.status_edit = QLineEdit()
        self.source_edit = QLineEdit()
        self.comment_edit = QTextEdit()
        self.duration_spin = QSpinBox()
        self.duration_spin.setRange(0, 999)
        self.duration_spin.setSuffix(" мин")
        self.date_edit = QDateTimeEdit()
        self.date_edit.setDateTime(QDateTime.currentDateTime())
        self.date_edit.setCalendarPopup(True)
        self.link_resume_edit = QLineEdit()

        # Заполняем выпадающие списки
        self.load_candidates()
        self.load_vacancies()
        self.load_users()

        # Заполняем поля данными (если редактирование)
        self.load_data()

        # Собираем форму
        layout = QVBoxLayout(self)
        form = QFormLayout()
        form.addRow("Кандидат:", self.candidate_combo)
        form.addRow("Вакансия:", self.vacancy_combo)
        form.addRow("Пользователь:", self.user_combo)
        form.addRow("Статус:", self.status_edit)
        form.addRow("Источник:", self.source_edit)
        form.addRow("Длительность (мин):", self.duration_spin)
        form.addRow("Дата/время звонка:", self.date_edit)
        form.addRow("Комментарий:", self.comment_edit)
        form.addRow("Ссылка на резюме:", self.link_resume_edit)
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

    def load_candidates(self):
        self.candidate_combo.clear()
        self.candidate_combo.addItem("Не выбран", None)
        if not self.session_maker:
            return
        try:
            with self.session_maker() as session:
                cand_db = CandidateDB(session)
                candidates = cand_db.get_all_candidates()  # предполагаем, что есть такой метод
                for c in candidates:
                    self.candidate_combo.addItem(c.name_candidate, c.id)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить кандидатов:\n{str(e)}")

    def load_vacancies(self):
        self.vacancy_combo.clear()
        self.vacancy_combo.addItem("Не выбрана", None)
        if not self.session_maker:
            return
        try:
            with self.session_maker() as session:
                vac_db = VacancyDB(session)
                vacancies = vac_db.get_all_vacancies()
                for v in vacancies:
                    self.vacancy_combo.addItem(v.name_vacancy, v.id)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить вакансии:\n{str(e)}")

    def load_users(self):
        self.user_combo.clear()
        self.user_combo.addItem("Не выбран", None)
        if not self.session_maker:
            return
        try:
            with self.session_maker() as session:
                user_db = UserDB(session)
                users = user_db.get_all_users()  # предполагаем, что есть
                for u in users:
                    self.user_combo.addItem(u.username, u.id)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить пользователей:\n{str(e)}")

    def load_data(self):
        if not self.data:
            return
        # Устанавливаем значения из словаря
        self.set_combo_by_id(self.candidate_combo, self.data.get("id_candidate"))
        self.set_combo_by_id(self.vacancy_combo, self.data.get("id_vacancy"))
        self.set_combo_by_id(self.user_combo, self.data.get("id_user"))
        self.status_edit.setText(self.data.get("status", ""))
        self.source_edit.setText(self.data.get("source", ""))
        self.comment_edit.setPlainText(self.data.get("comment", ""))
        self.duration_spin.setValue(self.data.get("duration_minutes", 0))
        self.link_resume_edit.setText(self.data.get("link_resume", ""))
        if "date_call" in self.data and self.data["date_call"]:
            dt = self.data["date_call"]
            if isinstance(dt, str):
                dt = QDateTime.fromString(dt, "yyyy-MM-dd HH:mm:ss")
            elif hasattr(dt, 'to_pydatetime'):  # если это datetime-объект
                dt = QDateTime.fromPython(dt)
            self.date_edit.setDateTime(dt)

    def set_combo_by_id(self, combo, id_val):
        if id_val is not None:
            idx = combo.findData(id_val)
            if idx >= 0:
                combo.setCurrentIndex(idx)

    @property
    def result_data(self):
        return {
            "id_candidate": self.candidate_combo.currentData(),
            "id_vacancy": self.vacancy_combo.currentData(),
            "id_user": self.user_combo.currentData(),
            "status": self.status_edit.text().strip(),
            "source": self.source_edit.text().strip(),
            "comment": self.comment_edit.toPlainText().strip(),
            "duration_minutes": self.duration_spin.value(),
            "date_call": self.date_edit.dateTime().toPython(),
            "link_resume": self.link_resume_edit.text().strip(),
        }