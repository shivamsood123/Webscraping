import top_city


html = top_city.web_scraper("https://www.treebo.com/blog/cleanest-cities-in-india/", "span", "ez-toc-section")
print(html.get_results())
