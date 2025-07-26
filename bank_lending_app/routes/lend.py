from flask import Blueprint, request, jsonify
from ..models import db, Loan
from ..utils import calculate_emi

lend_bp = Blueprint("lend", __name__)

@lend_bp.route("/lend", methods=["POST"])
def lend_money():
    data = request.get_json()
    loan = Loan(
        customer_name=data["customer_name"],
        principal=data["principal"],
        interest_rate=data["interest_rate"],
        term_months=data["term_months"],
        emi=calculate_emi(
            data["principal"],
            data["interest_rate"],
            data["term_months"]
        )
    )
    db.session.add(loan)
    db.session.commit()
    return jsonify({"message": "Loan issued", "emi": loan.emi}), 201

@lend_bp.route("/")
def home():
    return "🏦 Bank Lending App is Running!"
