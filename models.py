import database
from sqlalchemy import Column, Integer, String, Float

Base = database.Base

class Implied_Risk_Tolerance(Base):
    __tablename__ = 'implied_risk_tolerance'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer)
    score = Column(Float)
    weightage_average = Column(Float)
    imrt_seqid = Column(Integer)
    investor_id = Column(String)
    tenant_id = Column(String, nullable=True)
    risk_level_name = Column(String, nullable=True)

class Implied_Risk_Tolerance_Value(Base):
    __tablename__ = 'implied_risk_tolerance_value'

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float)
    imrtc_seq_id = Column(Integer)
    investor_id = Column(String)
    risk_level = Column(String)
    tenant_id = Column(String, nullable=True)

class Investment_Horizon(Base):
    __tablename__ = 'investment_horizon'

    id = Column(Integer, primary_key=True, index=True)
    investment_horizon_value = Column(Integer)
    tenant_id = Column(Integer, nullable=True)
    ih_seqid = Column(Integer)
    risk_level_id = Column(Integer)

class Portfolio_Optimization_Result_CR(Base):
    __tablename__ = 'portfolio_optimization_result_cr'

    id = Column(Integer, primary_key=True, index=True)
    por_cr_seqid = Column(Integer)
    index_result = Column(Integer)
    risk_rating = Column(String)
    risk_score = Column(Integer)
    tenant_id = Column(Integer, nullable=True)

class Question_Category(Base):
    __tablename__ = 'question_category'

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(Integer, nullable=True)
    weight = Column(Integer)
    que_seqid = Column(Integer)
    category_name = Column(String)

class Question_List(Base):
    __tablename__ = 'question_list'

    id = Column(Integer, primary_key=True, index=True)
    weight = Column(Integer)
    category_id = Column(Integer)
    quelist_seqid = Column(Integer)
    question = Column(String)
    question_type = Column(String)

class Response_List(Base):
    __tablename__ = 'response_list'

    id = Column(Integer, primary_key=True, index=True)
    risk_level_score = Column(Integer)
    question_id = Column(Integer)
    rl_seqid = Column(Integer)
    response_name = Column(String)

class Risk_Level_Score(Base):
    __tablename__ = 'risk_level_score'

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    tenant_id = Column(Integer, nullable=True)
    rls_seqid = Column(Integer)

class Security_Universe(Base):
    __tablename__ = 'security_universe'

    id = Column(Integer, primary_key=True, index=True)
    duration = Column(Float)
    index_no = Column(Integer)
    tenant_id = Column(Integer, nullable=True)
    weight = Column(Float)
    ytm = Column(Float)
    su_seqid = Column(Integer)
    issuer = Column(String, nullable=True)
    security_name = Column(String)

class Target_Yield(Base):
    __tablename__ = 'target_yield'

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Integer)
    target_yield_from = Column(Float)
    target_yield_to = Column(Float)
    tenant_id = Column(Integer, nullable=True)
    ty_seqid = Column(Integer)
