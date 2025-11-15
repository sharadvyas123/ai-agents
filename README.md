### Welcome to my Collcetions of Ai agents 

in this repo i have created 10 different Ai agents using Langgraph 
this is how i had learned and understood about Langgraph



# How to get started 
1. clone this repo
2. create a venv
```bash
python -3.13 -m venv venv
```

3. activate the venv
```bash
# for windows powershell

.venv\Scripts\activate

# for linux or mac
source venv/bin/activate
```

4. install the dependencies
```bash
pip install -r requirements.txt
```

5. setup the .env file
```txt
GOOGLE_API_KEY='your_google_api_key'
```

6. run the agents and explore and chatbot as well

# one note if you have openai api key then

change the imports from
```python
from langchain_google_genai import ChatGoogleGenerativeAI
# to
from langchain_openai import ChatOpenAI
```

and then go on


### by the way the api key in this repo is closed so you need to use your own api key :D
