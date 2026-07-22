from datetime import datetime
from typing import Optional, List
from config.db.models import Call


class CallDB:
    def __init__(self, session):
        self.session = session

    def add_call(self, user_id: int, candidate_id: int, vacancy_id: int,
                 status: str, source: str, comment: str, duration_minutes: int,
                 date_call: datetime, link_resume: str) -> Call:
        new_call = Call(
            id_user=user_id,
            id_candidate=candidate_id,
            id_vacancy=vacancy_id,
            status=status,
            source=source,
            comment=comment,
            duration_minutes=duration_minutes,
            date_call=date_call,
            link_resume=link_resume
        )
        self.session.add(new_call)
        self.session.commit()
        return new_call

    def get_all_calls(self) -> List[Call]:
        """Возвращает все звонки (для администратора или без фильтра)"""
        return self.session.query(Call).all()

    def get_calls_by_user(self, user_id: int) -> List[Call]:
        """Возвращает звонки для конкретного пользователя"""
        return self.session.query(Call).filter(Call.id_user == user_id).all()

    def get_calls_by_candidate(self, candidate_id: int) -> List[Call]:
        return self.session.query(Call).filter(Call.id_candidate == candidate_id).all()

    def get_call_by_id(self, call_id: int) -> Optional[Call]:
        return self.session.query(Call).filter(Call.id == call_id).first()

    def update_call(self, call_id: int, update_data: dict) -> Optional[Call]:
        call = self.get_call_by_id(call_id)
        if call:
            for key, value in update_data.items():
                setattr(call, key, value)
            self.session.commit()
            return call
        return None

    def delete_call(self, call_id: int) -> bool:
        call = self.get_call_by_id(call_id)
        if call:
            self.session.delete(call)
            self.session.commit()
            return True
        return False