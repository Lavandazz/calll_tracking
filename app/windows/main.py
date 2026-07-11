from PySide6.QtWidgets import QComboBox, QDateEdit, QHBoxLayout, QHeaderView, QPushButton, QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
import sys
from PySide6.QtWidgets import QLabel, QLineEdit, QMessageBox, QMainWindow
from qtpy.QtCore import QDate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рекрутер CRM")
        self.setGeometry(100, 100, 1100, 700)

        # Центральный виджет и вкладки
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Создаём вкладки
        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # Вкладка "Журнал звонков"
        self.tab_calls = QWidget()
        self.tabs.addTab(self.tab_calls, "Журнал звонков")
        self.setup_calls_tab()

        # Вкладка "Кандидаты"
        self.tab_candidates = QWidget()
        self.tabs.addTab(self.tab_candidates, "Кандидаты")
        self.setup_candidates_tab()

    # ---------- НАСТРОЙКА ВКЛАДКИ "ЖУРНАЛ ЗВОНКОВ" ----------
    def setup_calls_tab(self):
        layout = QVBoxLayout(self.tab_calls)

        # Панель фильтров (горизонтальная)
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Дата с:"))
        self.date_from = QDateEdit()
        self.date_from.setDate(QDate.currentDate().addDays(-7))
        self.date_from.setCalendarPopup(True)
        filter_layout.addWidget(self.date_from)

        filter_layout.addWidget(QLabel("по:"))
        self.date_to = QDateEdit()
        self.date_to.setDate(QDate.currentDate())
        self.date_to.setCalendarPopup(True)
        filter_layout.addWidget(self.date_to)

        filter_layout.addWidget(QLabel("Кандидат:"))
        self.filter_candidate = QLineEdit()
        self.filter_candidate.setPlaceholderText("Поиск по имени")
        filter_layout.addWidget(self.filter_candidate)

        filter_layout.addWidget(QLabel("Результат:"))
        self.filter_result = QComboBox()
        self.filter_result.addItems(["Все", "Не дозвонился", "Отказ", "Заинтересован", "Приглашён на собеседование", "Нанят"])
        filter_layout.addWidget(self.filter_result)

        self.btn_apply_filter = QPushButton("Применить")
        self.btn_apply_filter.clicked.connect(self.apply_filter)
        filter_layout.addWidget(self.btn_apply_filter)

        self.btn_reset_filter = QPushButton("Сбросить")
        self.btn_reset_filter.clicked.connect(self.reset_filter)
        filter_layout.addWidget(self.btn_reset_filter)

        layout.addLayout(filter_layout)

        # Таблица звонков
        self.table_calls = QTableWidget()
        self.table_calls.setColumnCount(7)
        self.table_calls.setHorizontalHeaderLabels([
            "ID", "Дата/время", "Кандидат", "Результат",
            "Длительность (мин)", "Комментарий", "Действия"
        ])
        self.table_calls.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table_calls)

        # Кнопки управления звонками (горизонтальная панель)
        btn_layout = QHBoxLayout()
        self.btn_add_call = QPushButton("➕ Добавить звонок")
        self.btn_add_call.clicked.connect(self.add_call)
        btn_layout.addWidget(self.btn_add_call)

        self.btn_edit_call = QPushButton("✏️ Редактировать")
        self.btn_edit_call.clicked.connect(self.edit_call)
        btn_layout.addWidget(self.btn_edit_call)

        self.btn_delete_call = QPushButton("🗑️ Удалить")
        self.btn_delete_call.clicked.connect(self.delete_call)
        btn_layout.addWidget(self.btn_delete_call)

        btn_layout.addStretch()  # растягивает, чтобы кнопки были слева
        layout.addLayout(btn_layout)

        # Заполним таблицу тестовыми данными
        self.populate_calls()

    # ---------- НАСТРОЙКА ВКЛАДКИ "КАНДИДАТЫ" ----------
    def setup_candidates_tab(self):
        layout = QVBoxLayout(self.tab_candidates)

        # Поиск
        search_layout = QHBoxLayout()
        search_layout.addWidget(QLabel("Поиск:"))
        self.search_candidate = QLineEdit()
        self.search_candidate.setPlaceholderText("Имя или телефон")
        self.search_candidate.textChanged.connect(self.search_candidates)  # поиск при вводе
        search_layout.addWidget(self.search_candidate)
        layout.addLayout(search_layout)

        # Таблица кандидатов
        self.table_candidates = QTableWidget()
        self.table_candidates.setColumnCount(6)
        self.table_candidates.setHorizontalHeaderLabels([
            "ID", "ФИО", "Телефон", "Email", "Статус", "Источник"
        ])
        self.table_candidates.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table_candidates)

        # Кнопки
        btn_layout = QHBoxLayout()
        self.btn_add_candidate = QPushButton("➕ Добавить кандидата")
        self.btn_add_candidate.clicked.connect(self.add_candidate)
        btn_layout.addWidget(self.btn_add_candidate)

        self.btn_edit_candidate = QPushButton("✏️ Редактировать")
        self.btn_edit_candidate.clicked.connect(self.edit_candidate)
        btn_layout.addWidget(self.btn_edit_candidate)

        self.btn_delete_candidate = QPushButton("🗑️ Удалить")
        self.btn_delete_candidate.clicked.connect(self.delete_candidate)
        btn_layout.addWidget(self.btn_delete_candidate)

        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        # Заполним тестовыми данными
        self.populate_candidates()

    # ---------- ЗАГЛУШКИ ДЛЯ ДАННЫХ (ПОТОМ ЗАМЕНИМ НА БД) ----------
    def populate_calls(self):
        self.table_calls.setRowCount(5)
        test_data = [
            (1, "2026-07-11 10:30", "Иванов Иван", "Заинтересован", "5", "Обсудили зарплату", ""),
            (2, "2026-07-11 11:15", "Петрова Мария", "Не дозвонился", "0", "Автоответчик", ""),
            (3, "2026-07-10 16:20", "Сидоров Алексей", "Приглашён на собеседование", "12", "Назначена встреча на пятницу", ""),
            (4, "2026-07-10 09:45", "Козлова Анна", "Отказ", "3", "Не подходит график", ""),
            (5, "2026-07-09 14:00", "Николаев Дмитрий", "Нанят", "8", "Принят на позицию", "")
        ]
        for row, data in enumerate(test_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.table_calls.setItem(row, col, item)
            # В последней колонке можно добавить кнопки, но пока оставим пустым

    def populate_candidates(self):
        self.table_candidates.setRowCount(4)
        test_data = [
            (1, "Иванов Иван", "+7-999-123-45-67", "ivanov@mail.ru", "В работе", "HH.ru"),
            (2, "Петрова Мария", "+7-999-234-56-78", "petrova@mail.ru", "Новый", "LinkedIn"),
            (3, "Сидоров Алексей", "+7-999-345-67-89", "sidorov@mail.ru", "Собеседование", "Работа.ру"),
            (4, "Козлова Анна", "+7-999-456-78-90", "kozlova@mail.ru", "Отказ", "Рекомендация")
        ]
        for row, data in enumerate(test_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.table_candidates.setItem(row, col, item)

    # ---------- МЕТОДЫ-ОБРАБОТЧИКИ (ПОКА ПРОСТЫЕ ЗАГЛУШКИ) ----------
    def apply_filter(self):
        QMessageBox.information(self, "Фильтр", "Фильтр применён (заглушка)")

    def reset_filter(self):
        self.date_from.setDate(QDate.currentDate().addDays(-7))
        self.date_to.setDate(QDate.currentDate())
        self.filter_candidate.clear()
        self.filter_result.setCurrentIndex(0)
        QMessageBox.information(self, "Фильтр", "Фильтры сброшены")

    def add_call(self):
        # Здесь будет открываться диалог добавления звонка
        QMessageBox.information(self, "Добавить звонок", "Открыть форму добавления звонка")

    def edit_call(self):
        QMessageBox.information(self, "Редактировать", "Редактирование выбранного звонка")

    def delete_call(self):
        QMessageBox.information(self, "Удалить", "Удаление выбранного звонка")

    def search_candidates(self):
        # Поиск по вводимому тексту
        QMessageBox.information(self, "Поиск", "Поиск кандидатов (заглушка)")

    def add_candidate(self):
        QMessageBox.information(self, "Добавить кандидата", "Открыть форму добавления кандидата")

    def edit_candidate(self):
        QMessageBox.information(self, "Редактировать", "Редактирование выбранного кандидата")

    def delete_candidate(self):
        QMessageBox.information(self, "Удалить", "Удаление выбранного кандидата")

