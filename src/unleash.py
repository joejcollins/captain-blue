"""The unleash client"""
from UnleashClient import UnleashClient
from functools import lru_cache


@lru_cache
def get_unleash() -> UnleashClient:
    """Initialise Unleash client for feature toggling and caching it for reuse."""
    # https://docs.getunleash.io/unleash-client-python/usage.html#using-unleashclient-with-gitlab
    unleash = UnleashClient(
        url="https://gitlab.com/api/v4/feature_flags/unleash/40359845",
        app_name="production",
        instance_id="dqKX_y6shyKCV7haRyyu",
        disable_metrics=True,  # Disable metrics to work with Gitlab
        disable_registration=True,  # Disable registration to work with Gitlab
    )
    unleash.initialize_client()
    return unleash
