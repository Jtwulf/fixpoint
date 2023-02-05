# あとは，同じサブネット内のサーバが全て故障している期間を求めて出力出来るように

from datetime import datetime, timedelta
import socket


# 確認日時を文字列から時間に変換する
def parse_time(time):
    return datetime.strptime(time, "%Y%m%d%H%M%S")


# 監視ログの各行をカンマ区切りで要素を分解する
def parse_log(log):
    return log.strip().split(',')


def calculate_downtime(server_downtime, n):
    downtime = {}
    for server, server_times in server_downtime.items():
        for time in server_times:
            if server not in downtime:
                downtime[server] = []
            downtime[server].append(time)
        if server in downtime and len(downtime[server]) >= n:
            start = downtime[server][0]
            end = downtime[server][-1]
            print(f"{server} was down from {start} to {end}")


def get_subnet(server):
    subnet = server.split("/")[0]
    subnet = ".".join(subnet.split(".")[:3])
    return subnet


def main():
    N = 3
    log_file = "log/ping1.log"
    server_downtime = {}
    subnet_downtime = {}
    with open() as f:
        log_lines = f.readlines()
        for line in log_lines:
            date_str, server, response = parse_log(line)
            date = parse_time(date_str)
            if response == '-':
                if server not in server_downtime:
                    server_downtime[server] = []
                server_downtime[server].append(date)
            else:
                if server in server_downtime and len(server_downtime[server]) >= N:
                    subnet = get_subnet(server)
                    if subnet not in subnet_downtime:
                        subnet_downtime[subnet] = {}
                    subnet_downtime[subnet][server] = server_downtime[server]
                server_downtime[server] = []
        for subnet, subnet_servers in subnet_downtime.items():
            print(f"Subnet {subnet} was down:")
            calculate_downtime(subnet_servers, N)


if __name__ == '__main__':
    main()
