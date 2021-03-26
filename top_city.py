import requests
from bs4 import BeautifulSoup


class web_scraper:
    
    def __init__(self,url, tag, class_name):
        req = requests.get(url)
        self.html = BeautifulSoup(req.content, 'html.parser')
        self.cities = self.find_class(tag, class_name)
        self.cities = self.cities[1:-1]
        self.cities =  [span.contents[0] for span in self.cities]
        
    def find_class(self, tag, class_name):
        return self.html.find_all(tag, {"class" : class_name})
    
    
    def parse_cities(self, data):
        return_dict = {}
        for data_point in data:
            city_data = data_point.split(".")
            position = int(city_data[0])
            try: 
                city_state = city_data[1].split(",")
                city = city_state[0]
                state = city_state[1]
            except:
                city = city_data[1]
                state = city_data[1]
            pos_data = {
                "city" : city,
                "state" : state
            }
            return_dict[position] = pos_data
        return return_dict
    
    def get_results(self):
        return self.parse_cities(self.cities)
    
    def another_fun():
        pass
    
