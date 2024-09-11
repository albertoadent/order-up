from flask import Blueprint, render_template, request
from flask_login import login_required
from app.models import Table, Order
from app.forms import TableAssignmentForm

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = TableAssignmentForm()
    if request.method == "POST":
        # Get the tables and open orders
        tables = Table.query.order_by(Table.number).all()
        open_orders = Order.query.filter(Order.finished == False)

        # Get the table ids for the open orders
        busy_table_ids = [order.table_id for order in open_orders]

        # Filter the list of tables for only the open tables
        open_tables = [table for table in tables if table.id not in busy_table_ids]

        # Finally, convert those tables to tuples for the select field and set the
        # choices property to it
        form.tables.choices = [(t.id, f"Table {t.number}") for t in open_tables]
    return render_template("order.html", form=form)
