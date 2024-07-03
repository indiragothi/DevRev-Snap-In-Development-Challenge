### Snap-in 2: Auto-Reply to Messages Outside Office Hours 

## Instructions to Install and Use the Snap-in:

1. Place the manifest.yaml and auto_reply.py files in your snap-in directory.
2. Use the DevRev CLI to install the snap-in:
   ```bash
   devrev snap-in install /path/to/snap-in-directory
   ```
   
3. Configure the snap-in inputs and execute:
   ```bash
   devrev snap-in execute auto-reply --inputs '{"start_time": "09:00", "end_time": "17:00", "auto_reply_message": "Our office is currently closed. We will get back to you during office hours."}'
   ```
   

## Screenshot/Demonstration: 

![Auto-Reply Snap-in Demonstration](https://your-screenshot-url.com)