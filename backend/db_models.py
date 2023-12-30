from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, create_engine, Text, Table, ForeignKey, Integer

engine = create_engine("sqlite:///experiments.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Categories<id:{self.id}, name:{self.name}>"

association_table = Table(
    "association_table",
    Base.metadata,
    Column("left_id", ForeignKey("experiments.id")),
    Column("right_id", ForeignKey("items.id")),
)

class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Items<id:{self.id}, name:{self.name}>"

class Experiments(Base):
    __tablename__ = 'experiments'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    short_description = Column(Text)
    description = Column(Text)
    item_list = relationship("Items", secondary=association_table)
    youtube_link = Column(String)

    def __repr__(self):
        return f"Experiments<id:{self.id}, title:{self.title}, short_description:{self.short_description}, description:{self.description}, youtube_link:{self.youtube_link}, item_list:{[item.name for item in self.item_list]}>"
