from __future__ import annotations

from databricks.sqlalchemy import TIMESTAMP
from databricks.sqlalchemy import TINYINT
from sqlalchemy import BigInteger
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Time
from sqlalchemy import Uuid
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class SampleObject(Base):
    __tablename__ = "my_table"

    bigint_col = Column(BigInteger, primary_key=True)
    string_col = Column(String, comment="this is a comment")
    tinyint_col = Column(TINYINT)
    int_col = Column(Integer)
    numeric_col = Column(Numeric(10, 2))
    boolean_col = Column(Boolean)
    date_col = Column(Date)
    datetime_col = Column(TIMESTAMP)
    datetime_col_ntz = Column(DateTime)
    time_col = Column(Time)
    uuid_col = Column(Uuid)
    foo_col = Column(String)
