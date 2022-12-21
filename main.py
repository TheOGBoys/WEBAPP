from website import create_app
from dotenv import load_dotenv
import os
#openAI
import openai

def configure():
    load_dotenv()

app = create_app()

configure()
#OpenAI Connection
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.organization = os.getenv('OPENAI_ORGANIZATION_KEY')
openai.Model.list()

if __name__ == '__main__':
    app.run(debug=True, port=8000)