#!/usr/bin/env python3
"""
Creates placeholder JSON files for the 16 remaining scenarios.
Run once locally: python create_placeholders.py
"""
import json, os

scenarios = [
    ("asd", "omar_screen_transition"),
    ("asd", "ines_sensory_overload"),
    ("asd", "ines_homework_refusal"),
    ("asd", "tarek_cumulative_disruption"),
    ("asd", "tarek_after_school_collapse"),
    ("asd", "omar_supermarket"),
    ("asd", "ines_social_conflict"),
    ("t21", "lina_morning_routine"),
    ("t21", "lina_homework_refusal"),
    ("t21", "youssef_screen_transition"),
    ("t21", "youssef_social_boundaries"),
    ("t21", "maya_sensory_overload"),
    ("t21", "maya_cumulative_disruption"),
    ("t21", "lina_after_school_collapse"),
    ("t21", "youssef_supermarket"),
    ("t21", "maya_communication_frustration"),
]

template = {
    "id": "",
    "condition": "",
    "character": "",
    "age": 0,
    "level": 1,
    "frameworks": ["ABA", "PBS", "Myles-Southwick"],
    "languages": ["en", "fr", "ar", "es", "pt", "sw"],
    "context": {"en": "TODO", "fr": "TODO", "ar": "TODO", "es": "TODO", "pt": "TODO", "sw": "TODO"},
    "phases": [
        {
            "phase": "rumbling",
            "child_prompt": {"en": "TODO", "fr": "TODO", "ar": "TODO", "es": "TODO", "pt": "TODO", "sw": "TODO"},
            "good_response_keywords": [],
            "feedback": {
                "good": {"en": "TODO", "fr": "TODO", "ar": "TODO"},
                "neutral": {"en": "TODO", "fr": "TODO", "ar": "TODO"},
                "poor": {"en": "TODO", "fr": "TODO", "ar": "TODO"}
            }
        }
    ],
    "references": ["NICE NG11, 2021", "AAP, 2020"],
    "validated_by": "PENDING",
    "version": "0.1-draft",
    "last_updated": "2026-03-31"
}

for condition, scenario_id in scenarios:
    character = scenario_id.split("_")[0]
    t = dict(template)
    t["id"] = scenario_id
    t["condition"] = condition.upper()
    t["character"] = character
    path = f"scenarios/{condition}/{scenario_id}.json"
    os.makedirs(f"scenarios/{condition}", exist_ok=True)
    with open(path, "w") as f:
        json.dump(t, f, indent=2, ensure_ascii=False)
    print(f"Created: {path}")

print(f"\nDone. {len(scenarios)} placeholder files created.")
