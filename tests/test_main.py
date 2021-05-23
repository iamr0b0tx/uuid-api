import datetime
import uuid

from decouple import config
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from db.crud import create_uuid
from db.database import Base
from db.schemas import UUIDSchema
from main import app, get_db

SQLALCHEMY_DATABASE_URL = config("TEST_DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db() -> Session:
    db_session = TestingSessionLocal()
    try:
        yield db_session

    finally:
        db_session.close()


db = next(iter(override_get_db()))
app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

NUM_SAMPLES = 3
uuids = [create_uuid(db, UUIDSchema(uuid=str(uuid.uuid4()))) for _ in range(NUM_SAMPLES)]


# generic test
def test_get_base_endpoint():
    response = client.get('/')
    assert response.status_code == 404


def test_get_uuid_endpoint():
    response = client.get('/uuid')
    assert response.status_code == 200

    response_data = response.json()
    assert len(response_data) == 4

    for i in range(NUM_SAMPLES):
        assert uuids[0].uuid == response_data[-1]['uuid']
        assert str(uuids[0].timestamp).replace(" ", "T") == response_data[-1]['timestamp']
