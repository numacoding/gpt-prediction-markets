import os
from notion_connection import NotionConnection
import json
from datetime import datetime, timezone

#notion auth
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
DATABASE_ID = os.getenv('DATABASE_ID')


notion_database = NotionConnection(NOTION_TOKEN, DATABASE_ID)

# print(json.dumps(notion_database.get_page(), indent=4))

# title = "Test Title1"
# description = "Futures"
# published_date = datetime.now().astimezone(timezone.utc).isoformat()
# data = {
#     "Market": {"title": [{"text": {"content": title}}]},
#     "Category": {"rich_text": [{"text": {"content": description}}]}
# }
# bloque = 'Testing paragraph'

# notion_database.create_page(data, bloque)

# data = {
#     "URL": {"title": [{"text": {"content": description}}]},
#     "Title": {"rich_text": [{"text": {"content": title}}]},
#     "Published": {"date": {"start": published_date, "end": None}}
# }

page_dict = notion_database.get_page()
page_url = page_dict[0]['url']
page_id = page_url.split('/')[-1]
print(page_id)

notion_database.add_block_children(page_dict[0]['id'], 'Test')