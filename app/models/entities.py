from app import myDb
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Entity(myDb.Model):

    __tablename__ = "Entities"

    entity_id = Column(Integer, primary_key=True, autoincrement=True)

    name = ""
    level = ""
    race_id = Column(Integer, ForeignKey("Races.race_id"))


class Monster(myDb.Model):

    __tablename__ = "Monsters_Stats"

    entity_id = Column(Integer, ForeignKey("Entities.entity_id"))


class NPC(myDb.Model):

    __tablename__ = "NPCs_Stats"

    entity_id = Column(Integer, ForeignKey("Entities.entity_id"))

