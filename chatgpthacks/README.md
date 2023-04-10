# Chat GPT Hacks
Quick Chat GPT hacks to make accessing Chat GPT more easier

Prequisite for both Hacks Slack GPT and Voice GPT is Open AI API token

1. Navigate to https://platform.openai.com/signup and sign up
2. Navigate to https://platform.openai.com/account/api-keys and click Create new secret key button
<img width="881" alt="image" src="https://user-images.githubusercontent.com/1044003/230877211-3d09c507-37b4-4502-857e-20c6124e728a.png">
3. Copy the key 

====================================================================================================

## Slack GPT
Slack Bot for accessing ChatGPT over slack

Before we start let's create a slack App.

#### Slack APP
Let's create a slack app first
1. Hit this link (https://api.slack.com/apps?new_classic_app=1) that redirects you to creating a classic slack app. 
2. Sign in to slack if you are not, click on Create New App and give your slack app a name and the workspace in which you want to install your app.
3. Add Legacy Bot User by clicking on "Add Legacy User Bot" button and enter a Display Name and a default username for your bot. The display name will be the name of the bot that will appear on the slack workspace. Choose any display name and the default name for the bot of your choice.
![image](https://user-images.githubusercontent.com/1044003/230877496-fc9a8412-19b5-421f-a6b2-c334df975a5d.png)

![image](https://user-images.githubusercontent.com/1044003/230877367-e876eb6d-16aa-4aea-bf88-fedba9c475b4.png)

4. Get the Bot User OAuth Access Token of the slack app so that we can receive events from the slack from our python script. So, navigate to the OAuth & Permissions tab from the sidebar of your app and then install the app on your workspace. After you install the app, you will get the OAuth tokens. Copy the Bot User OAuth Access Token.
![image](https://user-images.githubusercontent.com/1044003/230877420-aa392580-8219-44da-82d9-ccbb75e53a1a.png)


Just for a recap: we have created a classic slack app. We have then defined the features and functionalities our slack app is going to perform, given scopes to the app and lastly we have given our bot different kinds of name, duh!

#### Running the Slack Bot

Now, we will move ahead with our python script (slack-gpt.py). The python script will basically read the messages from the slack, send it to Chat GPT and sends back response from Chat GPT to the user.

But before that install slack client library that interfaces with the slack’s Real-Time Messaging (RTM) API using pip.

"pip install slackclient"

Now get copy of slack-gpt.py script and add OPENAI API token and Slack Bot token in below lines in script:
openai.api_key="### INSERT YOUR OPENAI API KEY ###"
slack_bot_token="### INSERT YOUR SLACK BOT TOKEN ###"

Use below command to start the Slack Bot:

python3 /Users/satish/bigdata/chatgpt/slackbot.py

====================================================================================================

## Voice Assistant with Chat GPT

Here, I'm using Google speech Recognition library to detect voice and mpg123 library to play audio 
1. Execute below commands to install both
pip3 install SpeechRecognition
brew install mpg123

2. Create a copy of 'voice-gpt.py' and add Open AI secret key in script at below declaration:
openai.api_key="### INSERT YOUR OPENAI API KEY ###"

3. Use below command to activate Voice GPT. When prompted "Say Somethhing!" ask any question and bot will read out answer from Chat GPT response.
python3 /Users/satish/bigdata/chatgpt/voice-gpt.py


