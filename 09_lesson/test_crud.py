import uuid

from db import run_test


def _unique_title(prefix: str) -> str:
    """Уникальное название, чтобы не пересекаться с реальными данными."""
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


def test_add_subject():
    def body(conn, track):
        subject_id = 1000
        title = _unique_title("Subject")

        with conn.cursor() as cur:
            # --- ДЕЙСТВИЕ: INSERT ---
            cur.execute(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (%s, %s);",
                (subject_id, title),
            )
            conn.commit()
            track(subject_id)

            # --- ПРОВЕРКА: SELECT по subject_id ---
            cur.execute(
                "SELECT subject_id, subject_title "
                "FROM subject WHERE subject_id = %s;",
                (subject_id,),
            )
            row = cur.fetchone()
            assert row is not None, "строка должна существовать после INSERT"
            assert row[0] == subject_id
            assert row[1] == title

            # --- ПРОВЕРКА: SELECT по названию ---
            cur.execute(
                "SELECT subject_id FROM subject WHERE subject_title = %s;",
                (title,),
            )
            found = cur.fetchone()
            assert found is not None
            assert found[0] == subject_id

    run_test(body)


def test_update_subject():
    def body(conn, track):
        subject_id = 2000
        old_title = _unique_title("Old")
        new_title = _unique_title("New")

        with conn.cursor() as cur:
            # --- ДЕЙСТВИЕ: INSERT ---
            cur.execute(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (%s, %s);",
                (subject_id, old_title),
            )
            conn.commit()
            track(subject_id)

            # Убеждаемся, что до UPDATE название старое
            cur.execute(
                "SELECT subject_title FROM subject WHERE subject_id = %s;",
                (subject_id,),
            )
            before = cur.fetchone()
            assert before is not None
            assert before[0] == old_title

            # --- ДЕЙСТВИЕ: UPDATE ---
            cur.execute(
                "UPDATE subject SET subject_title = %s "
                "WHERE subject_id = %s;",
                (new_title, subject_id),
            )
            conn.commit()

            # --- ПРОВЕРКА: SELECT — название изменилось ---
            cur.execute(
                "SELECT subject_title FROM subject WHERE subject_id = %s;",
                (subject_id,),
            )
            after = cur.fetchone()
            assert after is not None
            assert after[0] == new_title
            assert after[0] != old_title

            # --- ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА: старого названия больше нет ---
            cur.execute(
                "SELECT subject_id FROM subject WHERE subject_title = %s;",
                (old_title,),
            )
            gone = cur.fetchone()
            assert gone is None

    run_test(body)


def test_delete_subject():
    def body(conn, track):
        subject_id = 3000
        title = _unique_title("ToDelete")

        with conn.cursor() as cur:
            # --- ДЕЙСТВИЕ: INSERT ---
            cur.execute(
                "INSERT INTO subject (subject_id, subject_title) "
                "VALUES (%s, %s);",
                (subject_id, title),
            )
            conn.commit()
            track(subject_id)

            # Убеждаемся, что строка есть
            cur.execute(
                "SELECT subject_id FROM subject WHERE subject_id = %s;",
                (subject_id,),
            )
            exists = cur.fetchone()
            assert exists is not None

            # --- ДЕЙСТВИЕ: DELETE ---
            cur.execute(
                "DELETE FROM subject WHERE subject_id = %s;",
                (subject_id,),
            )
            conn.commit()

            # --- ПРОВЕРКА: SELECT — строки больше нет ---
            cur.execute(
                "SELECT subject_id FROM subject WHERE subject_id = %s;",
                (subject_id,),
            )
            gone = cur.fetchone()
            assert gone is None

            # --- ДОПОЛНИТЕЛЬНАЯ ПРОВЕРКА: по названию тоже не находится ---
            cur.execute(
                "SELECT subject_id FROM subject WHERE subject_title = %s;",
                (title,),
            )
            by_title = cur.fetchone()
            assert by_title is None

    run_test(body)