from db_models import *
import random

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

lorem_ipsum = f'''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mollis metus eget augue scelerisque fermentum. Sed ut justo vitae augue bibendum rhoncus. Donec vehicula justo a venenatis aliquam. Pellentesque felis purus, auctor et condimentum tincidunt, ullamcorper et sapien. Proin a semper est. Cras lacinia urna sed felis mollis, rutrum pretium diam tempor. Vestibulum et placerat lectus, a tristique lectus. Donec tempor orci non turpis molestie, eget vehicula dolor volutpat. Mauris sagittis finibus eros, vitae interdum magna maximus id. In gravida, mi vitae elementum ullamcorper, erat orci sollicitudin augue, ut facilisis tellus erat vel massa.\n
Donec at ornare arcu. Aenean lorem diam, vulputate ac aliquet ut, consequat et eros. Nullam et malesuada quam. Aliquam justo odio, tincidunt et tellus id, scelerisque faucibus ligula. Proin leo nibh, aliquet eu accumsan dapibus, volutpat nec diam. Sed sed eros fringilla, vehicula quam quis, auctor orci. Curabitur non sollicitudin nisi. Phasellus blandit nulla sed pellentesque placerat. Aliquam consequat rutrum metus, id mollis ex elementum sed. Integer ac varius lectus, vel facilisis mi. Fusce molestie consequat ex, at ullamcorper nisi varius ut. Praesent vestibulum hendrerit cursus.'''

session = Session()
session.add(Experiments(title="Fontanna z butelki wody", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Olej i woda", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Ręcznik papierowy", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Sól i woda", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Cukier i woda", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Ocet i soda oczyszczona", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Mydło i mleko", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Jajko w butelce", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Barwnik spożywczy i mleko", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Lód i sól", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Latający balon", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Balonowy rajd", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Cytryna i soda oczyszczona", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Ziemniak i ocet", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.add(Experiments(title="Świeca z butelki plastikowej", short_description="Lorem ipsum", description=lorem_ipsum, youtube_link="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
session.commit()
session.close()

session = Session()
session.add(Categories(name="Fizyka"))
session.add(Categories(name="Chemia"))
# session.add(Categories(name="Biologia"))
session.add(Categories(name="Matematyka"))
session.add(Categories(name="Informatyka"))
# session.add(Categories(name="Inżynieria"))
session.add(Categories(name="Elektronika"))
session.commit()
session.close() 

session = Session()
session.add(Items(name="Woda"))
session.add(Items(name="Olej"))
session.add(Items(name="Papier"))
session.add(Items(name="Sól"))
session.add(Items(name="Cukier"))
session.add(Items(name="Ocet"))
session.add(Items(name="Soda"))
session.add(Items(name="Mydło"))
session.add(Items(name="Mleko"))
session.add(Items(name="Jajko"))
session.add(Items(name="Barwnik spożywczy"))
# session.add(Items(name="Cytryna"))
# session.add(Items(name="Ziemniak"))
# session.add(Items(name="Świeca"))
# session.add(Items(name="Lód"))
# session.add(Items(name="Balon"))
# session.add(Items(name="Butelka plastikowa"))
# session.add(Items(name="Butelka szklana"))
# session.add(Items(name="Kubek"))
# session.add(Items(name="Miska"))
# session.add(Items(name="Łyżka"))
# session.add(Items(name="Widelec"))
# session.add(Items(name="Nóż"))
# session.add(Items(name="Talerz"))
# session.add(Items(name="Nożyczki"))
# session.add(Items(name="Taśma klejąca"))
# session.add(Items(name="Sznurek"))
# session.add(Items(name="Linijka"))
# session.add(Items(name="Długopis"))
# session.add(Items(name="Ołówek"))
# session.add(Items(name="Marker"))
# session.add(Items(name="Gumka do ścierania"))
# session.add(Items(name="Spinacz do papieru"))
# session.add(Items(name="Wykałaczka"))
# session.add(Items(name="Słomka"))
# session.add(Items(name="Pasta do zębów"))
# session.add(Items(name="Ręcznik"))
# session.add(Items(name="Bateria"))
# session.add(Items(name="Bawełna"))
# session.add(Items(name="Guma"))
# session.add(Items(name="Folia aluminiowa"))
# session.add(Items(name="Plastik"))
# session.add(Items(name="Drewno"))
# session.add(Items(name="Metal"))
# session.add(Items(name="Szkło"))
# session.add(Items(name="Ceramika"))
# session.add(Items(name="Piasek"))
# session.add(Items(name="Kamień"))
# session.add(Items(name="Magnes"))
session.commit()
session.close()

session = Session()

items_count = session.query(Items).count()

for experiment in session.query(Experiments).all() :
    [n] = random.sample(range(1, min(5, items_count)), 1)
    for i in random.sample(range(1, items_count), n) :
        experiment.item_list.append(session.query(Items).filter_by(id=i).first())
session.commit()
session.close()

session = Session()

categories_count = session.query(Categories).count()

for experiment in session.query(Experiments).all() :
    [n] = random.sample(range(1, min(3, categories_count)), 1)
    for i in random.sample(range(1, categories_count), n) :
        experiment.category_list.append(session.query(Categories).filter_by(id=i).first())
session.commit()
session.close()

print("\nDatabase created successfully\n")

print("\nCategories:\n")

session = Session()
for category in session.query(Categories).all() :
    print(category.name)
session.close()

print("\nItems:\n")

session = Session()
for item in session.query(Items).all() :
    print(item.name)
session.close()

print("\nExperiments:\n")

session = Session()
for experiment in session.query(Experiments).all() :
    print(experiment)
session.close()
