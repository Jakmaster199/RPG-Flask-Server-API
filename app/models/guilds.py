from app import myDb
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Guild(myDb.Model):

    __tablename__ = "Guilds"

    guild_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    icon = Column(String(128), nullable=True)
    creation_date = Column(DateTime, default=datetime.utcnow())


class GuildMembers(myDb.Model):

    __tablename__ = "Guilds_Members"

    guild_id = Column(Integer, ForeignKey("Guilds.guild_id"))
    character_id = Column(Integer, ForeignKey("Characters.character_id"))
    rank_id = Column(Integer, ForeignKey("Guilds_Ranks.rank_id"))


class GuildRank(myDb.Model):

    __tablename__ = "Guilds_Ranks"

    guild_id = Column(Integer, ForeignKey("Guilds.guild_id"))
    rank_id = Column(Integer)
    name = Column(String(32), nullable=False)

