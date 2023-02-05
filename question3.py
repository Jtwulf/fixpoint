from datetime import datetime, timedelta


# 確認日時を文字列から時間に変換する
def parse_time(time):
    return datetime.strptime(time, "%Y%m%d%H%M%S")


# 監視ログの各行をカンマ区切りで要素を分解する
def parse_log(log):
    return log.strip().split(',')


# 過負荷状態期間を求めて出力する
def calculate_overtime(log_lines, m, t):
    overtime = {}
    response_times = {}
    dates = {}
    for line in log_lines:
        date_str, server, response = parse_log(line)
        date = parse_time(date_str)
        if response == '-':
            continue
        response = int(response)
        if server not in response_times:
            response_times[server] = []
            dates[server] = []
        response_times[server].append(response)
        dates[server].append(date)
        if len(response_times[server]) > m:
            response_times[server].pop(0)
            dates[server].pop(0)
        avg_response_time = sum(response_times[server]) / len(response_times[server])
        if avg_response_time > t and len(response_times[server]) >= m:
            start = dates[server][0]
            end = dates[server][len(dates[server])-1]
            print(f"{server} was in overload state from {start} to {end}")


def main():
    m = 3
    t = 100
    print("m =", m)
    print("t =", t, "\n")
    for i in range(8):
        log_file = f"log/ping{i+1}.log"
        print(f"ping{i+1}.log:")
        with open(log_file) as f:
            log_lines = f.readlines()
            calculate_overtime(log_lines, m, t)
        print()


if __name__ == '__main__':
    main()
