# Browser_automation
automation with selenium in python
this is a bot which opens a college website and opens all the lectures, ppt, assignments, etc giving the highest hits.
Purpose of making this project is, it consumes a lot of time to open all docs just for the sake of formality. 
Github bot: This

## Requirements:
1)Python 2.>>

2)pip install selenium

3)download the webdriver of ur respective browser, i.e. chrome, firefox, etc.

just enter the username password in this code and and you are good to go :)

NOTE: YOU HAVE TO MENTION THE INDEX NO. OF FIRST SECTION IN THE FOR LOOPS(simply inspect that section and get the href thereby "a.index("the hrf"))", this will be the start of range)

A new script has been added to automate a commit for any repo, i.e. 
githubBot.py is the file name.


## Steps I took to execute the project

**1)** The below is the configuration you need to do for implementing it on heroku

```python
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
```
**2)** Add new buildpacks on heroku, buildpacks are mentioned below

