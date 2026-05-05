from db_manager import get_connection
from db_manager import get_connection


class Author:
    def __init__(self, id=None, name=None, surname=None, middle_name=None, position=None, department=None, email=None):
        self.id = id
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.position = position
        self.department = department
        self.email = email

    def save(self):
        """Добавление автора или обновление существующего"""
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute("""
                INSERT INTO Authors 
                (Name, Surname, Middle_name, Position, Department, Email)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.name, self.surname, self.middle_name, self.position, self.department, self.email))
            self.id = cur.lastrowid
        else:
            cur.execute("""
                UPDATE Authors 
                SET Name = ?, Surname = ?, Middle_name = ?, 
                    Position = ?, Department = ?, Email = ?
                WHERE AuthorID = ?
            """, (
                self.name, self.surname, self.middle_name, self.position, self.department, self.email, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        """Удаление автора"""
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Authors WHERE AuthorID = ?",
                (self.id,) )
            conn.commit()
            conn.close()


def get_all_authors():
    """Возвращает всех авторов"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT AuthorID, Name, Surname, Middle_name, Position, Department, Email
        FROM Authors""")
    rows = cur.fetchall()
    conn.close()
    return [
        Author(
            id=row[0],
            name=row[1],
            surname=row[2],
            middle_name=row[3],
            position=row[4],
            department=row[5],
            email=row[6]
        )
        for row in rows
    ]


def get_author_by_id(author_id):
    """Возвращает автора по ID"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT AuthorID, Name, Surname, Middle_name, Position, Department, Email
        FROM Authors
        WHERE AuthorID = ?
    """, (author_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return Author(
            id=row[0],
            name=row[1],
            surname=row[2],
            middle_name=row[3],
            position=row[4],
            department=row[5],
            email=row[6])
    return None