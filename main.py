import sqlite3
from typing import List

import uvicorn
from fastapi import FastAPI

from db import create_tables
from db.plans import create_plan_data, get_all_plans_data, create_plan_promotion
from db.customer_goals import insert_customer_goal_data
from models.models import Plan, CustomerGoals, PlanPromotion

app = FastAPI()

DB_CONNECTION = sqlite3.connect("./db/tortoise_db.db", check_same_thread=False)


@app.on_event("startup")
def create_db_tables():
    # create tables if not exists
    create_tables.create_plan_table(DB_CONNECTION)
    create_tables.create_customer_goals_table(DB_CONNECTION)
    create_tables.create_plan_promotion_table(DB_CONNECTION)


@app.on_event("shutdown")
def database_disconnect():
    DB_CONNECTION.close()


@app.get("/")
def service_health():
    return {"health": "Good"}


@app.get("/plan/all", response_model=List[Plan])
def get_all_plans():
    return get_all_plans_data(DB_CONNECTION)


@app.post("/plan/")
def create_plan(plan: Plan):
    create_plan_data(DB_CONNECTION, plan.__dict__)


@app.post("/plan/enroll")
def enroll_user_into_plan(customer_goal: CustomerGoals):
    insert_customer_goal_data(DB_CONNECTION, customer_goal.__dict__)


@app.post("/plan/promotion")
def create_promotion_for_plan(promotion_data: PlanPromotion):
    create_plan_promotion(DB_CONNECTION, promotion_data.__dict__)


if __name__ == '__main__':
    uvicorn.run(app)
