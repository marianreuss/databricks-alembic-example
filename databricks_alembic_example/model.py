from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as sa
from sqlalchemy import Column, BigInteger, String, Integer, DateTime, Time, Uuid, Boolean, Date, Numeric
from databricks.sqlalchemy import TIMESTAMP, TINYINT


class Base(DeclarativeBase):
	pass

class SampleObject(Base):
	__tablename__ = "my_table"

	bigint_col = Column(BigInteger, primary_key=True)
	string_col = Column(String)
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


