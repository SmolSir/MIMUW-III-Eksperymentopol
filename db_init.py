from db_models import Category, Item, Experiment, Session, Base, engine
import json

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

lorem_ipsum = f"""<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Duis mollis metus eget augue scelerisque fermentum. Sed ut justo vitae augue
bibendum rhoncus. Donec vehicula justo a venenatis aliquam. Pellentesque felis
purus, auctor et condimentum tincidunt, ullamcorper et sapien. Proin a semper
est. Cras lacinia urna sed felis mollis, rutrum pretium diam tempor. Vestibulum
et placerat lectus, a tristique lectus. Donec tempor orci non turpis molestie,
eget vehicula dolor volutpat. Mauris sagittis finibus eros, vitae interdum magna
maximus id. In gravida, mi vitae elementum ullamcorper, erat orci sollicitudin
augue, ut facilisis tellus erat vel massa.</p>

<p>Donec at ornare arcu. Aenean lorem diam, vulputate ac aliquet ut, consequat et
eros. Nullam et malesuada quam. Aliquam justo odio, tincidunt et tellus id,
scelerisque faucibus ligula. Proin leo nibh, aliquet eu accumsan dapibus,
volutpat nec diam. Sed sed eros fringilla, vehicula quam quis, auctor orci.
Curabitur non sollicitudin nisi. Phasellus blandit nulla sed pellentesque
placerat. Aliquam consequat rutrum metus, id mollis ex elementum sed. Integer
ac varius lectus, vel facilisis mi. Fusce molestie consequat ex, at ullamcorper
nisi varius ut. Praesent vestibulum hendrerit cursus.</p>"""

youtube_link = "https://www.youtube.com/embed/YdfNuwMhMg4?si=ShWbZ2JH5AKHaM64"

with open("experiments.json") as f:
    experiments = json.load(f)["experiments"]

    categories = set([experiment["category"] for experiment in experiments])
    items = set(sum([experiment["items"] for experiment in experiments], []))

    session = Session()
    for category in categories:
        session.add(Category(name=category))
    for item in items:
        session.add(Item(name=item))
    session.commit()

    for experiment in experiments:
        session.add(
            Experiment(
                title=experiment["title"],
                short_description=experiment["description"],
                description=lorem_ipsum,
                category_list=session.query(Category)
                .filter(Category.name.in_((experiment["category"],)))
                .all(),
                item_list=session.query(Item)
                .filter(Item.name.in_(experiment["items"]))
                .all(),
                youtube_link=youtube_link,
            )
        )
    session.commit()
    session.close()

print("Database created successfully!")
