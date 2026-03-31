"""
validate_scenarios.py
Validates all scenario JSON files against the required schema.
Run: python .github/scripts/validate_scenarios.py
"""

import json
import sys
from pathlib import Path

REQUIRED_TOP = ["id", "condition", "character", "age", "level",
                "frameworks", "languages", "context", "phases",
                "references", "validated_by", "version", "last_updated"]

REQUIRED_PHASE = ["phase", "child_prompt", "good_response_keywords", "feedback"]
REQUIRED_FEEDBACK = ["good", "neutral", "poor"]
VALID_CONDITIONS = {"ASD", "T21"}
VALID_CHARACTERS = {"omar", "ines", "tarek", "lina", "youssef", "maya"}
VALID_PHASES = {"rumbling", "rage", "recovery"}
REQUIRED_LANGUAGES = {"en", "fr", "ar"}

errors = []
files_checked = 0

for path in sorted(Path("scenarios").rglob("*.json")):
    files_checked += 1
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"{path}: Invalid JSON — {e}")
        continue

    # Top-level fields
    for field in REQUIRED_TOP:
        if field not in data:
            errors.append(f"{path}: Missing field '{field}'")

    # Condition
    if data.get("condition") not in VALID_CONDITIONS:
        errors.append(f"{path}: Invalid condition '{data.get('condition')}' — must be ASD or T21")

    # Character
    if data.get("character") not in VALID_CHARACTERS:
        errors.append(f"{path}: Invalid character '{data.get('character')}'")

    # Context languages
    context = data.get("context", {})
    for lang in REQUIRED_LANGUAGES:
        if lang not in context:
            errors.append(f"{path}: Missing context language '{lang}'")

    # Phases
    phases = data.get("phases", [])
    if not phases:
        errors.append(f"{path}: 'phases' is empty")

    for i, phase in enumerate(phases):
        for field in REQUIRED_PHASE:
            if field not in phase:
                errors.append(f"{path}: Phase {i} missing field '{field}'")

        if phase.get("phase") not in VALID_PHASES:
            errors.append(f"{path}: Phase {i} invalid phase value '{phase.get('phase')}'")

        # child_prompt languages
        prompt = phase.get("child_prompt", {})
        for lang in REQUIRED_LANGUAGES:
            if lang not in prompt:
                errors.append(f"{path}: Phase {i} child_prompt missing language '{lang}'")

        # feedback
        feedback = phase.get("feedback", {})
        for valence in REQUIRED_FEEDBACK:
            if valence not in feedback:
                errors.append(f"{path}: Phase {i} feedback missing valence '{valence}'")
            else:
                for lang in REQUIRED_LANGUAGES:
                    if lang not in feedback[valence]:
                        errors.append(f"{path}: Phase {i} feedback.{valence} missing language '{lang}'")

print(f"\nChecked {files_checked} scenario file(s)")

if errors:
    print(f"\n{len(errors)} error(s) found:\n")
    for e in errors:
        print(f"  ✗ {e}")
    sys.exit(1)
else:
    print("All scenarios valid ✓")
    sys.exit(0)
