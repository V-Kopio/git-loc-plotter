import sys
from datetime import datetime
from git_data_collector import extract_diff_summary, branch_history
from plotter import plot_with_date

def main(argv):
    total_lines = 0
    history_list = []

    for line in branch_history():
        if not line: continue

        if line[0] != ' ':
            commit_id, time = line.strip('\'').split(" ", 1)
        else:
            data = extract_diff_summary(line)

            total_lines += data['insertions'] - data['deletions']

            history_list.append(
                (datetime.fromtimestamp(float(time)), total_lines)
            )

    history_list.sort(key=lambda tup: tup[0])

    time_list, line_list = zip(*history_list)

    plot_with_date(time_list, line_list)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
