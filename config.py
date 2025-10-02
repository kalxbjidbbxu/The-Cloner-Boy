from os import environ

class Config(object):
    TG_BOT_TOKEN = environ.get("TG_BOT_TOKEN", "")
    APP_ID = int(environ.get("APP_ID", "21288218"))
    API_HASH = environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")
    TG_USER_SESSION = "BQEMD9UAR98zcKfgfvVihxeL_g41R7dVmRuOhu095dUYGsrnsH5p-GNNsV8PMqrYU9PlIlUujIGAS31sSkBVEvFvh4Eh6H5MloziffkE9kk9mt6Gu0Vt6i13JUFhfThlYmJPgzfHrNqWofrVghwMM31aKb0N_QAm7kQ97BaSs3LRBCj-nzNUXBV2k7qfsvPhGAeEL27fkYeALNa3vpEG0816AALDAIeVdN1OUH1O-9q93Y7qTOoJARvy89sQqqOn5Al8wEi_HkDuWGxWbxakyO690hEfRml7KI90tHY-HcvdIWcl1MCnC7QUXltnlNxZ370jXlq3pkDrsyTKfJKWK02bD0CHowAAAAE9gIqFAA"
    FILE_CAPTION = environ.get('FILE_CAPTION', '<code>{file_name}</code>')
    ADMINS = [x.strip("@ ") for x in str(environ.get("ADMINS", "") or "").split(",") if x.strip("@ ")]
    
