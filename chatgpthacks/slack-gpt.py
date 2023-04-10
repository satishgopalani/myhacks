from slack import RTMClient
import openai

model_to_use="text-davinci-003" # most capable
#model_to_use="text-curie-001"
#model_to_use="text-babbage-001"
#model_to_use="text-ada-001" # lowest token cost

# Load your API key from an environment variable or secret management service
openai.api_key="### INSERT YOUR OPENAI API KEY ###"
slack_bot_token="### INSERT YOUR SLACK BOT TOKEN ###"

def chatGPT(query):
    response = openai.Completion.create(
        model=model_to_use,
        prompt=query,
        temperature=0.8, # Tune this for making response more random (higher values) and more specific (lower values)
        max_tokens=1000 # Max token in response
        )
    return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

@RTMClient.run_on(event="message")
def myslackbot(**payload):
    """
    This function triggers when someone sends
    a message on the slack
    """
    try:
        data = payload["data"]
        web_client = payload["web_client"]
        bot_id = data.get("bot_id", "")

        # If a message is not send by the bot
        if bot_id == "":
            channel_id = data["channel"]

            # Extracting message send by the user on the slack
            query = data.get("text", "")

            (response,usage) = chatGPT(query)

            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id, text=response)
    except Exception as err:
        print(err)

try:
    rtm_client = RTMClient(token=slack_bot_token)
    #rtm_client = RTMClient(token=slack_bot_token)
    print("Bot is up and running!")
    rtm_client.start()
except Exception as err:
    print(err)
