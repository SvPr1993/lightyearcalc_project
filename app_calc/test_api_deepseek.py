from openai import OpenAI

client = OpenAI(api_key="sk-caf78fa452f7470397ba4e47393faefa", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Объясни, как работает рекурсия в программировании."}
    ],
    temperature=0.7,
    max_tokens=1000,
    stream=False
)

print(response.choices[0].message.content)
