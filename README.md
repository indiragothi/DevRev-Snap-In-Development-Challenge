# DevRev Snap-In Development Challenge

To complete the Snap-in Development Challenge, we need to follow the steps as outlined and provide the necessary code snippets, documentation, and demonstrations. Here's the full solution in the required format:

### Step 1 (10 points): Utilizing the DevRev API

#### Task: Create a Work Item

Below is a Python code snippet demonstrating the creation of a work item using the DevRev API. This assumes you have the necessary API token and endpoint URL.

python
```bash
import requests

### Replace with your DevRev API token and endpoint URL

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
```


### Step 2 (30 points): Creating a Snap-in

#### Task: Create and Install a Snap-in

For this challenge, we will implement the following snap-ins:

1. *Command to clone a work item (issue/ticket).*
2. *Auto-Reply to a message if it is outside office hours.*

## Snap-in 1: Clone a Work Item 

```bash
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
```


### Instructions to Install and Use the Snap-in:

1. Place the manifest.yaml and clone_work_item.py files in your snap-in directory.
2. Use the DevRev CLI to install the snap-in:
   ```bash
   devrev snap-in install /path/to/snap-in-directory
   ```
   
3. Execute the snap-in command:
   ```bash
   devrev snap-in execute clone-work-item --inputs '{"work_item_id": "existing_work_item_id"}'
   ```
   

### Screenshot/Demonstration: 

![Clone Work Item Snap-in Demonstration](https://your-screenshot-url.com)



## Snap-in 2: Auto-Reply to Messages Outside Office Hours 

```bash
# auto_reply.py
import datetime

def main(inputs):
    start_time = inputs['start_time']
    end_time = inputs['end_time']
    auto_reply_message = inputs['auto_reply_message']

    now = datetime.datetime.now().time()
    start = datetime.datetime.strptime(start_time, "%H:%M").time()
    end = datetime.datetime.strptime(end_time, "%H:%M").time()

    if now < start or now > end:
        return {'message': auto_reply_message}
    else:
        return {'message': 'Within office hours, no auto-reply needed'}
```

### Instructions to Install and Use the Snap-in:

1. Place the manifest.yaml and auto_reply.py files in your snap-in directory.
2. Use the DevRev CLI to install the snap-in:
   ```bash
   devrev snap-in install /path/to/snap-in-directory
   ```
   
3. Configure the snap-in inputs and execute:
   ```bash
   devrev snap-in execute auto-reply --inputs '{"start_time": "09:00", "end_time": "17:00", "auto_reply_message": "Our office is currently closed. We will get back to you during office hours."}'
   ```
   

### Screenshot/Demonstration: 

![Auto-Reply Snap-in Demonstration](https://your-screenshot-url.com)



## Submission Guideline

1. **Repository Link:** [GitHub Repository](https://github.com/indiragothi/DevRev-Snap-In-Development-Challenge)

2. **Documentation:**
   - *Step 1:*
     - [Code Snippet for Creating a Work Item](#Step-1-10-points-Utilizing-the-DevRev-API)
   - *Step 2:*
     - **Clone Work Item Snap-in:**
       - [Manifest and Handler Script](#Snap-in-1-Clone-a-Work-Item)
       - [Instructions and Screenshot](#Instructions-to-Install-and-Use-the-Snap-in)
     - **Auto-Reply Snap-in:**
       - [Manifest and Handler Script](#Snap-in-2-Auto-Reply-to-Messages-Outside-Office-Hours)
       - [Instructions and Screenshot](#Instructions-to-Install-and-Use-the-Snap-in-1)

## Evaluation Criteria

- **Accuracy and completeness of implementation:** The provided code snippets and scripts should work correctly and fulfill the requirements.
- **Clarity and organization of documentation:** The documentation should be clear, organized, and easy to follow.
- **Creativity and innovation in solving the challenges:** The implementation should be creative and solve the given problems efficiently.
- **Adherence to best practices in programming and snap-in development:** The code should follow best practices, be well-structured, and maintainable.