import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7715317380:AAGDYdtGVXuT2WoRio2FvMFWfhAkPvBvG1c")
      API_ID = int(os.environ.get("APP_ID", 26162072))
      API_HASH = os.environ.get("ba25181c01b50d945748801b6c8b6ecc")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "AvishkarPatil")
