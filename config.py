from os import environ

class Config(object):
    APP_ID = int(environ.get("APP_ID", "21288218"))
    API_HASH = environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    TG_USER_SESSION = environ.get("TG_USER_SESSION", "")
    ADMINS = [x.strip("@ ") for x in str(environ.get("ADMINS", "") or "").split(",") if x.strip("@ ")]
    STATUS_CHAT_GROUP_ID = -1003118824708
    STATUS_CHANNEL_ID = -1001631481154
    STATUS_CHANNEL_MSG_ID = int(environ.get("STATUS_CHANNEL_MSG_ID", "19"))
