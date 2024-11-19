import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'Give me a concise explainer on how humans can establish a permanent presence on the moon'
    }],
    stream=True
)

for chunk in response:
    print(chunk['message']['content'], end='', flush=True)
