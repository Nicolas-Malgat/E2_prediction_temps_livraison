from dotenv import load_dotenv
from pathlib import Path
import geocoder
import os

class BingGeocoder():
    def __init__(self) -> None:
        dotenv_path = Path('../../.env')
        load_dotenv(dotenv_path=dotenv_path)
        self.__key = os.getenv('BING_API_KEY')

    def loc_batch(self, adress_list):
        return geocoder.bing(adress_list, method='batch', key=self.__key)

if __name__ == '__main__':
    bg = BingGeocoder()
    coords = bg.loc_batch([
        'Place de Jaude',
        'Tour Eiffel',
        'Tour de Pise'
    ])
    print(
        [coord.latlng for coord in coords]
    )


# from modules.data_engineering import BingGeocoder

# bg = BingGeocoder()
# coords = bg.loc_batch([
#     'Place de Jaude',
#     'Tour Eiffel',
#     'Tour de Pise'
# ])
# [coord.latlng for coord in coords]