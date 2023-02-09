from flask import Blueprint, jsonify, abort, request
from flask_login import login_required
from models import Member, db

member_routes = Blueprint('members', __name__)
# @login_required
@member_routes.route('/', methods=['GET'])
def members():
    members = Member.query.all()
    return jsonify({'members': [member.to_dict() for member in members]})

@member_routes.route('/', methods=['POST'])
def create_member():
    # add validations
    new_member = Member(**request.form)
    db.session.add(new_member)
    db.session.commit()
    return "Member created successfully!"

"""
@app.route("/fee-line-items", method=["POST"])
def create_fee_line_item():
    item = FeeLineItem(**request.form)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for("fee_line_item", id=item.id))
"""

@member_routes.route('/<int:id>')
# @login_required
def member(id):
    member = Member.query.get_or_404(id)
    if(member is None):
        abort(404)
    return member.to_dict()
