import sqlite3
from contextlib import closing

DB_NAME = "dedup_store.db"

def init_db():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS events (
                    topic TEXT,
                    event_id TEXT,
                    PRIMARY KEY (topic, event_id)
                )
            ''')
            conn.commit()

def add_event(topic, event_id):
    with closing(sqlite3.connect(DB_NAME)) as conn:
        with closing(conn.cursor()) as cursor:
            try:
                cursor.execute('INSERT INTO events (topic, event_id) VALUES (?, ?)', (topic, event_id))
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                return False

def get_events():
    with closing(sqlite3.connect(DB_NAME)) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('SELECT * FROM events')
            return cursor.fetchall()