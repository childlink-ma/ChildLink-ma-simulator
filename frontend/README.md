# frontend/

| File | Description |
|---|---|
| `training.html` | Standalone simulator UI — voice-enabled, 6 languages, zero install |

## Usage

Served statically or embedded as iframe in WordPress.
Loads scenarios from `../scenarios/` via the ChildLink-MA Assistant API.

## ENV dependency

Update the `API_URL` constant at the top of `training.html` if the backend URL changes.
