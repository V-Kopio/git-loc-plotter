import subprocess
import re

def extract_diff_summary(string):
    regex_matches = re.match(
        r"( (?P<files>\d+) files? changed)"
        r"(, (?P<insertions>\d+) insertions?\(\+\))?"
        r"(, (?P<deletions>\d+) deletions?\(-\))?",
        string
    )

    details = regex_matches.groupdict()

    for detail in details:
        details[detail] = int(details[detail]) if details[detail] else 0

    return details

def branch_history():
    git = subprocess.Popen(
        ["git", "log", "--shortstat", "--reverse", "--pretty=format:'%H %at'"],
        stdout=subprocess.PIPE
    )

    out, _ = git.communicate()
    return out.split('\n')
