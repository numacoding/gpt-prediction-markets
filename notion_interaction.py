import os
from notion_connection import NotionConnection
import json

#notion auth
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')
headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

notion_database = NotionConnection(headers, DATABASE_ID)

print(json.dumps(notion_database.get_pms(), indent=4))