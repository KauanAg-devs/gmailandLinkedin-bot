# Connect with People on LinkedIn, Send a Custom Message with Person's Name Automatically!

A Python Selenium bot to automate connection with people on LinkedIn

<b>Send 200 connection requests in 15 minutes with one click, automatically add custom connect message with person's name included!</b>

LinkedIn constantly updates its pages elements' selectors. If You would like to see more scripts and more frequent updates, please consider a donation to the student (me) for a new laptop and an education abroad 💲💲: https://nakigoe.org/en/donate

## The project needs funding, planned features:

•  separating basic documentation and setup instructions;

•  separating code into 3 parts: 

     1) script logic, 

     2) moving assistant functions into PyPI package, 

     3) adding a separate file with settings;

inquiries: https://t.me/nakigoe

⭐ Add stars to all my repositories on GitHub: https://github.com/nakigoe

<b>3 February 2024 update:</b>

•  `eternal_wait()` function introduced to wait for login and other critical pages to load. That is the star of this script!!!

•  LinkedIn has limited the number of personalized invitations that could be sent per month, so the script sends 200 invitations per week as previousely, but the function that sent a custom message with a person's name is turned on by setting the `CONNECT_WITH_NAME = True`. Currently is set to `CONNECT_WITH_NAME = False` to keep the number of available personalized messages per month to the moments when you actually need them.

<b>24 January 2024 major upgrade:</b>

•  Added search by multiple locations and multiple occupations, see the arrays `us_locations`, `uk_locations`, and `linkedin_occupations`. You still might need to copy&#8209;n&#8209;paste the exact search URL from the actual search page to add other parameters than location and occupation. Currently only one optional parameter is added: `new connection is your 2-nd connection`.

•  Element selectors update

<b>19 January 2024 update:</b>

Multi-search feature added: 

•  You can now add multiple people from your contacts, whom contacts you want to connect to, defined in `search_links_array`;

<b>20 October 2023 upgrade:</b>

• outdated `cookie` files with entire `auth` folder are deleted automatically, and a standard login procedure with a username and password starts;

<b>24 September 2023 upgrade:</b>

• if a message recepeient's name is too long, shortens it to fit the LinkedIn limit of 300 characters per message.

<b>13 September 2023 major upgrade:</b>

• correct successful login indicator

<b>02 September 2023 major upgrade:</b> improved algorithm and functions, added `custom_search` query support.

<b>27 August 2023 major upgrade:</b> added `user agent`, `cookies` and `local storage` support to keep the login information from the last session and to reduce LinkedIn automation detection.

## How To Use

You must use **_English_** LInkedIn for the script to work.

The script has been written and tested many times for use with the **_Microsoft Edge_** browser. Sometimes installing the **LATEST VERSION** of **_Microsoft Edge_** on your device is required for the correct operation of this automation software.

Sometimes you need to manually download `msedgedriver.exe` from the Microsoft website: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Enter the path to the downloaded `msedgedriver.exe` into `system variables`.

Screen resolution and width is rather important when it comes to LinkedIn.
<br> The script is tested on 1280px and 1366px screen width resolutions. It is working!

### Change Weekly:

There is a weekly limit of invitations that could be sent on LinkedIn, so, to reduce automation detection, Your current weekly limit is set to 200 in `weekly_limit` and Your current `weekly_counter` is stored in a separate file `linkedin-weekly-counter.txt`.

Be sure to reset manually the value inside the file `linkedin-weekly-counter.txt` back to 0 every Monday! Just utilize any text editor and replace any value inside the file with `0`

### Change:

• Your browser information You usually use to browse LinkedIn (to reduce automation detection) `user_agent`

You can find your current browser's user-agent by searching **_"What's my user-agent?"_** in any search engine, it is just a string.

• The email to login on LinkedIn `username`

• Your password `password`

• People on LinkedIn in whose connections You are interested, see `search_query_array`, in that case change `custom_query_array` to `[]` right after the appropriate `for` cycle

Make sure that the target people allowed to browse their contacts. One can disable that in the profile settings.
You have to find people who allowed his / her contacts to be browsed. The link to the list of the person's connections must be clickable on their profile.

• Search by multiple locations and multiple occupations, see the arrays `us_locations`, `uk_locations`, and `linkedin_occupations` and the appropriate `for` cycle just below them. You still might need to copy&#8209;n&#8209;paste the exact search URL from the actual search page to add other parameters than location and occupation. Currently only one optional parameter is added: `new connection is your 2-nd connection`.

• Your custom messages set (without greating, the greating is included in the code!). Include as many different messages as reasonably possible to minimize LinkedIn automation detection:

`linkedin-invitation-0.txt`

`linkedin-invitation-1.txt`

`linkedin-invitation-2.txt`

`linkedin-invitation-3.txt`

• Your number of custom messages:

`number_of_messages`

### Install Python:

• https://www.python.org/downloads/

### Install PIP If it Has Not been Installed With Python Automatically:

• https://pip.pypa.io/en/stable/installation/

### Install Libraries (please open the command line interface):

• Selenium `pip install selenium`

### Start Connecting with People on LinkedIn!

• double-click on `start.bat`

The fresh version is always here: https://github.com/nakigoe/linkedin-bot
<br> Please write if You would like programming lessons: nakigoetenshi@gmail.com
<br> $60 per hour

<h2 style="margin: 0 auto" align="center">Put stars on GitHub and share!!!</h2>
<br>
<p style="margin: 0 auto" align="center">Please cast an eye on my website:</p>
<h1><a href="https://nakigoe.org/" style="background-color: black;" target="_blank">
  <img style="display: block; width: calc(100vw - (100vw - 100%));"
    src="https://nakigoe.org/_IMG/logo.png" 
    srcset="https://nakigoe.org/_IMG/logo.png 4800w,
      https://nakigoe.org/_SRC/logo-3840.png 3840w,
      https://nakigoe.org/_SRC/logo-2560.png 2560w,
      https://nakigoe.org/_SRC/logo-2400.png 2400w,
      https://nakigoe.org/_SRC/logo-2048.png 2048w,
      https://nakigoe.org/_SRC/logo-1920.png 1920w,
      https://nakigoe.org/_SRC/logo-1600.png 1600w,
      https://nakigoe.org/_SRC/logo-1440.png 1440w,
      https://nakigoe.org/_SRC/logo-1280.png 1280w,
      https://nakigoe.org/_SRC/logo-1200.png 1200w,
      https://nakigoe.org/_SRC/logo-1080.png 1080w,
      https://nakigoe.org/_SRC/logo-960.png 960w,
      https://nakigoe.org/_SRC/logo-720.png 720w,
      https://nakigoe.org/_SRC/logo-600.png 600w,
      https://nakigoe.org/_SRC/logo-480.png 480w,
      https://nakigoe.org/_SRC/logo-300.png 300w"
    alt="NAKIGOE.ORG">
<img class="blend" style="display: block; width: calc(100vw - (100vw - 100%));" 
  src="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg" 
  srcset="https://nakigoe.org/_IMG/nakigoe-academy-night.jpg 2800w,
    https://nakigoe.org/_SRC/nakigoe-academy-night-2048.jpg 2048w"
  alt="Nakigoe Academy">
  <img class="blend" style="display: block; width: calc(100vw - (100vw - 100%)); padding-bottom: 0.05em;"
    src="https://nakigoe.org/_IMG/logo-hot-bevel.png" 
    srcset="https://nakigoe.org/_IMG/logo-hot-bevel.jpg 4800w,
      https://nakigoe.org/_SRC/logo-hot-bevel-3840.jpg 3840w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2560.jpg 2560w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2400.jpg 2400w,
      https://nakigoe.org/_SRC/logo-hot-bevel-2048.jpg 2048w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1920.jpg 1920w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1600.jpg 1600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1440.jpg 1440w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1280.jpg 1280w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1200.jpg 1200w,
      https://nakigoe.org/_SRC/logo-hot-bevel-1080.jpg 1080w,
      https://nakigoe.org/_SRC/logo-hot-bevel-960.jpg 960w,
      https://nakigoe.org/_SRC/logo-hot-bevel-720.jpg 720w,
      https://nakigoe.org/_SRC/logo-hot-bevel-600.jpg 600w,
      https://nakigoe.org/_SRC/logo-hot-bevel-480.jpg 480w,
      https://nakigoe.org/_SRC/logo-hot-bevel-300.jpg 300w"
    alt="NAKIGOE.ORG">
</a></h1>

<p style="margin: 0 auto" align="center">© NAKIGOE.ORG</p>

<p style="margin: 0 auto" align="center">All rights reserved and no permissions are granted.</p>

<p style="margin: 0 auto" align="center">Please add stars to the repositories!</p>
