import os
from notion_connection import NotionConnection
import json
from datetime import datetime, timezone

#notion auth
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')


notion_database = NotionConnection(NOTION_TOKEN, DATABASE_ID)

# print(json.dumps(notion_database.get_page(), indent=4))

title = "Test Title"
description = "Test Description"
published_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "URL": {"title": [{"text": {"content": description}}]},
    "Title": {"rich_text": [{"text": {"content": title}}]},
    "Published": {"date": {"start": published_date, "end": None}}
}

bloque = 'Testing paragraph'

print(notion_database.get_page())

notion_database.create_page(data, bloque)