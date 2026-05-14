from db_manager import get_connection
class User:
    def __init__(self, id=None, login=None, password=None, role=None):
        self.id = id
        self.login = login
        self.password = password
        self.role = role
def get_role_id(role_name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT RoleID FROM Roles WHERE RoleName = ?", (role_name,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0]
    return None
def register_user(login, password, role_name):
    role_id = get_role_id(role_name)
    if role_id is None:
        print("Такая роль не найдена.")
        return None
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Users (Login, Password, RoleID)
        VALUES (?, ?, ?)
    """, (login, password, role_id))
    conn.commit()
    conn.close()
def login_user(login, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT u.UserID, u.Login, u.Password, r.RoleName
        FROM Users u
        JOIN Roles r ON u.RoleID = r.RoleID
        WHERE u.Login = ? AND u.Password = ?
    """, (login, password))
    row = cur.fetchone()
    conn.close()
    if row:
        return User(
            id=row[0],
            login=row[1],
            password=row[2],
            role=row[3])
    return None