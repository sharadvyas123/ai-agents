from openai import OpenAI

client = OpenAI(api_key="your_api_key_here")

models = client.models.list()

with open("awailable_openai_model.txt" , "w") as f : 
    for m in models:
        f.write(m.id +"\n")