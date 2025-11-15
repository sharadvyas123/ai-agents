import google.generativeai as genai
genai.configure(api_key='AIzaSyAQUqd9wUIAoSPIfjIg_pnClzE5PoOsc80')

with open("awailable_models.txt" , "w") as f:
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            f.write(m.name + "\n")

print("Successfully saved the list of available models to available_models.txt")