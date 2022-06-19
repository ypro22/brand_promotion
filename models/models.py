import datetime

from pydantic import BaseModel


class Plan(BaseModel):
    planName: str
    amountOptions: float | None = None
    tenureOptions: float | None = None
    benefitPercentage: float
    benefitType: str


class CustomerGoals(BaseModel):
    planId: int
    userId: int
    selectedAmount: float
    selectedTenure: float
    startedDate: datetime.date
    depositedAmount: float
    benefitPercentage: float
    benefitType: str


class PlanPromotion(BaseModel):
    planId: int
    promotionName: str
    promotionBenefitPercentage: float | None = None
    promotionUserLimit: int | None = None
    promotionPeriodStart: datetime.date | None = None
    promotionPeriodEnd: datetime.date | None = None
