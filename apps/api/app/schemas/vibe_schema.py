from config import db
from sqlalchemy import func
import json

# returning geojson for the map
def vibe_to_geojson(vibe):
    geojson_Str = db.session.scalar( 
        func.ST_AsGeoJson( vibe.location)
        )
    return {
        'type':'Feature',
        'Geometry':json.loads(geojson_Str),
        'properties':{
            'id':str(vibe.id),
            'content':vibe.content,
            'created_at':vibe.created_at.isoformat()
        }
        
    }

def vibes_to_feature_collection(vibes):
    return {
        "type": "FeatureCollection",
        "features": [vibe_to_geojson(v) for v in vibes]
    }