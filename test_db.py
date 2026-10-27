import pytest
import psycopg

@pytest.fixture
def db_connection():
    connection_config = {
        "host": "localhost",
        "port": 5432,
        "user": "myuser",
        "password": "mypassword",
        "dbname": "testdb",
    }

    conn = None
    try:
        conn = psycopg.connect(**connection_config)
        yield conn
    except Exception as e:
        pytest.fail(f"Не удалось подключиться к базе данных: {e}")
    finally:
        if conn:
            conn.close()


def test_postgresql_query(db_connection):
    with db_connection.cursor() as cursor:
        cursor.execute("SELECT NOW();")

        result = cursor.fetchone()

        assert result is not None, "Запрос вернул пустой результат"

        assert len(result) > 0, "Результат запроса пуст"

        print(f"\nУспешный ответ от БД: {result[0]}")
