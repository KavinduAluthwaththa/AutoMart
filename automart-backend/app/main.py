from fastapi import FastAPI
from .core.config import settings
from .core.database import Base, engine
from .api.v1 import cars


# Create tables (for dev only — use migrations in prod)
Base.metadata.create_all(bind=engine)


app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(cars.router)