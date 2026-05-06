from database.db_manager import get_connection
class Publication:
    def __init__(self, id=None, title=None, date=None, doi=None, link=None, type_id=None, source_id=None, status_id=None,  authorship_id=None):
        self.id = id
        self.title = title
        self.date = date
        self.doi = doi
        self.link = link
        self.type_id = type_id
        self.source_id = source_id
        self.status_id = status_id
        self.authorship_id = authorship_id

    def save(self):
        """Добавление публикации или обновление существующей"""
        conn = get_connection()
        cur = conn.cursor()
        if self.id is None:
            cur.execute("""
                INSERT INTO Publications
                (PublicationTitle, Date, DOI, Link, TypeID, SourceID, StatusID, AuthorshipID)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (self.title, self.date, self.doi, self.link, self.type_id, self.source_id, self.status_id, self.authorship_id))
            self.id = cur.lastrowid
        else:
            cur.execute("""
                UPDATE Publications
                SET PublicationTitle = ?, Date = ?, DOI = ?, Link = ?, TypeID = ?, SourceID = ?, StatusID = ?, AuthorshipID = ?
                WHERE PublicationID = ?""", (self.title, self.date,  self.doi, self.link, self.type_id, self.source_id, self.status_id, self.authorship_id, self.id))
        conn.commit()
        conn.close()

    def delete(self):
        """Удаление публикации"""
        if self.id is not None:
            conn = get_connection()
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM Publications WHERE PublicationID = ?",
                (self.id,))
            conn.commit()
            conn.close()


def get_all_publications():
    """Возвращает все публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT PublicationID, PublicationTitle, Date, DOI, Link, TypeID, SourceID, StatusID, AuthorshipID
        FROM Publications""")
    rows = cur.fetchall()
    conn.close()
    return [
        Publication(
            id=row[0],
            title=row[1],
            date=row[2],
            doi=row[3],
            link=row[4],
            type_id=row[5],
            source_id=row[6],
            status_id=row[7],
            authorship_id=row[8])
        for row in rows
    ]


def get_publication_by_id(publication_id):
    """Возвращает публикацию по ID"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT PublicationID, PublicationTitle, Date, DOI, Link,
               TypeID, SourceID, StatusID, AuthorshipID
        FROM Publications
        WHERE PublicationID = ?
    """, (publication_id,))
    row = cur.fetchone()
    conn.close()
    if row:
        return Publication(
            id=row[0],
            title=row[1],
            date=row[2],
            doi=row[3],
            link=row[4],
            type_id=row[5],
            source_id=row[6],
            status_id=row[7],
            authorship_id=row[8])
    return None


def update_publication_status(publication_id, status_id):
    """Изменение статуса публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(""" UPDATE Publications SET StatusID = ? WHERE PublicationID = ?""", (status_id, publication_id))
    conn.commit()
    conn.close()


def get_publications_full_info():
    """Возвращает публикации с расшифровкой справочных данных"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(""" SELECT p.PublicationID, p.PublicationTitle,p.Date,p.DOI, p.Link, pt.TypeName, ps.SourceTitle, st.StatusName, a.Surname || ' ' || a.Name || ' ' || IFNULL(a.Middle_name, '') AS AuthorName
        FROM Publications p
        LEFT JOIN Publication_types pt ON p.TypeID = pt.TypeID
        LEFT JOIN Publication_sources ps ON p.SourceID = ps.SourceID
        LEFT JOIN Publication_statuses st ON p.StatusID = st.StatusID
        LEFT JOIN Authorship au ON p.AuthorshipID = au.AuthorshipID
        LEFT JOIN Authors a ON au.AuthorID = a.AuthorID
        ORDER BY p.PublicationID""")
    rows = cur.fetchall()
    conn.close()
    return rows
    
    
