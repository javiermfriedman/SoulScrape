from bs4 import BeautifulSoup
import requests
from datetime import datetime

def classes_day(day):
        classes = day.find_all("div", class_="session open")

        for cls in classes:
                # Find the child elements for time and class-type
                time = cls.find("span", class_="time").text.strip()  # Extracts text inside <span class="time">
                name = cls.find("span", class_="class-type").text.strip()  # Extracts text inside <span class="class-type">
                
                # Print the extracted values
                print(" " + time + ": " + name)
        print("\n")


def reorder_array(days):
        day_of_month = datetime.now().day
        day_of_month = day_of_month

        for day in days:
                class_date = int(day['data-date'])
                if day_of_month == class_date:
                        break
                elif day_of_month > class_date:
                        days.append(days.pop(0))

        return days

def get_info():
        # my studios url
        url = "https://www.soul-cycle.com/find-a-class/studio/1/"

        # Fetch the webpage content
        page = requests.get(url)

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(page.text, "html.parser")

        # the table with the classes of the week is: class = classes-week-cols
        table = soup.find("div", class_="classes-week-cols")

        # put all the days of the week into a column
        days = table.find_all('div', attrs={'data-date': True})

        # reorder the days so that today is the first day of array
        days = reorder_array(days)

        # Iterate over each div and print the 'data-date' attribute

        print("TODAY")
        classes_day(days[0])
        print("TOMORROW")
        classes_day(days[1])
        print("DAY AFTER TOMORROW")
        classes_day(days[2])


