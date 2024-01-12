from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    create_engine,
    Text,
    Table,
    ForeignKey,
    Integer,
)

engine = create_engine("sqlite:///experiments.db")
Session = sessionmaker(bind=engine)

Base = declarative_base()

association_item_experiment_table = Table(
    "association_item_experiment_table",
    Base.metadata,
    Column("left_id", ForeignKey("experiments.id")),
    Column("right_id", ForeignKey("items.id")),
)

association_category_experiment_table = Table(
    "association_category_experiment_table",
    Base.metadata,
    Column("left_id", ForeignKey("experiments.id")),
    Column("right_id", ForeignKey("categories.id")),
)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Category<id:{self.id}, name:{self.name}>"


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"Item<id:{self.id}, name:{self.name}>"


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    short_description = Column(Text)
    description = Column(Text)
    category_list = relationship(
        "Category", secondary=association_category_experiment_table
    )
    item_list = relationship("Item", secondary=association_item_experiment_table)
    youtube_link = Column(String)

    def __repr__(self):
        return f"Experiment<id:{self.id}, title:{self.title}, short_description:{self.short_description}, description:{self.description}, category_list:{[category.name for category in self.category_list]}, item_list:{[item.name for item in self.item_list]}, youtube_link:{self.youtube_link}>"
