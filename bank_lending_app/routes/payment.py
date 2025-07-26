from flask import request, jsonify
from datetime import date
from models import Payment, Loan
from app import db
from routes import payment_bp

@payment_bp.route("/pay", methods=["POST"])
def make_payment():
    data = request.get_json()
    payment = Payment(
        loan_id=data["loan_id"],
        amount=data["amount"],
        payment_date=date.today()
    )
    db.session.add(payment)
    db.session.commit()
    return jsonify({"message": "Payment recorded"}), 201