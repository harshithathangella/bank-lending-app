from flask import jsonify
from models import Loan
from routes import overview_bp

@overview_bp.route("/overview", methods=["GET"])
def overview():
    loans = Loan.query.all()
    overview_data = [
        {
            "id": loan.id,
            "customer_name": loan.customer_name,
            "principal": loan.principal,
            "interest_rate": loan.interest_rate,
            "term_months": loan.term_months,
            "emi": loan.emi,
        }
        for loan in loans
    ]
    return jsonify(overview_data)