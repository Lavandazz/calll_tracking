from config.db.models import Role


def check_default_role(session_maker):
    """Проверяет наличие роли 'user' в базе данных, если нет - создаёт её."""
    with session_maker() as session:
        if not session.query(Role).filter(Role.role == 'user').first():
            session.add(Role(role='user'))
            session.commit()
