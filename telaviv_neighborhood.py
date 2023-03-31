import os

import requests
import json

import django
from django.db import IntegrityError
os.environ['DJANGO_SETTINGS_MODULE'] = 'kiddie_closet.settings'

django.setup()

from kiddie_closet_app.models import Neighborhood

# Send API request and retrieve response
url = "https://gisn.tel-aviv.gov.il/arcgis/rest/services/IView2/MapServer/511/query?where=1%3D1&outFields=*&f=json"
response = requests.get(url)

if response.status_code != 200:
    # handle API request error
    print("Error: API request failed")
else:
    # Parse JSON response and extract neighborhood names
    data = json.loads(response.text)
    neighborhoods = [Neighborhood(neighborhood_name=record["attributes"]["shem_shchuna"]) for record in
                     data["features"]]

    try:
        # Bulk create Neighborhood objects in database
        Neighborhood.objects.bulk_create(neighborhoods)
        print("Neighborhoods saved to database successfully")
    except IntegrityError:
        # handle database error
        print("Error: Failed to save neighborhoods to database")

