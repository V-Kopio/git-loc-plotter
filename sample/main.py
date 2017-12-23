import sys
from git_data_collector import extract_diff_summary, branch_history

def main(argv):
    total_lines = 0
    time_list = []
    line_list = []

    for line in branch_history():
        if not line: continue

        if line[0] != ' ':
            commit_id, time = line.strip('\'').split(" ", 1)
        else:
            data = extract_diff_summary(line)

            total_lines += data['insertions'] - data['deletions']

            time_list.append(time)
            line_list.append(total_lines)

            print "%s, %s: %d lines" % (commit_id, time, total_lines)

if __name__ == '__main__':
	sys.exit(main(sys.argv))
