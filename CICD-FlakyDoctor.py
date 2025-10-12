from constructCSV import constructCSV
import subprocess
import os
import sys

if __name__ == "__main__":
    constructCSV()

    flakydoctor_path = "/home/q/Documents/new/FlakyDoctor-CICD/FlakyDoctor/src/run_FlakyDoctor.sh"

    if not os.getenv("OPENAI_API_KEY"):
        print("[ERROR]: OPEN_API_KEY not set in the environment!")
        sys.exit(1)

    openai_key = os.getenv("OPENAI_API_KEY")
    input_csv = "/home/q/Documents/new/FlakyDoctor-CICD/tests.csv"

    subprocess.run(["bash", flakydoctor_path, "/home/q/Documents/new/", openai_key, "GPT-4", "results", input_csv, "ID"]) 