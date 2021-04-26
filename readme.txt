# Facebook Group Posting Bot
This python script to automate the posting on the social media website like Facebook.


### What it does:
As it is named, this python script automatically login/logout your Facebook account and posting your text-based content on the Facebook Group Pages you are a member of.

### How does it do or Instructions to use?
- This script requires the latest version of python to do work, also requires some of the python libraries like:
  - selenium
  - JSON if not available
- Once you install the python, sets the environment variables.
- Download FacebookBot Script, and extract it somewhere in the system

- **Required/Important:**
  - Open **fb_credentials.json** in notepad, and replace **yourloginemail** with your Facebook login email address, and email address should come between double-quotes. Also, perform the same thing with **yourpassword**, put your Facebook login password there (should come between double quotes).
  - To post the desire status/text, open the **PostingContents.txt** file in notepad, and add text there (this will not come in the double quotes).
  - Paste all your links of groups in the group_links.txt as **comma separated links ** it will be of the form /groups/123566456/.....
  - After performing the two above steps, run the start_post exe.

### Is it safe to use, and I have given my Facebook credentials?
Yes, it is safe. It will use your credentials to only log in to your account, and all posting process will happen in front of you. Once you run the running command in cmd, it will open separate/another chrome, and do the posting work.
**Warning:** Please don't interact with chrome, which will be opened by the script. You can use your other chrome instance to do your work.


**Credits for chromedriver.exe:**
- Thanks **Google** for creating <a href="https://chromedriver.chromium.org/">ChromeDriver</a> to control the chrome functions.



