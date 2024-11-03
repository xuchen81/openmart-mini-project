import os

from html_minifier import clean_html
from utils import read_file, write_to_file, int_to_base62
from openai import OpenAI
import json
from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv('OPENAI_KEY')

client = OpenAI(api_key=API_KEY)


def test():
    content = read_file("./test_pages/page2.html")
    cleaned, classNames = clean_html(content)
    print(content)
    print("-" * 10)
    print(cleaned)
    print(classNames)
    write_to_file('./test_pages/page2_cleaned.html', cleaned)


# def testAi():
#     with open('./prompts/analyze_html.txt', 'r') as file:
#         prompt = file.read()

#     content = read_file("./test_pages/page2_cleaned.html")
#     prompt = prompt.replace("{{ html_content }}", content)

#     print(prompt)


def get_openai_response():
    system_prompt = read_file('./prompts/analyze_html_v2.txt')

    user_content = read_file("./test_pages/page2_cleaned.html")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_content}
    ]

    print(messages)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        response_format={"type": "json_object"},
    )

    print(json.dumps(response.to_dict(), indent=2))
    print(response.choices[0].message.content)
    response_dict = json.loads(response.choices[0].message.content)
    print(response_dict)

    return response


# testAi()

get_openai_response()
