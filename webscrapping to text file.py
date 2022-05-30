from bs4 import BeautifulSoup
import requests
import time

## adding filters
print("Put skills you don't have here")
unskilled = input('>')
print(f'filtering out {unskilled}')

## job posted recently
def find_jobs():
    html_page = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_page, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate (jobs):
        date_published = job.find('span', class_="sim-posted").text
        if 'few' in date_published:
            company_name = job.find('h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find('span', class_="srp-skills").text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unskilled not in skills:

                with open (f'output/{index}.txt', 'w') as f:
                    f.write(f"Company name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info}")

                print(f'File saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} Minutes...')
        time.sleep(time_wait * 90)