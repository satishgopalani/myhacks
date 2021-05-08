# My Hacks - To make our daily life bit easier


## Vaccine Checker
You can use vaccineAvailChecker.py script to check if a slot is available for booking vaccine slot.
You need to just edit the script and add below details.

1. One or more pincodes you want to track.

> pincodes=["201301"]

More Examples:

pincodes=["683575","683574","683101"]

pincodes=["411017","411018","411019","411026","411027","411033","411035","411044","411057"]

2. Add age limit you want to track, 18 for 18-44 slots and 45 for 45+ age slots.

> age_limit=18


3. Gmail User using which you want to send email

Replace xxx by your gmail address and ppppp by your gmail password

Note: Make sure your turn on setting on this [link](https://myaccount.google.com/lesssecureapps) to be able to send email 

> gmail_user = "xxx@gmail.com"

> gmail_password = "ppppp"

4. Gmail address where you want to send email. Replace xxxxx by your gmail address

Note this could same as gmail_user

> to = "xxxxx@gmail.com"

### Deployment:
This python script has been test with python version 3+

You can schedule this script in crontab as below:

Checks every 2 mins for slot:
> */2 * * * * python3 vaccineAvailChecker.py >> ~/vaccineAvailChecker.py.log 2>&1
