"""Meridian Edge — Prediction Market Consensus SDK"""
import requests

__version__ = "0.1.0"
__all__ = ["MeridianEdge"]


class MeridianEdge:
    BASE_URL = "https://meridianedge.io/api/v1"

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers["X-API-Key"] = api_key

    def _get(self, endpoint, params=None):
        r = self.session.get(f"{self.BASE_URL}/{endpoint}", params=params)
        r.raise_for_status()
        return r.json().get("data", [])

    def consensus(self, sport=None, limit=20, min_spread=None):
        """Get aggregated consensus probabilities.

        Args:
            sport: Filter by sport (NBA, NFL, MLB, NHL, MLS, POLITICS, etc.)
            limit: Max results (default 20, max 100)
            min_spread: Minimum spread filter (e.g. 0.02 for 2%+)

        Returns:
            List of event dicts with consensus_prob, spread, movement, sparkline.
        """
        params = {"limit": limit}
        if sport:
            params["sport"] = sport
        if min_spread:
            params["min_spread"] = min_spread
        return self._get("consensus", params)

    def opportunities(self, sport=None, min_score=5, limit=10):
        """Get divergence opportunities ranked by score.

        Requires Starter tier or above.

        Args:
            sport: Filter by sport
            min_score: Minimum opportunity score (default 5)
            limit: Max results (default 10)

        Returns:
            List of opportunity dicts with score, spread, direction.
        """
        params = {"limit": limit, "min_score": min_score}
        if sport:
            params["sport"] = sport
        return self._get("opportunities", params)

    def signals(self, limit=10):
        """Get recent market signals with direction.

        Args:
            limit: Max results (default 10)

        Returns:
            List of signal dicts with direction and event info.
        """
        return self._get("signals/recent", {"limit": limit})

    def markets(self, sport=None, limit=20):
        """Get active markets list.

        Args:
            sport: Filter by sport
            limit: Max results (default 20)

        Returns:
            List of active market dicts.
        """
        params = {"limit": limit}
        if sport:
            params["sport"] = sport
        return self._get("markets", params)

    def settlements(self, sport=None, limit=10):
        """Get settlement history with verified outcomes.

        Args:
            sport: Filter by sport
            limit: Max results (default 10)

        Returns:
            List of settled event dicts with outcome.
        """
        endpoint = f"settlements/sports/{sport}" if sport else "settlements/recent"
        return self._get(endpoint, {"limit": limit})

    def embed(self, sport=None, limit=5):
        """Get lightweight widget data. No API key required.

        Args:
            sport: Filter by sport
            limit: Max results (default 5, max 10)

        Returns:
            List of event dicts for widget rendering.
        """
        params = {"limit": limit}
        if sport:
            params["sport"] = sport
        return self._get("embed", params)
