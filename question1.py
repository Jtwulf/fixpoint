from datetime import datetime, timedelta


# 確認日時を文字列から時間に変換する
def parse_time(time):
    return datetime.strptime(time, "%Y%m%d%H%M%S")


# 監視ログの各行をカンマ区切りで要素を分解する
def parse_log(log):
    return log.strip().split(',')


# 故障期間を求めて出力するプログラム
def calculate_downtime(log_lines):
    downtime = {}
    for line in log_lines:
        date_str, server, response = parse_log(line)
        date = parse_time(date_str)
        if response == '-':
            if server not in downtime:
                downtime[server] = []
            downtime[server].append(date)
        else:
            if server in downtime and len(downtime[server]) >= 1:
                start = downtime[server][0]
                end = date
                print(f"{server} was down from {start} to {end}")
            downtime[server] = []


def main():
    for i in range(8):
        log_file = f"log/ping{i+1}.log"
        print(f"ping{i+1}.log:")
        with open(log_file) as f:
            log_lines = f.readlines()
            calculate_downtime(log_lines)
        print()


if __name__ == '__main__':
    main()
