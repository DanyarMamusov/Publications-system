import sqlite3
from config import DB_NAME
def get_connection():
    return sqlite3.connect(DB_NAME)
conn = get_connection()
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Publication_types (
        TypeID INTEGER PRIMARY KEY AUTOINCREMENT,
        TypeName TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Publication_sources(
        SourceID INTEGER PRIMARY KEY AUTOINCREMENT,
        SourceTitle TEXT,
        Publisher TEXT,
        Publication_place TEXT,
        issn_isbn TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Publication_statuses(
        StatusID INTEGER PRIMARY KEY AUTOINCREMENT,
        StatusName TEXT )''')
cur.execute('''CREATE TABLE IF NOT EXISTS Roles(
        RoleID INTEGER PRIMARY KEY AUTOINCREMENT,
        RoleName TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Authors(
        AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
        Surname TEXT,
        Name TEXT,
        Middle_name TEXT,
        Position TEXT,
        Department TEXT,
        Email TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Users(
         UserID INTEGER PRIMARY KEY AUTOINCREMENT,
         Login TEXT,
         Password TEXT,
         AuthorID INTEGER,
         RoleID INTEGER,
         FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID),
         FOREIGN KEY (RoleID) REFERENCES Roles(RoleID))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Authorship(
         AuthorshipID INTEGER PRIMARY KEY AUTOINCREMENT,
         AuthorID INTEGER,
         FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID))''')
cur.execute('''CREATE TABLE IF NOT EXISTS Publications(
         PublicationID INTEGER PRIMARY KEY AUTOINCREMENT,
         PublicationTitle TEXT,
         Date TEXT,
         DOI TEXT,
         Link TEXT,
         TypeID INTEGER,
         SourceID INTEGER,
         StatusID INTEGER,
         AuthorshipID INTEGER,
         FOREIGN KEY (TypeID) REFERENCES Publication_types(TypeID),
         FOREIGN KEY (SourceID) REFERENCES Publication_sources(SourceID),
         FOREIGN KEY (StatusID) REFERENCES Publication_statuses(StatusID),
         FOREIGN KEY (AuthorshipID) REFERENCES Authorship (AuthorshipID))''')
conn.commit()
conn.close()