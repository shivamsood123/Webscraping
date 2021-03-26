import requests
from bs4 import BeautifulSoup
import time

start = time.time()
def parse_cities(data):
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




req = requests.get("https://www.treebo.com/blog/cleanest-cities-in-india/")
data = BeautifulSoup(req.content, 'html.parser')
top_cities = data.find_all("span", {"class" : "ez-toc-section"})
top_cities = top_cities[1:-1]
top_cities = [span.contents[0] for span in top_cities]
out_data = parse_cities(top_cities)
print(out_data)
end = time.time()

print(f"time taken for the script to run {end-start}")
