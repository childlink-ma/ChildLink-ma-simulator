# Scenario Schema & Authoring Guide

This document defines the JSON structure for all ChildLink-MA simulator scenarios
and provides guidelines for creating new ones.

---

## File Naming

```
scenarios/{condition}/{character}_{situation}.json
```

Examples:
- `scenarios/asd/omar_morning_routine.json`
- `scenarios/t21/lina_homework_refusal.json`

---

## Full JSON Schema

```json
{
  "id": "string — unique, snake_case, matches filename without .json",
  "condition": "ASD | T21",
  "character": "omar | ines | tarek | lina | youssef | maya",
  "age": "integer — character age in years",
  "level": "1 | 2 (1 = beginner, 2 = advanced)",
  "frameworks": ["ABA", "PBS", "Myles-Southwick", "NICE-NG11", "AAP-2020"],
  "languages": ["en", "fr", "ar", "es", "pt", "sw"],
  "context": {
    "en": "Situation description in English (2-4 sentences max)",
    "fr": "...",
    "ar": "...",
    "es": "...",
    "pt": "...",
    "sw": "..."
  },
  "phases": [
    {
      "phase": "rumbling | rage | recovery",
      "child_prompt": {
        "en": "What the child says or does (1-2 sentences)",
        "fr": "...",
        "ar": "...",
        "es": "...",
        "pt": "...",
        "sw": "..."
      },
      "good_response_keywords": [
        "list of strategy keywords that indicate a good parental response"
      ],
      "feedback": {
        "good": {
          "en": "Positive feedback explaining why this approach works (2-3 sentences)",
          "fr": "...",
          "ar": "...",
          "es": "...",
          "pt": "...",
          "sw": "..."
        },
        "neutral": {
          "en": "Neutral feedback — approach is acceptable but not optimal",
          "fr": "...",
          "ar": "..."
        },
        "poor": {
          "en": "Corrective feedback — explains what to avoid and why",
          "fr": "...",
          "ar": "..."
        }
      }
    }
  ],
  "references": [
    "NICE NG11, 2021",
    "AAP, 2020"
  ],
  "validated_by": "string — validator role (e.g. 'Specialized educator, integrated school settings')",
  "version": "string — e.g. '1.0'",
  "last_updated": "YYYY-MM-DD"
}
```

---

## Characters

| Character | Condition | Age | Profile |
|---|---|---|---|
| Omar | ASD | 7 | Level 1-2, verbal, school-age |
| Inès | ASD | 9 | Level 1, verbal, school-age |
| Tarek | ASD | 6 | Level 2, limited verbal |
| Lina | T21 | 8 | Verbal, school-age |
| Youssef | T21 | 10 | Verbal, school-age |
| Maya | T21 | 7 | Limited verbal |

---

## Phases (Myles & Southwick)

| Phase | Description | Parent goal |
|---|---|---|
| `rumbling` | Early warning signs — child is escalating | De-escalate, prevent |
| `rage` | Peak crisis — meltdown or shutdown | Safety, reduce stimuli |
| `recovery` | Calming down — child is fragile | Reconnect, no debriefing yet |

---

## Clinical Rules

- **Never** include content that diagnoses, prescribes, or replaces professional advice
- **Never** suggest physical restraint or punishment
- **Always** ground feedback in at least one named framework
- **Always** provide feedback in all 3 valences (good / neutral / poor)
- Keep child prompts realistic — based on documented behavioral presentations
- Keep feedback under 60 words per valence

---

## Validation Process

1. Author submits PR with new scenario JSON
2. CI validates JSON schema automatically (`validate-scenarios.yml`)
3. Clinical reviewer (specialized educator or BCBA) reviews content
4. Maintainer merges after approval

---

## Languages

All 6 languages required for `context` and `child_prompt`.
Feedback (`good`, `neutral`, `poor`) requires minimum EN + FR + AR.
ES, PT, SW feedback accepted as contributions.
