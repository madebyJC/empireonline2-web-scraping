from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service(r"C:\\Users\\janns\\PycharmProjects\\chromedriver.exe")
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

driver.get("https://www.empireonline.com/movies/features/best-movies-2/")
all_movies = driver.find_elements(By.CSS_SELECTOR, ".listicle-container h3")

with open("Empire's 100 Greatest Movies 2022", mode="w", encoding="utf-8") as file:
    file.write("The 100 Greatest Movies 2022 \n")
    file.write("Source: Empire Online \n")
    file.write("https://www.empireonline.com/movies/features/best-movies-2/ \n\n")
    for movie in all_movies[::-1]:
        file.write(f"{movie.text}\n")

    print("Successfully written to file.")

