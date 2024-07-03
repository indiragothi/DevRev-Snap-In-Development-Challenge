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
