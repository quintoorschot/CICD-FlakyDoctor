from getTestNames import get_test_names

def constructCSV():
    project_name = "test-repo"
    test_names = get_test_names("/home/q/Documents/new/test-repo/src/test/java/com/example/AppTest.java")

    with open("tests.csv", "w") as f:
        for test_name in test_names:
            f.write(f"{project_name},,.,{test_name},ID,ID,,,")
        f.write("\n")