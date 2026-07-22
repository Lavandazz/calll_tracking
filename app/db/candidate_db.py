from typing import Optional, List
from datetime import date
from config.db.models import Candidate


class CandidateDB:
    def __init__(self, session):
        self.session = session

    def get_all_candidates(self) -> List[Candidate]:
        """Возвращает всех кандидатов"""
        return self.session.query(Candidate).all()

    def get_candidate_by_id(self, candidate_id: int) -> Optional[Candidate]:
        return self.session.query(Candidate).filter(Candidate.id == candidate_id).first()

    def create_candidate(self, candidate_data: dict) -> Candidate:
        """Создаёт нового кандидата из словаря"""
        new_candidate = Candidate(**candidate_data)
        self.session.add(new_candidate)
        self.session.commit()
        return new_candidate

    def update_candidate(self, candidate_id: int, update_data: dict) -> Optional[Candidate]:
        """Обновляет поля кандидата по ID"""
        candidate = self.get_candidate_by_id(candidate_id)
        if candidate:
            for key, value in update_data.items():
                setattr(candidate, key, value)
            self.session.commit()
            return candidate
        return None

    def delete_candidate(self, candidate_id: int) -> bool:
        candidate = self.get_candidate_by_id(candidate_id)
        if candidate:
            self.session.delete(candidate)
            self.session.commit()
            return True
        return False