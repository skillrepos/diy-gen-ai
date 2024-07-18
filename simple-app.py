from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="n-a")

completion = client.chat.completions.create(
    model="local_model",
    messages=[
        { "role": "system", "content": "Always answer in the form of a poem, but keep it brief." },
        { "role": "user", "content": "Tell me about yourself." }
    ],
    temperature=2.0
)

print(completion.choices[0].message.content)
