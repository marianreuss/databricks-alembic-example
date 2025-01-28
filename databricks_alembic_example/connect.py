from sqlalchemy import create_engine
import os

engine = None

host = os.getenv("DATABRICKS_HOST").replace("https://", "").strip("/")
http_path = os.getenv("DATABRICKS_HTTP_PATH")
access_token = os.environ["DATABRICKS_TOKEN"]
catalog = os.getenv("DATABRICKS_CATALOG")
schema = os.getenv("DATABRICKS_SCHEMA")

url = f"databricks://token:{access_token}@{host}?http_path={http_path}&catalog={catalog}&schema={schema}"

extra_connect_args = {
	"_tls_verify_hostname": True,
	"_user_agent_entry": "PySQL Example Script",
}


def get_engine():
	global engine
	if not engine:
		engine = create_engine(url=url, connect_args=extra_connect_args, echo=True)
	return engine
