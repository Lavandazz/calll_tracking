from datetime import datetime

from config.db.models import Call


class CallDB:
    def __init__(self, session):
        self.session = session

    def add_call(self, user_id: int, candidate_id: int, vacancy_id: int, status: str, source: str, comment: str, duration_minutes: int, date_call: datetime, link_resume: str) -> Call:
        new_call = Call(
            user_id=user_id,
            candidate_id=candidate_id,
            vacancy_id=vacancy_id,
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

    def get_calls(self, user_id: int):
        query = self.session.query(Call)
        query = query.filter(Call.id_user == user_id)

        return query.all()

    def get_calls_by_candidate(self, candidate_id: int):
        query = self.session.query(Call)
        query = query.filter(Call.id_candidate == candidate_id)

        return query.all()