from app import myDb


class Race(myDb.Model):
    __tablename__ = "Races"

    race_id = ""
    name = ""
    playable = ""

    base_hp = ""
    base_mp = ""


class Profession(myDb.Model):
    __tablename__ = "Professions"

    profession_id = ""
    name = ""
