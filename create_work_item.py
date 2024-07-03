import requests

# Replace with your DevRev API token and endpoint URL
API_TOKEN = 'your_api_token_here'
API_URL = 'https://api.devrev.ai/v1/work_items'

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}

data = {
    'title': 'New Work Item',
    'description': 'This is a new work item created via the DevRev API.',
    'type': 'issue',  # Example type
    'priority': 'medium'
}

response = requests.post(API_URL, headers=headers, json=data)

if response.status_code == 201:
    print('Work item created successfully:', response.json())
else:
    print('Failed to create work item:', response.text)