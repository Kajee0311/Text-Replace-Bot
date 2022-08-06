import os
from os import environ

# Your Auto Forward Channel ID's
FROM_CHANNELS = set(int(x)
                    for x in os.environ.get("FROM_CHANNELS", "").split())
TO_CHATS = set(int(x) for x in os.environ.get("TO_CHATS", "").split())

# required to Movies information
OMDB_KEY = environ.get("OMDB_KEY", "")

RE1TXT = os.environ.get("RE1TXT", "")
RE2TXT = os.environ.get("RE2TXT", "")
RE3TXT = os.environ.get("RE3TXT", "")
RE4TXT = os.environ.get("RE4TXT", "")
RE5TXT = os.environ.get("RE5TXT", "")
RE6TXT = os.environ.get("RE6TXT", "")

# text you want to replace with text above.
REPLACED1 = os.environ.get("REPLACED1", "")
REPLACED2 = os.environ.get("REPLACED2", "")
REPLACED3 = os.environ.get("REPLACED3", "")
REPLACED4 = os.environ.get("REPLACED4", "")
REPLACED5 = os.environ.get("REPLACED5", "")
REPLACED6 = os.environ.get("REPLACED6", "")