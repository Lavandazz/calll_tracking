class AppContext:
    """Хранит состояние приложения: текущий пользователь"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._current_user_id = None
            cls._instance._current_user_role = None
        return cls._instance

    @property
    def current_user_id(self):
        return self._current_user_id

    @current_user_id.setter
    def current_user_id(self, value):
        self._current_user_id = value

    @property
    def current_user_role(self):
        return self._current_user_role

    @current_user_role.setter
    def current_user_role(self, value):
        self._current_user_role = value

    def is_admin(self):
        return self._current_user_role == 'admin'