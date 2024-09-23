from server_start import app, db, Drink
db.session.add(Drink(name = "Grape soda", description = "Taste like grape"))
db.session.commit()

