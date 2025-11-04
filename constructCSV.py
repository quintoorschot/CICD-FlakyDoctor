#!/usr/bin/env python3
from pathlib import Path
import sys

# import from a sibling file "getTestNames.py"
from getTestNames import get_test_names


def construct_csv(project_name: str, source: str, out_path: str) -> None:
    """
    project_name: repo/project name shown in CSV (e.g., 'test-repo')
    source: path to a test file OR directory (whatever get_test_names accepts)
    out_path: where to write tests.csv that FlakyDoctor will read
    """
    test_names = get_test_names(source)

    # write one row per test (newline INSIDE the loop)
    with open(out_path, "w", encoding="utf-8") as f:
        for test_name in test_names:
            f.write(f"{project_name},,.,{test_name},ID,ID,,,\n")


if __name__ == "__main__":
    # args: [source] [out_path] [project_name]
    # defaults work for your sample project
    src = sys.argv[1] if len(sys.argv) > 1 else "src/test/java/com/example/AppTest.java"
    out = sys.argv[2] if len(sys.argv) > 2 else "tests.csv"
    proj = sys.argv[3] if len(sys.argv) > 3 else Path(".").name
    construct_csv(proj, src, out)
