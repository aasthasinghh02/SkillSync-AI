from ai.client import client


response = client.responses.create(
    model="gpt-5.5",
    input="Say hello in one sentence"
)


print(response.output_text)
