# Campaign Model
# Represents a marketing campaign on the Amex website
# Think of it like a form — every campaign has these fields

class Campaign:
    """A marketing campaign for a card portfolio."""

    def __init__(self, campaign_id, card_portfolio, headline, status="draft"):
        self.campaign_id = campaign_id
        self.card_portfolio = card_portfolio
        self.headline = headline
        self.status = status

    def to_dict(self):
        """Convert campaign to a dictionary for API responses."""
        return {
            "campaign_id": self.campaign_id,
            "card_portfolio": self.card_portfolio,
            "headline": self.headline,
            "status": self.status,
        }