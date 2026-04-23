# Campaign Routes
# These are the "menu items" the website can order from our API
# Each route is a URL the website can call

from flask import Blueprint, jsonify
from src.models import Campaign

campaigns_bp = Blueprint("campaigns", __name__)

# This is our fake database — just a list of campaigns
# At real Amex this would connect to an actual database
CAMPAIGNS = [
    Campaign("MKT-001", "Platinum", "Earn 150K points with the Platinum Card", "live"),
    Campaign("MKT-002", "Delta", "Fly further with Delta SkyMiles", "live"),
    Campaign("MKT-003", "Hilton", "Earn a free night at any Hilton property", "in_review"),
    Campaign("MKT-004", "Platinum", "The Platinum Card: Built for Travel", "draft"),
    Campaign("MKT-005", "Delta", "Delta SkyMiles Gold: No Annual Fee", "live"),
]


@campaigns_bp.route("/api/campaigns", methods=["GET"])
def get_all_campaigns():
    """The website asks: 'Give me all campaigns.'"""
    return jsonify([c.to_dict() for c in CAMPAIGNS])


@campaigns_bp.route("/api/campaigns/<campaign_id>", methods=["GET"])
def get_campaign(campaign_id):
    """The website asks: 'Give me one specific campaign.'"""
    for campaign in CAMPAIGNS:
        if campaign.campaign_id == campaign_id:
            return jsonify(campaign.to_dict())
    return jsonify({"error": "Campaign not found"}), 404