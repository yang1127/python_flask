# -*-coding:utf-8-*-
from flask import Blueprint, render_template

blueprint = Blueprint('products', __name__, url_prefix='/products', template_folder='templates', static_folder='static')


@blueprint.route("/car")
def car_products():
    return render_template('car.html')


@blueprint.route("/baby")
def baby_products():
    return render_template('baby.html')