from app import myDb
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric, Boolean


class Character(myDb.Model):

    __tablename__ = "Characters"

    character_id = Column(Integer, primary_key=True, autoincrement=True)
    account_id = Column(Integer, ForeignKey("Account.account_id"), nullable=False)
    name = Column(String(24), nullable=False)
    level = Column(Integer, nullable=False)
    race = Column(Integer, nullable=False)
    profession = Column(Integer, nullable=False)
    title = Column(String(32), nullable=True)
    
    sex = Column(Integer, default=0)

    is_online = Column(Boolean, nullable=False, default=False)

    creation_date = Column(DateTime, default=datetime.utcnow())
    modification_date = Column(DateTime, default=datetime.utcnow())


class CharacterStats(myDb.Model):

    __tablename__ = "Characters_Stats"

    character_id = Column(Integer, ForeignKey("Characters.character_id"))
    max_hp = Column(Numeric(precision=10, scale=2))
    current_hp = Column(Numeric(precision=10, scale=2))
    max_mp = Column(Numeric(precision=10, scale=2))
    current_mp = Column(Numeric(precision=10, scale=2))
    current_xp = Column(Integer)

    # Should be calculated from class stats + profession stats + equipped items
    attack_speed = Column(Integer, default=0)
    physical_attack = ""
    physical_defense = ""
    magical_attack = ""
    magical_defense = ""

    # Elemental Resistance Stats

    strength = Column(Integer, default=0)
    intellect = Column(Integer, default=0)
    charisma = Column(Integer, default=0)
    luck = Column(Integer, default=0)
    vitality = Column(Integer, default=0)
    mentality = Column(Integer, default=0)
    dexterity = Column(Integer, default=0)
    perception = Column(Integer, default=0)


class CharacterInventory(myDb.Model):

    __tablename__ = "Characters_Inventory"

    character_id = Column(Integer, ForeignKey("Characters.character_id"))
    item_id = Column(Integer, ForeignKey("Items.item_id"))
    is_equipped = Column(Integer, default=0)
    equipped_slot = Column(Integer, default=0)
    augmentation = Column(Integer, default=0)


class CharacterAbility(myDb.Model):

    __tablename__ = "Characters_Abilities"

    character_id = Column(Integer, ForeignKey("Characters.character_id"))
    ability_id = Column(Integer, ForeignKey("Abilities.ability_id"))
    level = Column(Integer)


class CharacterLocation(myDb.Model):

    __tablename__ = "Characters_Location"

    character_id = Column(Integer, ForeignKey("Characters.character_id"))
    map = Column(Integer, default=0)
    x = Column(Integer, default=0)
    y = Column(Integer, default=0)
    z = Column(Integer, default=0)
    sight = Column(Integer, default=0)

class CharacterFriend(myDb.Model):

    __tablename__ = "Characters_Friends"