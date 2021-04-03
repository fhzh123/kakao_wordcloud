def time_return(time_text):
    if time_text[:2] == '오전':
        hour, minute = time_text[2:].split(':')
        hour = int(hour)
        minute = int(minute)
    elif time_text[:2] == '오후':
        hour, minute = time_text[2:].split(':')
        hour = int(hour) + 12
        minute = int(minute)
    else:
        print(time_text)
    return int(hour), int(minute)