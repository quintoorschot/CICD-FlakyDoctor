from pathlib import Path
import os, sys, subprocess, re

if __name__ == "__main__":

    workspace = Path(os.environ.get("GITHUB_WORKSPACE", Path(__file__).resolve().parents[1]))
    fd_root = workspace / "CICD-FlakyDoctor"
    flakydoctor_path = fd_root / "FlakyDoctor" / "src" / "run_FlakyDoctor.sh"
    input_csv = fd_root / "tests.csv"

    tool_cwd = fd_root / "FlakyDoctor"

    if not flakydoctor_path.exists():
        print(f"[ERROR] run_FlakyDoctor.sh not found at: {flakydoctor_path}")
        sys.exit(1)

    openai_key = os.getenv("OPENAI_API_KEY")
    if not openai_key:
        print("[ERROR] OPENAI_API_KEY not set in the environment!")
        sys.exit(1)

    flakydoctor_path.chmod(0o755)

    safe_name = re.sub(r'[/\\: ]+', '_', workspace.name)
    output_path = workspace / "CICD-FlakyDoctor" / f"ID_Results_GPT-4_{safe_name}" / "results"
    output_path.mkdir(parents=True, exist_ok=True)

    projects_root = workspace.parent

    print(
        f"bash {flakydoctor_path} {projects_root} <OPENAI_API_KEY> GPT-4 "
        f"{output_path} {input_csv} ID"
    )

    # print("IMPORTANT ================")
    # import javalang
    # from javalang import tree
    # src = open("/home/q/Documents/new/test-repo/src/test/java/com/example/AppTest.java").read()
    # cu = javalang.parse.parse(src)
    # for cls in cu.types:
    #     for m in cls.methods:
    #         print(m.name, "start:", getattr(m, "start_position", None), "end:", getattr(m, "end_position", None))

    try:
        subprocess.run(
            ["bash", str(flakydoctor_path),
            str(projects_root),
            openai_key,
            "GPT-4",
            str(output_path),
            str(input_csv),
            "ID"],
            check=True,
            cwd=str(tool_cwd),
            stdout=sys.stdout,
            stderr=sys.stderr,
        )
    except Exception as e:
        print(f"::error::FlakyDoctor GPT-4 run failed: {e}", flush=True)
        raise

    print(f"[INFO] Results saved in: {output_path}")
