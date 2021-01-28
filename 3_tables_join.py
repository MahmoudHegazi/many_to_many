

show = db.Table('Show',
db.Column('id', db.Integer, primary_key=True),
db.Column('venue_id', db.Integer, db.ForeignKey('Venue.id') ,nullable=False),
db.Column('artist_id',db.Integer, db.ForeignKey('Artist.id') ,nullable=False),
db.Column('start_time',db.String, nullable=False),
db.Column('image_link',db.String),
db.Column('venue_name',db.String),
db.Column('artist_name',db.String),

)

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500), nullable=False, default='/static/img/covid_venues_joey_bruce_900_611_90.jpg')
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String)
    # 1- artist here not mean relation bettwen the Artist for each venue
    # it define which table to join the join statment 3 tables should be givin in this case
    # if there are a relation bettween the Venue and artist like store and item no need to define
    # shows var in Artist but here we have diffrent 2 tables each one should give show backref
    shows = db.relationship('Artist', secondary=show, backref=db.backref('venue', lazy=True))




    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    # i hope it work

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120), nullable=False, default='/static/img/84241059_189132118950875_4138507100605120512_n.jpg')
    website = db.Column(db.String)
    #
    shows = db.relationship('Venue', secondary=show, backref=db.backref('artist', lazy=True))
