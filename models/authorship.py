from database.db_manager import get_connection
from models.author import Author
class Authorship:
    def __init__(self, id=None, author_id=None ):
        self.id = id
        self.author_id = author_id
    def save(self):
        """Добавление или обновление авторства"""
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute("""INSERT INTO Authorship (AuthorID)
                        VALUES(?)""",(self.author_id,))
            self.id = cur.lastrowid
        else:
            cur.execute("""UPDATE Authorship SET AuthorID = ? WHERE AuthorshipID = ?""",(self.author_id, self.id) )
        conn.commit()
        conn.close()
    def delete(self):
        """Удаление авторства"""
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM Authorship WHERE AuthorshipID = ?", (self.id,))
            conn.commit()
            conn.close()
def get_authorship_by_id(authorship_id):
    """Возвращает авторство по ID"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT AuthorshipID, AuthorID FROM Authorship WHERE AuthorshipID = ?""",
(authorship_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return Authorship(
            id = row[0],
            author_id = row[1])
    return None
def get_author_by_authorship_id(authorship_id):
    """Возвращение автора по ID авторства"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT a.AuthorID, a.Name, a.Surname, a.Middle_name, a.Position, a.Department, a.Email FROM Authorship au
                    JOIN Authors a ON au.AuthorID = a.AuthorID WHERE au.AuthorshipID = ?""",
                    (authorship_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return Author(
            id = row[0],
            name = row[1],
            surname = row[2],
            middle_name = row[3],
            position = row[4],
            department = row[5],
            email = row[6] )
    return None
        
        
