import pandas as pd
import pgeocode
import geopy.distance
import math

class Service:
  def __init__(self, filename):
    self.df = pd.read_csv (filename)

  def getNearestStarbucks(self, countryCode, zipcode):
    nomi = pgeocode.Nominatim(countryCode)
    nomi.query_postal_code(zipcode)

    coords_1 = (nomi.query_postal_code(zipcode)['latitude'],nomi.query_postal_code(zipcode)['longitude'])
    self.df['distance'] = self.df.apply(lambda row : self.calculateDistance(coords_1,row), axis=1)
    self.df = self.df.fillna('')
    self.df = self.df.sort_values(by='distance')
    self.df = self.df[self.df['distance'] > 0]
    return self.df.head(10).to_json(orient="records")

  def calculateDistance(self,coords_1,row):
      coords_2 = (row['Latitude'], row['Longitude'])
      if math.isnan(coords_2[0]) or math.isnan(coords_2[1]):
          return -1
      return geopy.distance.geodesic(coords_1,coords_2).miles
