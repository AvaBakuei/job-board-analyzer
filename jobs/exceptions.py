import openai


def handle_openai_error(error) -> list:
    if isinstance(error, openai.APITimeoutError):
        print(f"OpenAI API request timed out: {error}")
        return []
    elif isinstance(error, openai.APIConnectionError):
        print(f"Failed to connect to OpenAI API: {error}")
        return []
    elif isinstance(error, openai.RateLimitError):
        print(f"OpenAI API request exceeded the rate limit: {error}")
        return []
    elif isinstance(error, openai.AuthenticationError):
        print(f"OpenAI API authentication failed: {error}")
        return []
    elif isinstance(error, openai.BadRequestError):
        print(f"Invalid request sent to OpenAI API: {error}")
        return []
    elif isinstance(error, openai.InternalServerError):
        print(f"OpenAI API server error: {error}")
        return []
    elif isinstance(error, openai.APIError):
        print(f"OpenAI API returned an error: {error}")
        return []
