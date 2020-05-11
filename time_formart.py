import datetime 

def get_time_stamp():
    now=datetime.datetime.now()
    # YYYYMMDDHHmmss
    time_stamp=datetime.datetime.strftime(now,"%Y%m%d%H%M%S")
    print(time_stamp)
    return time_stamp

