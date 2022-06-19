import sqlite3
from typing import Dict

from models.models import Plan


def create_plan_data(connection: sqlite3.Connection, plan_details: Dict):
    columns = ', '.join(plan_details.keys())
    placeholders = ', '.join('?' * len(plan_details))

    sql = 'INSERT INTO PLAN ({}) VALUES ({})'.format(columns, placeholders)
    values = [plan_data for plan_data in plan_details.values()]

    curr = connection.cursor()
    curr.execute(sql, values)
    connection.commit()


def create_plan_promotion(connection: sqlite3.Connection, promotion_data: Dict):
    columns = ', '.join(promotion_data.keys())
    placeholders = ', '.join('?' * len(promotion_data))

    sql = 'INSERT INTO PLAN_PROMOTION ({}) VALUES ({})'.format(columns, placeholders)
    values = [_data for _data in promotion_data.values()]

    curr = connection.cursor()
    curr.execute(sql, values)
    connection.commit()


def get_all_plans_data(connection: sqlite3.Connection):
    curr = connection.cursor()
    curr.execute("SELECT * FROM PLAN")

    plans_data = curr.fetchall()
    plans_response = []
    for data in plans_data:
        plans_response.append(
            Plan(
                planName=data[1],
                amountOptions=data[2],
                tenureOptions=data[3],
                benefitPercentage=data[4],
                benefitType=data[5]
            )
        )

    return plans_response
