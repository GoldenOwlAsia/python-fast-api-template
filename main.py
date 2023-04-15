from fastapi import FastAPI
from app.api.v1.routes import users
import sentry_sdk
from dotenv import dotenv_values

config = dotenv_values(".env")

sentry_sdk.init(
    dsn=config.get('SENTRY_KEY'),

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,
)

app = FastAPI()
app.include_router(router=users.router)
