import bcrypt

def hash_password(password):
    # Генерируем соль
    salt = bcrypt.gensalt()
    # Хешируем пароль с солью
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')  # Возвращаем строку для хранения

def verify_password(password, hashed):
    # Проверяем пароль, используя ту же соль из хеша
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))