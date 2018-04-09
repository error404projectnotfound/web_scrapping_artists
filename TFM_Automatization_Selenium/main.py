# -*- coding: utf-8 -*-
import logging
import time
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


letters_string = string.ascii_lowercase
letters_list = list(letters_string)
letters_list.append("number")

driver = webdriver.Chrome("C:/Windows/chromedriver_win32/chromedriver.exe")
partial_url = "https://www.billboard.com/artists/"
full_url = ""
authors_buffer = ""

authors_counter = 0
partial_authors_file_name = "Billboard_authors_"

try:
    for letter in letters_list:
        if letter == "number":
            full_authors_file_name = partial_authors_file_name + "#.txt"
        else:
            full_authors_file_name = partial_authors_file_name + letter.upper() + ".txt"
        full_authors_file_opened = open(full_authors_file_name, "wb")
        full_url = partial_url + letter
        driver.get(full_url)
        authors_table = driver.find_elements_by_xpath('//*[@id="block-system-main"]/div/div/div[2]/table/tbody/tr')
        
        for authors_row in authors_table: #Iterates over the authos table
            authors_list = authors_row.text.split("\n")
            for author in authors_list:
                authors_buffer += author + "|"
                authors_counter += 1
                if authors_counter % 500 == 0:
                    full_authors_file_opened.write(authors_buffer.rstrip('\n').encode())
                    authors_buffer = ""
                    print("INFO: url:", full_url)
                    print("INFO: Authors counter:", authors_counter)

        full_authors_file_opened.write(authors_buffer[:-1].rstrip('\n').encode())
        authors_buffer = ""
        print("INFO: url:", full_url)
        print("INFO: Authors counter:", authors_counter)
        full_authors_file_opened.close()

except Exception as e:
    print(e)
    print("An error has ocurred in the following url:", full_url)
    print("Authors counter for that url:", authors_counter)




'''
driver = webdriver.Chrome("C:/Windows/chromedriver_win32/chromedriver.exe")
partial_url = "http://www.songfacts.com/released-"
full_url = ""
authors_counter = 0

authors_file = open("SongFacts_authors.txt","w")
try:
    for year in range(1950, 2019):
        partial_url_year = partial_url + str(year)
        full_url = partial_url_year + "-1.php"
        driver.get(full_url)

        try: #Looks for the greatest page number. The following xpath defines the greatest one.
            last_page = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/div/div[1]/a[2]")
            last_page_number = last_page.text if "Next" not in last_page.text  else 2
        except:
            try: #Looks for the second page number. The following xpath defines the second one.
                last_page = driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/div/div[1]/a[1]")
                last_page_number = last_page.text
            except: #There is only one page of songs for that year
                last_page_number = 1
        
        authors_string = ""
        for i in range(1, int(last_page_number) + 1): #Iterates over the different table pages
            full_url = partial_url_year + "-" + str(i) + ".php"
            print(full_url)
            print(authors_counter)
            driver.get(full_url)
            song_author_table = driver.find_elements_by_xpath("/html/body/div[5]/div[1]/div/div/div/ul/li")
            
            for row in song_author_table: #Iterates over the authos table
                author = row.text.split("-")[1]
                authors_string += author.strip() + "|"
                authors_counter += 1
                if authors_counter % 10 == 0: #Write collected authors and reset the string
                    authors_file.write(authors_string.rstrip('\n'))
                    authors_string = ""
            time.sleep(0.5)
            authors_file.write(authors_string.rstrip('\n'))
            authors_string = ""
except Exception as e:
    print(e)
    print("An error has ocurred:", full_url)
    print("Authors counter for that url:", authors_counter)

authors_file.close()
driver.close()
'''