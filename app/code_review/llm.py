import openai

openai.api_key = 'your-api-key'

def process_text(text):
    # Тестовая LLM обработка текста
    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        max_tokens=50,
    )
    return response.choices[0].text.strip()

