#openAI
import openai


def generateCodeAI(text, language):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=text + " in " + language,
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text

def showOpenAiResponse():
    pass