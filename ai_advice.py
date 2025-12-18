import openai
from config import config

openai.api_key = config.OPENAI_API_KEY

async def get_clothing_advice(weather_text: str) -> str:
    prompt = (
        "На основе погоды дай короткий совет по одежде.\n"
        "Пиши по-русски, 1–2 предложения.\n\n"
        f"{weather_text}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты помощник, который советует одежду по погоде."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=80,
            temperature=0.6
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return "Не удалось получить совет по одежде 🤖"
