# Meridian Edge — Prediction Market Consensus SDK

Real-time consensus probabilities aggregated from multiple regulated prediction markets. One API, one number per event.

## Install

```bash
pip install meridianedge
```

## Try This Now

```python
from meridianedge import MeridianEdge

me = MeridianEdge()  # Free — no key needed for demo

# What do prediction markets think about tonight's games?
for event in me.consensus(sport="NBA", limit=3):
    print(f"{event['event_name']}")
    print(f"  Consensus: {event['consensus_prob']:.0%}")
    print(f"  Sources: {event['n_platforms']} regulated markets")
    print(f"  Confidence: {event['confidence']}")
    print()
```

Output:
```
Lakers vs Celtics
  Consensus: 62%
  Sources: 5 regulated markets
  Confidence: HIGH

Nuggets vs Warriors
  Consensus: 54%
  Sources: 4 regulated markets
  Confidence: MEDIUM
```

Get your free API key at [meridianedge.io](https://meridianedge.io) — no credit card, 100 calls/day.

## Quick Start

```python
from meridianedge import MeridianEdge

me = MeridianEdge(api_key="YOUR_KEY")  # Free key at meridianedge.io

# Get consensus for all NBA events
events = me.consensus(sport="NBA")
for e in events:
    print(f"{e['event_name']}: {e['consensus_prob']:.1%}")

# Get divergence opportunities
opps = me.opportunities(min_score=5)

# Get recent market signals
signals = me.signals()
```

## Free API Key

Get one instantly at [meridianedge.io](https://meridianedge.io) — no credit card required.

- Free: 100 calls/day
- Starter ($29/mo): 500 calls/day + opportunities + signals
- Pro ($99/mo): 5,000 calls/day + fair value + platform breakdown
- [Full pricing](https://meridianedge.io/#pricing)

## Endpoints

| Method | Description |
|--------|-------------|
| `consensus()` | Aggregated consensus probabilities with spread + movement |
| `opportunities()` | Divergence opportunities ranked by score |
| `signals()` | Recent market signals with direction |
| `markets()` | Active markets list |
| `settlements()` | Settlement history with verified outcomes |
| `embed()` | Lightweight widget data (no auth required) |

## Examples

### NBA win probabilities

```python
from meridianedge import MeridianEdge

me = MeridianEdge(api_key="me_free_demo000000000000")

nba = me.consensus(sport="NBA", limit=5)
for game in nba:
    prob = game["consensus_prob"]
    name = game["event_key"]
    move = game.get("movement", "stable")
    print(f"{name}: {prob:.1%}  ({move})")
```

### Find high-divergence markets

```python
# Markets where platforms disagree most
opps = me.opportunities(min_score=5, limit=10)
for o in opps:
    print(f"{o['event_key']}: score={o.get('score')}, spread={o.get('spread'):.1%}")
```

### Embed widget data (no auth)

```python
me = MeridianEdge()  # no key needed for embed
data = me.embed(sport="NHL", limit=3)
for item in data:
    print(f"{item['event_key']}: {item['consensus_prob']:.1%}")
```

## Response Format

Every `consensus()` response item includes:

| Field | Type | Description |
|-------|------|-------------|
| `event_key` | string | Unique event identifier |
| `event_name` | string | Human-readable name |
| `sport` | string | Sport or category |
| `consensus_prob` | float | Aggregated probability (0.0–1.0) |
| `confidence` | string | LOW / MEDIUM / HIGH |
| `spread` | float | Spread between highest and lowest market |
| `movement` | string | `up`, `down`, or `stable` vs 30 min ago |
| `movement_pct` | float | % change over last 30 minutes |
| `sparkline` | array | 6 recent values for trend visualization |
| `ts` | string | ISO 8601 timestamp |

## AI Platform Integrations

Use Meridian Edge consensus data directly inside major AI platforms — no code required:

| Platform | Link | Notes |
|----------|------|-------|
| **ChatGPT** | [Open Custom GPT](https://chatgpt.com/g/g-69c5cf29be388191aeaaf3159cd41697-prediction-market-consensus) | No setup — just open and ask |
| **Claude** | [MCP install guide](https://github.com/meridian-edge/meridian-edge-mcp) | Claude Desktop / Cursor via MCP |
| **Gemini** | [Open Gem](https://gemini.google.com/gem/1aSpfo0atq00TWFEjDJLytxzsnqTdqHjJ) | No setup — just open and ask |

---

## Links

- [Dashboard](https://meridianedge.io/dashboard.html) — free, no signup
- [API Docs](https://meridianedge.io/docs.html)
- [AI Integrations](https://meridianedge.io/agents.html)
- [Widget](https://meridianedge.io/widget.html) — embeddable, free

## Data Coverage

- **Sports:** NBA, NFL, MLB, NHL, MLS, college sports, boxing
- **Politics:** US elections, ballot measures, appointment markets
- **Economics:** Federal Reserve rate decisions, macro indicator markets
- **Update frequency:** Every 10 minutes during active market hours

*For informational purposes only. Not investment advice.*

## License

MIT
