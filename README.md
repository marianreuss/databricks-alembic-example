# A minimal example to use SQLAlchemy & alembic on databricks



* Copy your specs from the SQL warehouse's `Connection Details` tab and set them as env vars (see [connect.py](databricks_alembic_example/connect.py) for required variables.)
* There are two alembic revisions in [databricks_alembic_example/alembic/versions](databricks_alembic_example/alembic/versions)

# Installation

```console
pip install -e .
```