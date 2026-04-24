# Amex Marketing Content API

A simple Flask REST API that serves marketing campaign data. Built as a learning project to practice Flask blueprints, query-parameter filtering, and pytest.

## What it does

Exposes a read-only HTTP API for browsing marketing campaigns associated with Amex card portfolios (Platinum, Delta, Hilton, etc.). Campaigns are currently stored in an in-memory list — no database is required.

## Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/api/campaigns` | List all campaigns |
| GET | `/api/campaigns?portfolio=<name>` | List campaigns filtered by portfolio (e.g. `Platinum`, `Delta`) |
| GET | `/api/campaigns/<campaign_id>` | Fetch a single campaign by ID (e.g. `MKT-001`) |

Each campaign has the shape:

```json
{
  "campaign_id": "MKT-001",
  "card_portfolio": "Platinum",
  "headline": "Earn 150K points with the Platinum Card",
  "status": "live"
}
```

`status` is one of `live`, `in_review`, or `draft`.

## Getting started

Requires Python 3.10+.

```bash
# clone
git clone https://github.com/keshavgb/amex-marketing-api.git
cd amex-marketing-api

# create + activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the API
python run.py
```

The server starts on `http://127.0.0.1:5000`.

### Try it

```bash
curl http://127.0.0.1:5000/api/campaigns
curl http://127.0.0.1:5000/api/campaigns?portfolio=Delta
curl http://127.0.0.1:5000/api/campaigns/MKT-001
```

## Running tests

```bash
pytest
```

## Project structure

```
amex-marketing-api/
├── run.py                 # Entry point for local development
├── requirements.txt       # Python dependencies
├── src/
│   ├── app.py             # Flask app factory (create_app)
│   ├── routes.py          # Campaign endpoints (Blueprint)
│   └── models.py          # Campaign model
└── tests/
    └── test_routes.py     # Endpoint tests
```

## Notes

- Data is hardcoded in `src/routes.py` as a Python list; it resets on every restart. A real implementation would read from a database.
- The API is read-only for now — no POST/PUT/DELETE endpoints.
- The `portfolio` filter is an exact, case-sensitive match.
