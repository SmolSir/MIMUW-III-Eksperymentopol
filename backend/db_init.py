from db_models import *
import random

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

session = Session()
session.add(Experiments(title="Water Bottle Fountain", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.add(Experiments(title="Oil and Water", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.add(Experiments(title="Paper Towel", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.add(Experiments(title="Salt and Water", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.add(Experiments(title="Sugar and Water", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.add(Experiments(title="Vinegar and Baking Soda", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.add(Experiments(title="Soap and Milk", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.add(Experiments(title="Egg in a Bottle", short_description="Make a water bottle fountain", description="Make a water bottle fountain", youtube_link="https://www.youtube.com/watch?v=Zf2gcy3Zgqo"))
session.commit()
session.close()

# Add example data to Categories table
session = Session()
session.add(Categories(name="Physics"))
session.add(Categories(name="Chemistry"))
session.add(Categories(name="Biology"))
session.add(Categories(name="Math"))
session.add(Categories(name="Computer Science"))
session.add(Categories(name="Engineering"))
session.add(Categories(name="Electronics"))
session.commit()
session.close()

# Add example data to Items table
session = Session()
session.add(Items(name="Water"))
session.add(Items(name="Oil"))
session.add(Items(name="Paper"))
session.add(Items(name="Salt"))
session.add(Items(name="Sugar"))
session.add(Items(name="Vinegar"))
session.add(Items(name="Baking Soda"))
session.add(Items(name="Soap"))
session.add(Items(name="Milk"))
session.add(Items(name="Egg"))
session.add(Items(name="Food Coloring"))
session.add(Items(name="Lemon"))
session.add(Items(name="Potato"))
session.add(Items(name="Candle"))
session.add(Items(name="Ice"))
session.add(Items(name="Balloon"))
session.add(Items(name="Plastic Bottle"))
session.add(Items(name="Glass Bottle"))
session.add(Items(name="Cup"))
session.add(Items(name="Bowl"))
session.add(Items(name="Spoon"))
session.add(Items(name="Fork"))
session.add(Items(name="Knife"))
session.add(Items(name="Plate"))
session.add(Items(name="Scissors"))
session.add(Items(name="Tape"))
session.add(Items(name="String"))
session.add(Items(name="Ruler"))
session.add(Items(name="Pen"))
session.add(Items(name="Pencil"))
session.add(Items(name="Marker"))
session.add(Items(name="Rubber Band"))
session.add(Items(name="Paper Clip"))
session.add(Items(name="Toothpick"))
session.add(Items(name="Straw"))
session.add(Items(name="Toothpaste"))
session.add(Items(name="Towel"))
session.add(Items(name="Battery"))
session.add(Items(name="Cotton"))
session.add(Items(name="Rubber"))
session.add(Items(name="Aluminum Foil"))
session.add(Items(name="Plastic"))
session.add(Items(name="Wood"))
session.add(Items(name="Metal"))
session.add(Items(name="Glass"))
session.add(Items(name="Ceramic"))
session.add(Items(name="Sand"))
session.add(Items(name="Rock"))
session.add(Items(name="Magnet"))
session.commit()
session.close()

# Add example items to experiments in assosiation table
session = Session()

# Number of items in Items table
items_count = session.query(Items).count()

# Add up to 7 random items from all items to each experiment
for experiment in session.query(Experiments).all() :
    [n] = random.sample(range(1, min(7, items_count)), 1)
    for i in random.sample(range(1, items_count), n) :
        experiment.item_list.append(session.query(Items).filter_by(id=i).first())
session.commit()
session.close()

# Add example categories to experiments in assosiation table
session = Session()

# Number of items in Items table
categories_count = session.query(Categories).count()

# Add up to 3 random items from all items to each experiment
for experiment in session.query(Experiments).all() :
    [n] = random.sample(range(1, min(3, categories_count)), 1)
    for i in random.sample(range(1, categories_count), n) :
        experiment.category_list.append(session.query(Categories).filter_by(id=i).first())
session.commit()
session.close()

print("\nDatabase created successfully\n")

print("\nCategories:\n")

# Print all categories from Categories table
session = Session()
for category in session.query(Categories).all() :
    print(category.name)
session.close()

print("\nItems:\n")

# Print all items from Items table
session = Session()
for item in session.query(Items).all() :
    print(item.name)
session.close()

print("\nExperiments:\n")

# Print all experiments from Experiments table
session = Session()
for experiment in session.query(Experiments).all() :
    print(experiment)
session.close()
