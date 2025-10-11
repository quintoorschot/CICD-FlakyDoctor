#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: $0 <project_dir>"
    exit 1
fi

project_dir=$1
logs_dir="$(pwd)/logs"
mkdir -p "$logs_dir"

(
    cd "$project_dir"

    echo "[INFO] Detecting order-dependent flaky tests..."
    mvn edu.illinois.cs:idflakies-maven-plugin:2.0.0:detect \
        -Ddetector.detector_type=random-class-method \
        -Ddt.randomize.rounds=10 \
        -Ddt.detector.original_order.all_must_pass=false \
        > "$logs_dir/mvn_detect.log" 2>&1

    echo "[INFO] Identifying minimal polluter-victim pairs..."
    mvn edu.illinois.cs:idflakies-maven-plugin:2.0.1-SNAPSHOT:minimize \
        > "$logs_dir/mvn_minimize.log" 2>&1

    find .dtfixingtools/minimized -maxdepth 1 -type f -name '*.json' -print0 \
        | xargs -0 -I{} jq -r '
            .dependentTest as $victim
            | .polluters[].deps[]
            | [. , $victim]     # (polluter, victim)
            | @tsv
            ' {} \
        | sort -u > ../pairs.tsv
    echo "[SUCCESS] Polluter-victim pairs succesfully stored!"

    echo "[INFO] Removing temporary files from project..."
    rm -rf .dtfixingtools
    echo "[SUCCESS] Removed temporary files!"
)

echo "[RESULT] Output logs can be found at: $logs_dir"
echo "[RESULT] Polluter-victim pairs can be found at: $(pwd)/pairs.tsv"