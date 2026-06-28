from sqlalchemy import inspect
from sqlalchemy import text

from database.database import engine


def ensure_application_schema(
    print_summary=False
):

    with engine.begin() as connection:

        inspector = inspect(
            connection
        )

        tables = inspector.get_table_names()

        if "prediction_history" in tables:

            connection.execute(
                text(
                    "ALTER TABLE prediction_history "
                    "ADD COLUMN IF NOT EXISTS "
                    "room_service_spend_usd "
                    "DOUBLE PRECISION"
                )
            )

        connection.execute(
            text(
                "ALTER TABLE users "
                "ADD COLUMN IF NOT EXISTS role "
                "VARCHAR DEFAULT 'hotel_user' NOT NULL"
            )
        )

        connection.execute(
            text(
                "UPDATE users "
                "SET role = 'hotel_user' "
                "WHERE role IS NULL"
            )
        )

        admin_count = connection.execute(
            text(
                "SELECT COUNT(*) "
                "FROM users "
                "WHERE role = 'admin'"
            )
        ).scalar()

        user_count = connection.execute(
            text(
                "SELECT COUNT(*) "
                "FROM users"
            )
        ).scalar()

        if user_count and admin_count == 0:

            connection.execute(
                text(
                    "UPDATE users "
                    "SET role = 'admin' "
                    "WHERE id = ("
                    "SELECT id FROM users "
                    "ORDER BY created_at ASC "
                    "LIMIT 1"
                    ")"
                )
            )

        if print_summary:

            users = connection.execute(
                text(
                    "SELECT id, name, email, role "
                    "FROM users "
                    "ORDER BY id"
                )
            ).fetchall()

            print(
                users
            )


def main():

    ensure_application_schema(
        print_summary=True
    )


if __name__ == "__main__":

    main()
