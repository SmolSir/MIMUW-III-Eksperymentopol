from flask import Flask, request, render_template
from markupsafe import Markup
from db_models import Category, Item, Experiment, Session

import json

application = Flask(__name__)


@application.route("/")
def index():
    return render_template("index.html")


@application.route("/api/available_filters")
def available_filters():
    with Session.begin() as session:
        categories = session.query(Category).all()
        items = session.query(Item).all()
        return json.dumps(
            {
                "categories": [(category.id, category.name) for category in categories],
                "items": [(item.id, item.name) for item in items],
            }
        )


@application.route("/experiment")
def experiments():
    with Session.begin() as session:
        id = request.args.get("id")
        experiment = session.query(Experiment).filter_by(id=id).first()

        return render_template(
            "experiment.html",
            title=experiment.title,
            experiment_title=experiment.title,
            experiment_short_description=experiment.short_description,
            experiment_description=Markup(experiment.description),
            experiment_category_list=experiment.category_list,
            experiment_item_list=experiment.item_list,
            experiment_youtube_link=experiment.youtube_link,
        )


@application.route("/api/search")
def search():
    with Session.begin() as session:
        categories = request.args.getlist("category")
        items = [int(i) for i in request.args.getlist("item")]
        experiments = None
        if categories:
            experiments = (
                session.query(Experiment)
                .filter(
                    Experiment.category_list.any(Category.id.in_(categories)),
                )
                .all()
            )
        else:
            experiments = session.query(Experiment).all()
        if items:
            experiments = filter(
                lambda experiment: all(
                    item.id in items for item in experiment.item_list
                ),
                experiments,
            )
        return json.dumps(
            {
                "experiment_list": [
                    {
                        "id": experiment.id,
                        "title": experiment.title,
                        "short_description": experiment.short_description,
                        "image_path": f"/static/experiment_images/{experiment.id}.jpg",
                    }
                    for experiment in experiments
                ]
            }
        )
