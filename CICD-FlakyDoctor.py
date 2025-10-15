# CICD-FlakyDoctor.py
from pathlib import Path
import os, sys, subprocess, re
from constructCSV import constructCSV

if __name__ == "__main__":
    constructCSV()

    workspace = Path(os.environ.get("GITHUB_WORKSPACE", Path(__file__).resolve().parents[1]))
    fd_root = workspace / "CICD-FlakyDoctor"
    flakydoctor_path = fd_root / "FlakyDoctor" / "src" / "run_FlakyDoctor.sh"
    input_csv = fd_root / "tests.csv"

    if not flakydoctor_path.exists():
        print(f"[ERROR] run_FlakyDoctor.sh not found at: {flakydoctor_path}")
        sys.exit(1)

    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("[ERROR] OPENAI_API_KEY not set in the environment!")
        sys.exit(1)

    flakydoctor_path.chmod(0o755)

    # 🔧 add '/results' so nested folder ends up inside this one
    safe_name = re.sub(r'[/\\: ]+', '_', workspace.name)
    output_path = workspace / "CICD-FlakyDoctor" / f"ID_Results_GPT-4_{safe_name}" / "results"
    output_path.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        ["bash", str(flakydoctor_path), str(workspace), openai_key, "GPT-4", str(output_path), str(input_csv), "ID"],
        check=True,
        cwd=str(workspace),
    )

    print(f"[INFO] Results saved in: {output_path}")
