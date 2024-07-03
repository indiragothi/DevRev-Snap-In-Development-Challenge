# clone_work_item.py
import requests
import json

def main(inputs):
    API_TOKEN = 'your_api_token_here'
    API_URL = 'https://api.devrev.ai/v1/work_items'
    work_item_id = inputs['work_item_id']

    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'application/json'
    }

    # Get the existing work item
    response = requests.get(f'{API_URL}/{work_item_id}', headers=headers)
    if response.status_code != 200:
        return {'error': 'Failed to fetch work item'}

    work_item = response.json()

    # Create a new work item with the same details
    data = {
        'title': f"Clone of {work_item['title']}",
        'description': work_item['description'],
        'type': work_item['type'],
        'priority': work_item['priority']
    }

    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 201:
        return {'new_work_item_id': response.json()['id']}
    else:
        return {'error': 'Failed to create cloned work item'}
