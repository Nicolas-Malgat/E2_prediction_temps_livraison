from haversine import haversine as hs
from dotenv import load_dotenv
from unittest import result
from pathlib import Path
import geocoder
import os


class Geocoder():
    def __init__(self, provider='BING') -> None:
        dotenv_path = Path('../../.env')
        load_dotenv(dotenv_path=dotenv_path)
        self.__key = os.getenv(provider)

    def batch(self, adress_list):
        return [
            result.latlng
            for result
            in geocoder.bing(adress_list, method='batch', key=self.__key)
        ]

    def get_adress(self, adress):
        return geocoder.google(adress)
    
    """ Pour deux addresses, retourne leur distance en kilometres
    """
    def get_distance(self, adr1, adr2):
        coords = self.batch([adr1, adr2])
        return hs(tuple(coords[0]), tuple(coords[1]))

if __name__ == '__main__':
    adr1 = 'Paris'
    adr2 = 'Marseille'

    bg = Geocoder()
    temp = bg.get_distance(adr1, adr2)
    temp

# from modules.data_engineering import Geocoder

# bg = Geocoder()
# coords = bg.batch(adresses)
# coords