# CICD-FlakyDoctor.py
from pathlib import Path
import os, sys, subprocess, re
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

    # Sanitize workspace path for output folder
    safe_name = re.sub(r'[/\\: ]+', '_', str(workspace.name))
    output_dir = workspace / "results" / f"ID_Results_GPT-4_{safe_name}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Ensure the script is executable
    flakydoctor_path.chmod(0o755)

    # Run FlakyDoctor with cleaned output path
    subprocess.run(
        ["bash", str(flakydoctor_path), str(workspace), openai_key, "GPT-4", str(output_dir), str(input_csv), "ID"],
        check=True,
        cwd=str(workspace),
    )

    print(f"[INFO] Results saved in: {output_dir}")
