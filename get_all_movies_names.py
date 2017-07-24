from bs4 import BeautifulSoup
import requests
import csv

url = "https://gomovies.sc/movies/page/{}/"

def get_number_of_page():
    url = "https://gomovies.sc/movies"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"html.parser")

    last_page_number = int(soup.find(id="pagination").find_all("li")[-1].a["href"].split("/")[-2])

    return last_page_number

def main():
    total_pages = get_number_of_page()
    with open("movies.csv","w+") as f:
        writer = csv.writer(f)
        writer.writerow(["Movie","Quality"])
        for page_number in range(1,total_pages+1):
            new_url = url.format(page_number)
            r = requests.get(new_url)
            soup = BeautifulSoup(r.text,"html.parser")
            movie_items = soup.find_all("div",{"class":"ml-item"})

            for movie_item in movie_items:
                movie_quality = movie_item.a.span.text.strip().encode("utf-8")
                movie_name = movie_item.a.img["title"].strip().encode("utf-8")
                writer.writerow([movie_name,movie_quality])

if __name__ == "__main__":
    main()
