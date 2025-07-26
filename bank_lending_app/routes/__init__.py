from flask import Blueprint

# Create blueprints for each route module
lend_bp = Blueprint("lend", __name__)
payment_bp = Blueprint("payment", __name__)
ledger_bp = Blueprint("ledger", __name__)
overview_bp = Blueprint("overview", __name__)

# Import routes to register their endpoints
from . import lend, payment, ledger, overview
