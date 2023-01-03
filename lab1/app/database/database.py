__all__ = ["USERS","CATEGORIES","RECORDS","db"]

USERS = [
    # {
    #     'id': 1,
    #     'name': 'Ivan'
    # }
]

CATEGORIES = [
    # {
    #     'id': 1,
    #     'category_name': 'Food',
    # },
]

RECORDS = [
    # {
    #     'id': 1,
    #     'user_id': 1,
    #     'category_id': 1,
    #     'date_time': '27.10.2022 - 14:20',
    #     'total': 100
    # },
    # {
    #     'id': 2,
    #     'user_id': 1,
    #     'category_id': 1,
    #     'date_time': '27.10.2022 - 14:20',
    #     'total': 100
    # }
]

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()