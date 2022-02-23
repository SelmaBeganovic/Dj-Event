import click
from flask.cli import with_appcontext
from datetime import datetime


@click.command()
@with_appcontext
def insert_events_into_database():
    from api.events.event_model import Event
    from api import db
    events = [
        {
            "id": "1",
            "name": "Throwback Thursdays with DJ Manny Duke",
            "slug": "throwback-thursdays-with-dj-manny-duke",
            "venue": "Horizon Club",
            "address": "919 3rd Ave New York, New York(NY), 10022",
            "performers": "DJ Manny Duke",
            "date": "06-09-2021",
            "time": "10:00 PM EST",
            "description": "Featuring deep cuts, party anthems and remixes nostalgic songs from two of the best decades of music with the very best music from the 90's and 2000's",
            "image": "/images/sample/event1.jpg"
        },
        {
            "id": "2",
            "name": "Boom Dance Festival Experience",
            "slug": "boom-dance-festival-experience",
            "venue": "Blackjacks",
            "address": "966 Lexington Ave New York, New York(NY), 10021",
            "performers": "DJ LUCK & MC NEAT, NICKY BLACKMARKET, DJ NICKY BLACKMARKET, RATPACK",
            "date": "06-02-2021",
            "time": "8:00 PM EST",
            "description": "It's looking more and more like we will be seeing events return in the summer! To celebrate this we are arranging a festival experience to say good bye to lock down! We will also be celebrating the fact Zoom Dance is one year old!",
            "image": "/images/sample/event2.jpg"
        },
        {
            "id": "3",
            "name": "Encore Night Boat Party",
            "slug": "encore-night-boat-party",
            "venue": "Encore",
            "address": "675 Water St New York, New York(NY), 10002",
            "performers": "Bad Boy Bill",
            "date": "06-11-2021",
            "time": "7:00 PM EST",
            "description": "Who is ready to party? I mean in the middle of the water, a boat with good music and drinks. If thats you then you have made it to the right place.",
            "image": "/images/sample/event3.jpg"
        },
        {
            "id": "4",
            "name": "Jam Concert Live",
            "slug": "jam-concert-live",
            "venue": "Club Ozone",
            "address": "70 W 115th St New York, New York(NY), 10026",
            "performers": "DJ RNB",
            "date": "06-20-2021",
            "time": "10:00 PM EST",
            "description": "The most diverse dj on the east coast, DJ RNB team up once again to bring you the next installment in the high energy, Jam Concert Live series!",
            "image": "/images/sample/event4.jpg"
        },
        {
            "id": "5",
            "name": "UnMute Rock Festival",
            "slug": "unmute-rock-festival",
            "venue": "Studio 54",
            "address": "55 La Salle St #12K New York, New York(NY), 10027",
            "performers": "Big Wednesday, Black Pyre, Calling Apollo",
            "date": "06-30-2021",
            "time": "8:00 PM EST",
            "description": "With bands from around the UK ready to send the roof into orbit, get ready for the loudest Welsh festival: the inaugural UnMute 2021.",
            "image": "/images/sample/event5.jpg"
        },
        {
            "id": "6",
            "name": "Soul Kitchen Party",
            "slug": "soul-kitchen-party",
            "venue": "Onyx Club",
            "address": "60 Gramercy Park N #2 New York, New York(NY), 10010",
            "performers": "A-Trak, Nightmares on Wax, Rakim, Jay Electronica",
            "date": "06-02-2021",
            "time": "8:00 PM EST",
            "description": "Dope party which features Hip Hop legends, emerging artists and world-class turntablists",
            "image": "/images/sample/event6.jpg"
        }
    ]
    for evt in events:
        existing_event = Event.query.filter(Event.name == evt.get("name")).one_or_none()
        if existing_event is None:
            new_event = Event(name=evt.get("name"), venue=evt.get("venue"), slug=evt.get("slug"),
                              address=evt.get("address"), performers=evt.get("performers"),
                              date=datetime.strptime(evt.get("date"), '%m-%d-%Y'),
                              time=evt.get("time"), description=evt.get("description"))

            db.session.add(new_event)
            db.session.commit()
