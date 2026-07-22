from config.db.models import Company


class CompanyDB:
    def __init__(self, session):
        self.session = session

    def get_all_companies(self):
        return self.session.query(Company).all()

    def get_company_by_id(self, company_id):
        return self.session.query(Company).filter(Company.id == company_id).first()

    def add_company(self, company_data: dict):
        new_company = Company(**company_data)
        self.session.add(new_company)
        self.session.commit()
        return new_company

    def update_company(self, company_id, name_company=None, contact_person=None, phone=None, email=None, website=None):
        company = self.get_company_by_id(company_id)
        if company:
            if name_company is not None:
                company.name = name_company
            if contact_person is not None:
                company.contact_person = contact_person
            if phone is not None:
                company.phone = phone
            if email is not None:
                company.email = email
            if website is not None:
                company.website = website
            self.session.commit()
        return company

    def delete_company(self, company_id):
        company = self.get_company_by_id(company_id)
        if company:
            self.session.delete(company)
            self.session.commit()