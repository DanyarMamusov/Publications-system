from database.db_manager import get_connection


def get_publication_count_by_author():
    """Возвращает количество публикаций по авторам"""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT (a.Surname || ' ' || a.Name || ' ' || IFNULL(a.Middle_name, '')) AS AuthorName, COUNT(p.PublicationID) AS PublicationCount
        FROM Authors a
        LEFT JOIN Authorship au ON a.AuthorID = au.AuthorID
        LEFT JOIN Publications p ON au.AuthorshipID = p.AuthorshipID
        GROUP BY a.AuthorID
        ORDER BY PublicationCount DESC""")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_publication_count_by_type():
    """Возвращает количество публикаций по типам"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT pt.TypeName, COUNT(p.PublicationID) AS PublicationCount
        FROM Publication_types pt
        LEFT JOIN Publications p ON pt.TypeID = p.TypeID
        GROUP BY pt.TypeID
        ORDER BY PublicationCount DESC""")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_publication_count_by_status():
    """Возвращает количество публикаций по статусам"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT 
            st.StatusName,
            COUNT(p.PublicationID) AS PublicationCount
        FROM Publication_statuses st
        LEFT JOIN Publications p ON st.StatusID = p.StatusID
        GROUP BY st.StatusID
        ORDER BY PublicationCount DESC""")
    rows = cur.fetchall()
    conn.close()
    return rows
