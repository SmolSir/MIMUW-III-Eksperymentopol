from flask import Flask, request
# from datetime import date
from db_models import Categories, Items, Experiments, Base, engine, Session

import json

application = Flask(__name__)

@application.route('/backend/available_filters')
def available_filters():
    with Session.begin() as session:
        categories = session.query(Categories).all()
        items = session.query(Items).all()
        return json.dumps({
            "categories": [(category.id, category.name) for category in categories],
            "items": [(item.id, item.name) for item in items]
        })
    
# Return experiment with given id
@application.route('/backend/experiments')
def experiments():
    with Session.begin() as session:
        # Get id from GET request
        id = request.args.get('id')
        # Get experiment with given id
        experiment = session.query(Experiments).filter_by(id=id).first()
        return json.dumps({
            "id": experiment.id,
            "title": experiment.title,
            "short_description": experiment.short_description,
            "description": experiment.description,
            "category_list": [(category.id, category.name) for category in experiment.category_list],
            "item_list": [(item.id, item.name) for item in experiment.item_list],
            "youtube_link": experiment.youtube_link
        })
    
# /backend/search?category=2&category=3&category=12&item=21&item=32&item=1212&item=312&item=132
# {
#     "experiment_list": [
#         {
#             "id": 69,
#             "title": "Experiment 1",
#             "short_description": "This is the first experiment",
#             "image_path": "/static/experiment_images/69.png",
#         },
#         {
#             "id": 70,
#             "title": "Experiment 2",
#             "short_description": "This is the second experiment",
#             "image_path": "/static/experiment_images/70.png",
#         },
#         {
#             "id": 71,
#             "title": "Experiment 3",
#             "short_description": "This is the third experiment",
#             "image_path": "/static/experiment_images/71.png",
#         },
#     ]
# }

@application.route('/backend/search')
def search():
    with Session.begin() as session:
        # Get categories and items from GET request
        categories = request.args.getlist('category')
        items = [int(i) for i in request.args.getlist('item')]
        # Get experiments with given categories and items
        experiments = session.query(Experiments).filter(
            Experiments.category_list.any(Categories.id.in_(categories)),
        ).all()
        # item_list is sublist of items 
        exp_duplicate = experiments.copy()
        # print(exp_duplicate)
        # print(items)
        # print(categories)
        for exp in exp_duplicate:
            for item in exp.item_list:
                if item.id not in items:
                    # print(exp.id, item.id)
                    experiments.remove(exp)
                    break
        return json.dumps({
            "experiment_list": [
                {
                    "id": experiment.id,
                    "title": experiment.title,
                    "short_description": experiment.short_description,
                    "image_path": f"/static/experiment_images/{experiment.id}.png",
                } for experiment in experiments
            ]
        })
