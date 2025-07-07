from openai import OpenAI

# Initialize the client with your API key
client = OpenAI(api_key="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")  # Replace with your actual key

# Call the chat completion
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello, what can you do?"}
    ]
)

# Print the response content
print(response.choices[0].message.content)