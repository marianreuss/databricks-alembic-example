
from datetime import date, datetime, time, timedelta, timezone
from uuid import UUID
from decimal import Decimal
from sqlalchemy.orm import Session
from model import SampleObject

from connect import get_engine


sample_object = {
	"bigint_col": 1234567890123456789,
	"string_col": "foo",
	"tinyint_col": -100,
	"int_col": 5280,
	"numeric_col": Decimal("525600.01"),
	"boolean_col": True,
	"date_col": date(2020, 12, 25),
	"datetime_col": datetime(
		1991, 8, 3, 21, 30, 5, tzinfo=timezone(timedelta(hours=-8))
	),
	"datetime_col_ntz": datetime(1990, 12, 4, 6, 33, 41),
	"time_col": time(23, 59, 59),
	"uuid_col": UUID(int=255),
}
sa_obj = SampleObject(**sample_object)

session = Session(get_engine())
session.add(sa_obj)
session.commit()
