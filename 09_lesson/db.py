import os
import psycopg2


DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "858")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "lesson")


def connect():
    """Открыть соединение с БД."""
    return psycopg2.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
    )


def run_test(test_function):
    """
    Открывает соединение, передаёт в тест conn и функцию track.
    После теста удаляет все subject_id, которые были созданы.

    Это делает тесты стабильными: их можно запускать много раз подряд.
    """
    conn = connect()
    created_ids = []  # список subject_id, которые надо удалить после теста

    def track(subject_id: int):
        """Запомнить id, чтобы удалить его после теста."""
        created_ids.append(subject_id)
        return subject_id

    try:
        test_function(conn, track)
    finally:
        # Удаляем всё, что создал тест, обычным DELETE-запросом
        with conn.cursor() as cur:
            for sid in reversed(created_ids):
                cur.execute(
                    "DELETE FROM subject WHERE subject_id = %s;",
                    (sid,),
                )
        conn.commit()
        conn.close()


__all__ = ["connect", "run_test"]