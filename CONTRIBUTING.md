# Contributing to ChildLink-MA Simulator

Thank you for your interest. All contributions must meet our clinical and ethical standards.

---

## Who We Welcome

- Behavior analysts (BCBA) and specialized educators
- Child psychologists and neuropsychologists
- Translators (EN · FR · AR · ES · PT · SW)
- Parents with lived experience (scenario realism review)
- Frontend developers (accessibility, voice UX)

---

## How to Contribute a Scenario

1. Read [SCENARIO_SCHEMA.md](SCENARIO_SCHEMA.md) fully before starting
2. Choose an existing character or propose a new one via Issue first
3. Create your JSON file following the schema exactly
4. Open a Pull Request — CI will validate the schema automatically
5. A clinical reviewer (specialized educator or BCBA) will review content
6. Maintainer merges after approval

```bash
git checkout -b scenario/character-situation
# e.g. scenario/maya-communication-frustration
git add scenarios/t21/maya_communication_frustration.json
git commit -m "feat(scenario): add maya communication frustration T21"
git push origin scenario/character-situation
```

---

## Clinical Rules (non-negotiable)

- No diagnostic statements
- No physical restraint or punishment strategies
- No content that replaces professional consultation
- Every feedback must cite at least one named framework
- All 3 feedback valences required (good / neutral / poor)
- Minimum EN + FR + AR for all text fields

---

## Translation Contributions

If you want to add ES, PT, or SW translations to existing scenarios:
1. Open an Issue listing which scenarios you'll translate
2. Add the missing language keys to the JSON
3. Submit a PR with only translation changes

---

## Bug Reports

Use GitHub Issues. Include: scenario ID, language, expected behavior, actual behavior.

---

## Contact

📩 admin@childlink-ma.org · 🌐 childlink-ma.org
