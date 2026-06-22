import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6I6wdnJxJc6qYimFzJMiCG234s15J1X1Gy5Fyy0onCazg")

for m in genai.list_models():
    print(m.name)