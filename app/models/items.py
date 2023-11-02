from app import myDb


class Weapon(myDb.Model):
    __tablename__ = "Weapons"


class Armor(myDb.Model):
    __tablename__ = "Armors"


class EtcItem(myDb.Model):
    __tablename__ = "Etc_Items"
