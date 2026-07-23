from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from config.db.models import Call


class StatisticsService:
    def __init__(self, table_widget: QTableWidget, parent_widget, session_maker: sessionmaker):
        self.table = table_widget
        self.parent = parent_widget
        self.session_maker = session_maker

        self.setup_table()

    def setup_table(self):
        """Настройка таблицы статистики (2 столбца)"""
        table = self.table
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Показатель", "Значение"])
        table.setEditTriggers(QTableWidget.NoEditTriggers)  # type: ignore
        header = table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Загружаем статистику за всё время
        self.load_statistics()

    def load_statistics(self, start_date=None, end_date=None):
        """
        Загружает статистику за указанный период.
        Если даты не заданы – за всё время.
        """
        with self.session_maker() as session:
            query = session.query(Call)
            if start_date:
                query = query.filter(Call.date_call >= start_date)
            if end_date:
                # Приводим end_date к концу дня (если это дата без времени)
                if isinstance(end_date, datetime):
                    end_date = end_date.replace(hour=23, minute=59, second=59)
                query = query.filter(Call.date_call <= end_date)
            calls = query.all()

        # Вычисляем показатели
        total = len(calls)
        connected = sum(1 for c in calls if c.status != 'Не дозвонился')
        not_connected = total - connected

        interested = sum(1 for c in calls if c.status == 'Заинтересован')
        invited = sum(1 for c in calls if c.status == 'Приглашён на собеседование')
        rejections = sum(1 for c in calls if c.status == 'Отказ')
        hired = sum(1 for c in calls if c.status == 'Нанят')

        durations = [c.duration_minutes for c in calls if c.duration_minutes is not None]
        avg_duration = sum(durations) / len(durations) if durations else 0
        efficiency = (connected / total * 100) if total > 0 else 0

        data = [
            ("Всего звонков", str(total)),
            ("Дозвонились", str(connected)),
            ("Не дозвонились", str(not_connected)),
            ("Заинтересованы", str(interested)),
            ("Приглашены на собеседование", str(invited)),
            ("Отказов", str(rejections)),
            ("Нанято", str(hired)),
            ("Средняя длительность", f"{avg_duration:.1f} мин"),
            ("Эффективность", f"{efficiency:.1f}%"),
        ]
        self._populate_table(data)

    def _populate_table(self, data):
        table = self.table
        table.setRowCount(len(data))
        for row, (label, value) in enumerate(data):
            table.setItem(row, 0, QTableWidgetItem(label))
            table.setItem(row, 1, QTableWidgetItem(value))

    # Методы-обёртки для фильтрации
    def load_day(self):
        """Статистика за сегодня"""
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        tomorrow = today + timedelta(days=1)
        self.load_statistics(start_date=today, end_date=tomorrow)

    def load_week(self):
        """Статистика за последнюю неделю"""
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        week_ago = today - timedelta(days=7)
        self.load_statistics(start_date=week_ago, end_date=today)

    def load_month(self):
        """Статистика за последний месяц (30 дней)"""
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        month_ago = today - timedelta(days=30)
        self.load_statistics(start_date=month_ago, end_date=today)

    def load_all(self):
        """Статистика за всё время"""
        self.load_statistics()