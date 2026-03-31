# ChildLink-MA — Behavioral Simulator

**Public beta v0.1 — April 2026**
Voice-enabled behavioral training simulator for parents of neurodiverse children.
Practice real-life crisis situations · Immediate feedback · ABA/PBS framework · Free & open-source.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Nonprofit](https://img.shields.io/badge/initiative-nonprofit-green)](https://childlink-ma.org)
[![RNA](https://img.shields.io/badge/RNA-W941020510-blue)](https://childlink-ma.org)

---

## Overview

The ChildLink-MA Simulator puts parents in real behavioral situations with an AI-powered child.
You respond — the simulator evaluates your approach and explains what worked and why.

> Training tool only. Does not replace professional support.

**Sister repo:** [ChildLink-MA Assistant](https://github.com/childlink-ma/ChildLink-ma) — RAG clinical Q&A assistant.

---

## Scenarios

17 scenarios across two conditions, 6 UN languages each.

| Condition | Count | Characters |
|---|---|---|
| Autism Spectrum Disorder (ASD) | 8 | Omar, Inès, Tarek |
| Trisomy 21 (T21) | 9 | Lina, Youssef, Maya |

**Clinical frameworks:** ABA · PBS · Myles & Southwick (Rumbling/Rage/Recovery) · NICE NG11 · AAP 2020 · DSM-5

**Languages:** EN · FR · AR · ES · PT · SW

---

## Repo Structure

```
ChildLink-simulator/
├── scenarios/
│   ├── asd/                        # 8 ASD scenario JSON files
│   │   ├── omar_morning_routine.json
│   │   ├── omar_screen_transition.json
│   │   ├── ines_sensory_overload.json
│   │   ├── ines_homework_refusal.json
│   │   ├── tarek_cumulative_disruption.json
│   │   ├── tarek_after_school_collapse.json
│   │   ├── omar_supermarket.json
│   │   └── ines_social_conflict.json
│   └── t21/                        # 9 T21 scenario JSON files
│       ├── lina_morning_routine.json
│       ├── lina_homework_refusal.json
│       ├── youssef_screen_transition.json
│       ├── youssef_social_boundaries.json
│       ├── maya_sensory_overload.json
│       ├── maya_cumulative_disruption.json
│       ├── lina_after_school_collapse.json
│       ├── youssef_supermarket.json
│       └── maya_communication_frustration.json
├── frontend/
│   └── training.html               # Standalone simulator UI (voice-enabled)
├── README.md
├── CONTRIBUTING.md
├── SCENARIO_SCHEMA.md              # JSON schema + authoring guide
├── LICENSE
├── .gitignore
└── .github/
    └── workflows/
        └── validate-scenarios.yml  # CI: validate JSON schema on PR
```

---

## Scenario JSON Schema

Each scenario file follows a strict schema. See [SCENARIO_SCHEMA.md](SCENARIO_SCHEMA.md) for full documentation.

```json
{
  "id": "omar_morning_routine",
  "condition": "ASD",
  "character": "omar",
  "age": 7,
  "level": 1,
  "frameworks": ["ABA", "PBS", "Myles-Southwick"],
  "languages": ["en", "fr", "ar", "es", "pt", "sw"],
  "context": { "en": "...", "fr": "...", "ar": "..." },
  "phases": [
    {
      "phase": "rumbling",
      "child_prompt": { "en": "...", "fr": "..." },
      "good_response_keywords": ["first-then", "visual schedule"],
      "feedback": {
        "good": { "en": "...", "fr": "..." },
        "neutral": { "en": "...", "fr": "..." },
        "poor": { "en": "...", "fr": "..." }
      }
    }
  ]
}
```

---

## Frontend

`frontend/training.html` is a standalone, zero-install browser app.

- Voice-enabled (Azure Speech Services)
- Auto-detects browser language
- Works as iframe in WordPress
- No backend required — connects to ChildLink-MA Assistant API for evaluation

---

## Clinical Validation

All scenarios reviewed against:
- ABA (Applied Behavior Analysis)
- PBS (Positive Behavior Support)
- Myles & Southwick Rumbling/Rage/Recovery framework
- NICE NG11 (2021)
- AAP 2020 guidelines
- DSM-5 criteria

Scenario validator: specialized educator working with neurodivergent children in integrated school settings.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). We especially welcome:
- Specialized educators and behavior analysts (BCBA)
- Translators for the 6 supported languages
- Parents with lived experience for scenario realism review

---

## Performance (v0.1)

| Metric | Value |
|---|---|
| Scenarios | 17 (8 ASD + 9 T21) |
| Languages per scenario | 6 |
| Clinical errors | 0 |
| Hallucination rate | 0% |
| Avg latency | 1.4s |

---

## License

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — Free for non-commercial use, with attribution, same license.

---

## Nonprofit

Led by **Dr. Fatima Azzahra Mastari** under the **ChildLink-MA** nonprofit.
RNA W941020510 · SIRET 989 176 201 00014 · Vitry-sur-Seine, France.

📩 admin@childlink-ma.org · 🌐 childlink-ma.org
