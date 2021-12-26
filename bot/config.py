import os


class Config:

    BOT_TOKEN = os.environ.get("1938198458:AAFCi1qkTeMTHCamqHacxGuSGXsuamGGIl0")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("4289473"))

    API_HASH = os.environ.get("6c829cf0df94349245c1dc156fef1132")

    CLIENT_ID = os.environ.get("611089228236-ptnf0vk3m8aousuaplr5u1fbvs67tqpb.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("4zoObnH0QOl5KdzguXfcqnaS")

    BOT_OWNER = int(os.environ.get("1722652154"))

    AUTH_USERS_TEXT = os.environ.get("1722652154", "")

    AUTH_USERS = [BOT_OWNER] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "Must Join on Telegram @dvmoviesbackup").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
