import secrets

from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

from app.config import CONVERSATIONAL_BOT_API_KEY


# Swagger lock icon support
api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)


def verify_api_key(
    api_key: str = Security(api_key_header)
):

    if not api_key:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key missing"
        )

    # secure comparison
    if not secrets.compare_digest(
        api_key,
        CONVERSATIONAL_BOT_API_KEY
    ):

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid API key"
        )

    return api_key

