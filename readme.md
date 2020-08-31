# Foodie Chatbot
Conversational Chatbot for Restaurant Search

Chatbots have become popular in a large number of business domains. Companies are building chatbots for booking hotels, flights, movies etc., customer support, enquiring bus and train schedules, tax saving advice, accessing stock market information etc.

There are two broad types of chatbots - generic chatbots and domain-specific chatbots.

Generic chatbots, also called virtual assistants, such as Google Assistant, Amazon’s Alexa, Microsoft’s Cortana or Apple’s Siri, are used to answer generic queries such as dialling a phone number, dropping a message to a contact, booking a calendar slot, fetching results from a web search, etc. These systems have been trained on massive amounts of user data, encyclopedias, conversational dialogues with humans etc. 

The other type is the domain-specific, task-oriented chatbot. By domain-specific and task-oriented, we mean that it can handle queries pertaining to a particular domain or type of task. For example, a ‘weather bot’ can only tell weather predictions. It cannot book a table in a restaurant or set up an alarm. Similarly, a restaurant discovery bot can help you find restaurants in several cities, though it might not be able to answer general questions such as "Who is the prime minister of India?".

#### Problem Statement

An Indian startup named 'Foodie' wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities. The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.

The bot takes the following inputs from the user:

- City: Take the input from the customer as a text field. For example:

        Bot: In which city are you looking for restaurants?
        User: anywhere in Delhi
        
Assume that Foodie works only in Tier-1 and Tier-2 cities. We can use the current HRA classification of the cities from third-party source. Your chatbot should provide results for tier-1 and tier-2 cities only, while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".

- Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that.
Following is an example for the same:

        Bot: What kind of cuisine would you prefer?
                
        Chinese
        Mexican
        Italian
        American
        South Indian
        North Indian
        User: I’ll prefer Italian!

- Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. The bot should ask the user to select one of the three price categories. For example:

        Bot: What price range are you looking at?

        Lesser than Rs. 300
        Rs. 300 to 700
        More than 700
        User: in range of 300 to 700

While showing the results to the user, the bot should display the top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). The format should be: {restaurant_name} in {restaurant_address} has been rated {rating}.

Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email. Else, just reply with a 'goodbye' message.

### Building ChatBot using RASA

We are going to use an open source framework for building conversational bots  - RASA.

RASA - An open source Conversational AI is a set of machine learning tools for developers to create contextual text and voice-based chatbots and assistants.

Apple’s Siri, Amazon’s Alexa etc. are much more than a 'speech-based search engine'. Apart from searching for information (e.g. from Wikipedia, YouTube, Google etc.), they can 'talk' to us in natural language. 

Conversation, or dialogue, is a very fundamental aspect of human language, and arguably the most interesting challenge in building truly intelligent NLP systems. A step towards building such systems is domain specific, text-based chatbots used by organisations for tasks such as booking hotels, retrieving stock market information, resolving customer queries etc.

Any conversational system has primarily two components -
 - Natural Language Understanding, or NLU
 - A Dialogue Management System which carries out the overall conversation.
 
In Rasa, these two components are named Rasa NLU and Rasa Core respectively.

Rasa NLU is the tool used for intent classification and entity extraction.

Rasa Core, the dialogue management layer of Rasa, takes structured input in the form of intents and entities (i.e. the output of Rasa NLU) and decides the next actions.

### Dependencies with Version: 
absl-py==0.9.0
aiofiles==0.5.0
aiohttp==3.6.2
alembic==1.4.2
APScheduler==3.6.3
astor==0.8.1
async-generator==1.10
async-timeout==3.0.1
attrs==19.3.0
blis==0.2.4
boto3==1.14.48
botocore==1.17.48
cachetools==4.1.1
certifi==2020.6.20
cffi==1.14.2
chardet==3.0.4
cloudpickle==1.3.0
colorclass==2.2.0
coloredlogs==10.0
colorhash==1.0.2
cryptography==2.9.2
cycler==0.10.0
cymem==2.0.3
decorator==4.4.2
dnspython==1.16.0
docopt==0.6.2
docutils==0.15.2
en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-2.1.0/en_core_web_md-2.1.0.tar.gz
fbmessenger==6.0.0
future==0.18.2
gast==0.2.2
gevent==1.5.0
gitdb==4.0.5
GitPython==3.1.7
google-auth==1.20.1
google-auth-oauthlib==0.4.1
google-pasta==0.2.0
greenlet==0.4.16
grpcio==1.31.0
h11==0.8.1
h2==3.2.0
h5py==2.10.0
hpack==3.0.0
hstspreload==2020.8.25
httplib2==0.18.1
httptools==0.1.1
httpx==0.9.3
humanfriendly==8.2
hyperframe==5.2.0
idna==2.10
importlib-metadata==1.7.0
isodate==0.6.0
jmespath==0.10.0
joblib==0.16.0
jsonpickle==1.4.1
jsonschema==3.2.0
kafka-python==1.4.7
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
kiwisolver==1.2.0
Mako==1.1.3
Markdown==3.2.2
MarkupSafe==1.1.1
matplotlib==3.2.2
mattermostwrapper==2.2
multidict==4.7.6
murmurhash==1.0.2
networkx==2.4
numpy==1.19.1
oauth2client==4.1.3
oauthlib==3.1.0
opt-einsum==3.3.0
packaging==20.4
pika==1.1.0
plac==0.9.6
preshed==2.0.1
prompt-toolkit==2.0.10
protobuf==3.13.0
psycopg2-binary==2.8.5
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
pydot==1.4.1
PyJWT==1.7.1
pykwalify==1.7.0
pymongo==3.8.0
pyparsing==2.4.7
pyrsistent==0.16.0
PySocks==1.7.1
python-crfsuite==0.9.7
python-dateutil==2.8.1
python-editor==1.0.4
python-engineio==3.12.1
python-socketio==4.5.1
python-telegram-bot==12.8
pytz==2019.3
PyYAML==5.3.1
questionary==1.5.2
rasa==1.10.11
rasa-sdk==1.10.2
rasa-x==0.32.0
redis==3.5.3
regex==2020.6.8
requests==2.24.0
requests-oauthlib==1.3.0
requests-toolbelt==0.9.1
rfc3986==1.4.0
rocketchat-API==1.3.1
rsa==4.6
ruamel.yaml==0.16.10
ruamel.yaml.clib==0.2.0
s3transfer==0.3.3
sanic==19.12.2
Sanic-Cors==0.10.0.post3
sanic-jwt==1.3.2
Sanic-Plugins-Framework==0.9.3
scikit-learn==0.22.2.post1
scipy==1.4.1
six==1.15.0
sklearn-crfsuite==0.3.6
slackclient==2.8.0
smmap==3.0.4
sniffio==1.1.0
spacy==2.1.9
SQLAlchemy==1.3.19
srsly==1.0.2
tabulate==0.8.7
tensorboard==2.1.1
tensorflow==2.1.1
tensorflow-addons==0.7.1
tensorflow-estimator==2.1.0
tensorflow-hub==0.8.0
tensorflow-probability==0.9.0
termcolor==1.1.0
terminaltables==3.1.0
thinc==7.0.8
tornado==6.0.4
tqdm==4.45.0
twilio==6.26.3
typing-extensions==3.7.4.3
tzlocal==2.1
ujson==1.35
urllib3==1.25.10
uvloop==0.14.0
wasabi==0.8.0
wcwidth==0.2.5
webexteamssdk==1.3
websockets==8.1
Werkzeug==1.0.1
wrapt==1.12.1
yarl==1.5.1
zipp==3.1.0