from flask import jsonify, request
from models import Loan, Payment
from routes import ledger_bp

@ledger_bp.route("/ledger/<int:loan_id>", methods=["GET"])
def get_ledger(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    ledger = [{"amount": p.amount, "date": p.payment_date.isoformat()} for p in loan.payments]
    return jsonify({"loan_id": loan.id, "ledger": ledger})