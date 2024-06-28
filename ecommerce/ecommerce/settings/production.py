from .base import *

ALLOWED_HOSTS = ["*"]

sentry_sdk.init(
    dsn="https://bdb75d660f48b5f5239d2bbfbe17b5c5@o4507510214295552.ingest.de.sentry.io/4507510215802960",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
