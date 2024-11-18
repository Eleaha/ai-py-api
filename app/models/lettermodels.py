import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting
from vertexai.preview.prompts import Prompt

from dotenv import load_dotenv
import os

load_dotenv()

def generate_letter(prompt_variables):
    vertexai.init(project=os.getenv("PROJECT"), location="europe-west2")

    prompt = Prompt(
        prompt_data=[text1],
        model_name="gemini-1.5-flash-002",
        variables=prompt_variables,
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    # Generate content using the assembled prompt. Change the index if you want
    # to use a different set in the variable value list.
    responses = prompt.generate_content(
        contents=prompt.assemble_contents(**prompt.variables[0]),
        stream=True,
    )
    response_string = ""
    for response in responses:
        response_string += response.text

    print(response_string)

    return {"letter": response_string}

text1 = """Please write a complete, ready-to-send formal letter in the style of a letter you would send to a government representitive using only the information provided in this prompt. Do not include any placeholders like [name], [address]. Instead, directly insert the provided information into the letter itself. If any information is "n/a", please ignore or use generic phrasing.

For example, if I provide you with: 
- to: Mr. John Smith
- from: Jane Doe
- Topic: Noise complaints
- Where: Apartment 3B
- Timescale: The past three months
- Emotion: Frustrated

You would generate a complete formal letter which is several couple of paragraphs long, ready to send, using "dear" Mr. John Smith, from Jane Doe about noise complaints coming from Apartment 3B, which have been happening for the past three months, written from a frustrated point of view.

the details are:
- to:{to_name}
- from:{from_name}
- subject:{subject}
- emotion:{emotion}
- location:{location}
- timescale:{timescale}
- when: {when}
- additional: {additional}"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.OFF
    ),
]