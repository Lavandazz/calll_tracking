from typing import Optional

from config.db.models import Vacancy


class VacancyDB:
    def __init__(self, session):
        self.session = session

    def get_vacancy_by_id(self, vacancy_id: int) -> Optional[Vacancy]:
        return self.session.query(Vacancy).filter(Vacancy.id == vacancy_id).first()

    def get_all_vacancies(self) -> list[Vacancy]:
        return self.session.query(Vacancy).all()

    def create_vacancy(self, vacancy_data: dict) -> Vacancy:
        new_vacancy = Vacancy(**vacancy_data)
        self.session.add(new_vacancy)
        self.session.commit()
        return new_vacancy

    def update_vacancy(self, vacancy_id: int, update_data: dict) -> Optional[Vacancy]:
        vacancy = self.get_vacancy_by_id(vacancy_id)
        if vacancy:
            for key, value in update_data.items():
                setattr(vacancy, key, value)
            self.session.commit()
            return vacancy
        return None

    def delete_vacancy(self, vacancy_id: int) -> bool:
        vacancy = self.get_vacancy_by_id(vacancy_id)
        if vacancy:
            self.session.delete(vacancy)
            self.session.commit()
            return True
        return False