import sqlite3
from typing import Dict


def insert_customer_goal_data(connection: sqlite3.Connection, goal_details: Dict):
    columns = ', '.join(goal_details.keys())
    placeholders = ', '.join('?' * len(goal_details))

    sql = 'INSERT INTO CUSTOMER_GOALS ({}) VALUES ({})'.format(columns, placeholders)
    values = [goal_data for goal_data in goal_details.values()]

    curr = connection.cursor()
    curr.execute(sql, values)
    connection.commit()
