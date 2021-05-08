import smtplib
import json
import urllib.request
from datetime import date
from datetime import timedelta 
from datetime import datetime

################## User Input changes start ##################

# Adding one or more pincodes you want to track
pincodes=["201301"]

#Examples:
#pincodes=["683575","683574","683101"]
#pincodes=["411017","411018","411019","411026","411027","411033","411035","411044","411057"]

# Add age limit you want to track, 18 for 18-44 slots and 45 for 45+ age slots
age_limit=18

# Gmail User using which you want to send email
# Replace xxx by your gmail address
# and ppppp by your gmail password
# Note: Make sure your turn on setting on below link to be able to send email
# Link: https://myaccount.google.com/lesssecureapps

gmail_user = "xxx@gmail.com"
gmail_password = "ppppp"

# Gmail address where you want to send email. Replace xxxxx by your gmail address 
# Note this could same as gmail_user
to = "xxxxx@gmail.com"

################## User Input changes END ##################

def sendMail(gmail_user, gmail_password, to, subject, body):
    email_text = """\
From: %s
To: %s
Subject: %s
    
%s
""" % (gmail_user, to, subject, body)
    
    print(email_text)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, email_text)
        server.close()
    
        print('Email sent!')
    except:
        print('Something went wrong...')

def checkVaccineAvailability(pincodes, age_limit, days_to_check):
    today = date.today()
    for nextday in range(0,days_to_check):
        chkdate = (today + timedelta(days=nextday)).strftime("%d-%m-%Y")
        for pincode in pincodes:
            url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=" + pincode + "&date=" + chkdate

            req = urllib.request.Request(url,headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'})
    
            data = urllib.request.urlopen(req).read().decode()
            obj = json.loads(data)
    
            sessions = obj['sessions']
            for session in sessions:
                if session['min_age_limit'] == age_limit and session['available_capacity'] > 0:
                    sdata="Vaccine available for " + str(session['min_age_limit']) + "+ at - " + session['name'] + " on " + session['date'] + " pincode - " + pincode + " - Capacity - " + str(session['available_capacity'])
                    return sdata,pincode
    return "",0


def main():
    days_to_check = 3
    avlvaccine,pincode = checkVaccineAvailability(pincodes, age_limit, days_to_check)
    if avlvaccine != "":
        subject = "Vaccine Available - " + str(pincode)
        sendMail(gmail_user, gmail_password, to, subject, avlvaccine)
    else:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " : No Vaccine slot found...")

main()
