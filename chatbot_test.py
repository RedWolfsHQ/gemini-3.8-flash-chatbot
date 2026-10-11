from google import genai
client = genai.Client(api_key="")

def chatbot(topic):
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents = topic
    )
    return response.text

while True:
    topic = input ("what troubles your mind?")
    answer = chatbot(topic)
    print(answer)
