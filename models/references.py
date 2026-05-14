from database.db_manager import get_connection

def get_all_publication_types():
    """Возвращает все типы публикаций"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT TypeID, TypeName
        FROM Publication_types
        ORDER BY TypeID""")
    rows = cur.fetchall()
    conn.close()
    return rows


def add_publication_type(type_name):
    """Добавляет новый тип публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Publication_types (TypeName)
        VALUES (?)""", (type_name,))
    conn.commit()
    conn.close()


def delete_publication_type(type_id):
    """Удаляет тип публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Publication_types WHERE TypeID = ?", (type_id,))
    conn.commit()
    conn.close()


def get_all_publication_sources():
    """Возвращает все источники публикаций"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT SourceID, SourceTitle, Publisher, Publication_place, issn_isbn
        FROM Publication_sources
        ORDER BY SourceID
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


def add_publication_source(source_title, publisher, publication_place, issn_isbn):
    """Добавляет источник публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Publication_sources
        (SourceTitle, Publisher, Publication_place, issn_isbn)
        VALUES (?, ?, ?, ?)
    """, (source_title, publisher, publication_place, issn_isbn))

    conn.commit()
    conn.close()


def delete_publication_source(source_id):
    """Удаляет источник публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Publication_sources WHERE SourceID = ?", (source_id,))
    conn.commit()
    conn.close()


def get_all_publication_statuses():
    """Возвращает все статусы публикаций"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT StatusID, StatusName
        FROM Publication_statuses
        ORDER BY StatusID""")
    rows = cur.fetchall()
    conn.close()
    return rows


def add_publication_status(status_name):
    """Добавляет новый статус публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Publication_statuses (StatusName)
        VALUES (?)""", (status_name,))
    conn.commit()
    conn.close()


def delete_publication_status(status_id):
    """Удаляет статус публикации"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Publication_statuses WHERE StatusID = ?", (status_id,))
    conn.commit()
    conn.close()


def get_status_id_by_name(status_name):
    """Возвращает ID статуса по названию"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT StatusID
        FROM Publication_statuses
        WHERE StatusName = ? """, (status_name,))
    row = cur.fetchone()
    conn.close()
    if row:
        return row[0]
    return None

