"""
Improve code cohesion
Put all the attributes and methods where they belong
"""


class Session:
    session_id = 40


class Settings:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url

    def addition(self, a: float, b: float) -> float:
        return a + b

    def create_db_session(self) -> Session:
        return Session()

    def get_connection_string(self) -> str
        return "my_connnection_string"


class Database:
    def subtraction(self, a: float, b: float) -> float:
        return a - b

    def truncate_table(self, table_name: str) -> None:
        print(f"truncating table {table_name}")

    def print_settings(self) -> None:
        print("printing all settings")


class Calculator:
    def __init__(self, autocommit: bool) -> None:
        self.autocommit = autocommit

    def multiplication(self, a: float, b: float) -> float:
        return a * b

    def drop_database(self, db_name: str):
        print(f"dropping database {db_name}")



