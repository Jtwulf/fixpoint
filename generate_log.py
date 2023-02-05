import random
import time
from datetime import datetime, timedelta


def generate_logs():
    logs = []
    servers = ["10.20.30.{}/16".format(i) for i in range(1, 3)] + ["192.168.1.{}/24".format(i) for i in range(1, 3)]
    curr_time = datetime(2020, 10, 19, 13, 0, 0)
    end_time = datetime(2020, 10, 19, 14, 0, 0)
    while curr_time <= end_time:
        server = random.choice(servers)
        if random.random() < 0.8:
            logs.append("{},{},-".format(curr_time.strftime("%Y%m%d%H%M%S"), server))
        else:
            logs.append("{},{},{}".format(curr_time.strftime("%Y%m%d%H%M%S"), server, random.randint(1, 100)))
        curr_time += timedelta(seconds=random.randint(1, 15))
    return logs


def main():
    logs = generate_logs()
    for log in logs:
        print(log)


if __name__ == '__main__':
    main()
