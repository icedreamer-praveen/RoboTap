from typing import List, Optional

from pydantic import BaseModel


class InvestmentHorizon(BaseModel):
    investment_horizon_value:int
    tenant_id:int
    ih_seqid:int
    risk_level_id:int
