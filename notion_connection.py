import json
import requests

class NotionConnection:

    HEADERS = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json"
    }

    def __init__(self, database_id: str):
        self.database_id = database_id


    def get_pms(self):
        url = f'https://api.notion.com/v1/databases/{self.database_id}/query'
        payload = {'page_size': 100}
        r = requests.post(url, json=payload, headers = NotionConnection.HEADERS)

        result_dict = r.json()

        with open('db.json', 'w', encoding='utf8') as f:
            json.dump(result_dict, f, ensure_ascii=False, indent=4)
        
        results = result_dict['results']

        return results

    def create_pm(self, data: dict):
        create_url = 'https://api.notion.com/v1/pages'
        payload= {'parent': {'database_id': self.database_id}, 'properties': data}

        r = requests.post(create_url, headers= NotionConnection.HEADERS, json= payload)
        print(r.status_code)

        return r

    def update_pms(self, page_id: str, data: dict):
        url= f'https://api.notion.com/v1/pages/{page_id}'
        payload= {'properties': data}

        r = requests.patch(url, json=payload, headers=NotionConnection.HEADERS)
        print(r.status_code)
        return r

    def delete_pms(self, page_id: str):
        url= f'https://api.notion.com/v1/pages/{page_id}'

        payload= {'archived': True}

        r = requests.patch(url, json=payload, headers=NotionConnection.HEADERS)
        print(r.status_code)
        return r