from shapely.geometry import Point
from geoalchemy2.shape import from_shape
from models.vibe import Vibe , User
from config import db
from sqlalchemy import func
import json
# fetching all the vibes of unique user

# saving a vibe
def pin_vibe(user_id,content,longitude,latitude):
    point = Point(longitude,latitude)
    vibe=Vibe(
        user_id = user_id,
        content = content,
        location= from_shape(point,srid=4326) # create a WKBElement  from a shapely object
    )
    db.session.add(vibe)
    db.session.commit()
    return vibe

#fetching all the nearby pubicly available vibes.
def nearby_vibe(longitude,latitude , radius_meters=500):
    user_point = f"SRID=4326;POINT({longitude}{latitude})" 
    return Vibe.query.filter(
          Vibe.is_active == True,
          Vibe.is_public==True,
          func.ST_DWithin(
            Vibe.location,
            func.ST_GeogFromText(user_point),
            radius_meters
        )
    ).all

