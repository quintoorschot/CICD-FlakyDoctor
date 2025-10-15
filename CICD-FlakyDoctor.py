# CICD-FlakyDoctor.py
from pathlib import Path
import os, sys, subprocess
from constructCSV import constructCSV

if __name__ == "__main__":
    constructCSV()

    # Workspace root (fallback to repo root via file location)
    workspace = Path(os.environ.get("GITHUB_WORKSPACE", Path(__file__).resolve().parents[1]))

    fd_root = workspace / "CICD-FlakyDoctor"
    flakydoctor_path = fd_root / "FlakyDoctor" / "src" / "run_FlakyDoctor.sh"
    input_csv = fd_root / "tests.csv"           # adjust if you want the other tests.csv

    if not flakydoctor_path.exists():
        print(f"[ERROR] run_FlakyDoctor.sh not found at: {flakydoctor_path}")
        sys.exit(1)

    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("[ERROR] OPENAI_API_KEY not set in the environment!")
        sys.exit(1)

    # Ensure the script is executable
    flakydoctor_path.chmod(0o755)

    # Pass the project path explicitly and set cwd
    subprocess.run(
        ["bash", str(flakydoctor_path), str(workspace), openai_key, "GPT-4", "results", str(input_csv), "ID"],
        check=True,
        cwd=str(workspace),
    )
