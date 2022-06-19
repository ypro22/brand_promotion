import sqlite3


def create_plan_table(connection: sqlite3.Connection):
    """creates plan table"""
    with connection:
        curr = connection.cursor()

        # create table if it does not exist
        plan_table = """CREATE TABLE IF NOT EXISTS PLAN (
                        planId INTEGER PRIMARY KEY,
                        planName TEXT NOT NULL,
                        amountOptions REAL,
                        tenureOptions REAL,
                        benefitPercentage REAL NOT NULL,
                        benefitType TEXT NOT NULL
                     ); """
        curr.execute(plan_table)
        connection.commit()


def create_plan_promotion_table(connection: sqlite3.Connection):
    """creates plan promotion table"""
    with connection:
        curr = connection.cursor()

        # create table if it does not exist
        plan_promotion_table = """CREATE TABLE IF NOT EXISTS PLAN_PROMOTION (
                        promotionId INTEGER PRIMARY KEY,
                        planId INTEGER NOT NULL,
                        promotionName TEXT NOT NULL,
                        promotionBenefitPercentage REAL,
                        promotionUserLimit INTEGER,
                        promotionPeriodStart TIMESTAMP,
                        promotionPeriodEnd TIMESTAMP,
                        FOREIGN KEY (planId)
                            REFERENCES PLAN (planId)
                            ON DELETE CASCADE 
                            ON UPDATE NO ACTION
                     ); """
        curr.execute(plan_promotion_table)
        connection.commit()


def create_customer_goals_table(connection: sqlite3.Connection):
    """creates customer goals table"""

    with connection:
        curr = connection.cursor()

        # create table if it does not exist
        customer_goals = """CREATE TABLE IF NOT EXISTS CUSTOMER_GOALS (
                        planId INTEGER,
                        userId INTEGER,
                        selectedAmount REAL NOT NULL,
                        selectedTenure REAL NOT NULL,
                        startedDate TIMESTAMP NOT NULL,
                        depositedAmount REAL NOT NULL,
                        benefitPercentage REAL NOT NULL,
                        benefitType TEXT NOT NULL,
                        PRIMARY KEY (planId, userId)
                        FOREIGN KEY (planId)
                            REFERENCES PLAN (planId)
                            ON DELETE CASCADE 
                            ON UPDATE NO ACTION
                     ); """
        curr.execute(customer_goals)
        connection.commit()
