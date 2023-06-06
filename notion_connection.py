import json
import requests

class NotionConnection:

    def __init__(self, sec_token, database_id: str):
        self.database_id = database_id
        self.headers = {
            "Authorization": "Bearer " + sec_token,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }


    def get_page(self):
        url = f'https://api.notion.com/v1/databases/{self.database_id}/query'
        payload = {'page_size': 100}
        r = requests.post(url, json=payload, headers = self.headers)

        result_dict = r.json()

        with open('db.json', 'w', encoding='utf8') as f:
            json.dump(result_dict, f, ensure_ascii=False, indent=4)
        
        results = result_dict['results']

        return results

    # def create_page(self, data: dict):
    #     create_url = "https://api.notion.com/v1/pages"

    #     payload = {"parent": {"database_id": self.database_id}, "properties": data}

    #     res = requests.post(create_url, headers=self.headers, json=payload)
    #     # print(res.status_code)
    #     return res

    def create_page(self, data: dict, block):
        create_url = 'https://api.notion.com/v1/pages'
        payload= {'parent': 
            {
                'database_id': self.database_id
            }, 
            'properties': data, 
            'children': [
                {
                    'object': 'block',
                    'type': 'heading_2',
                    'heading_2': {
                        'text': [{'type': 'text', 'text': {'content': 'Prediction Market'}}]
                    }
                },
                {
                    'object': 'block',
                    'type': 'paragraph',
                    'paragraph': {
                        'text': [{'type': 'text', 'text': {'content': block}}]
                    }
                }
            ]
        }
        

        r = requests.post(create_url, headers= self.headers, json= payload)
        print(r.status_code)

        return r

    def add_block_children(self, page_id, data:dict):
        page_id_edited = page_id.replace('-','')
        print(page_id_edited)
        url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        block_data = {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "text": [
                    {
                        "type": "text",
                        "text": {
                            "content": data
                        }
                    }
                ]
            }
        }

        r = requests.patch(url, headers=self.headers, json=block_data)

        if r.status_code == 200:
            print("Block added")
        else:
            print("Error:", r.status_code, r.text)


    def update_page(self, page_id: str, data: dict):
        url= f'https://api.notion.com/v1/pages/{page_id}'
        payload= {'properties': data}

        r = requests.patch(url, json=payload, headers=self.headers)
        print(r.status_code)
        return r

    def delete_page(self, page_id: str):
        url= f'https://api.notion.com/v1/pages/{page_id}'

        payload= {'archived': True}

        r = requests.patch(url, json=payload, headers=self.headers)
        print(r.status_code)
        return r