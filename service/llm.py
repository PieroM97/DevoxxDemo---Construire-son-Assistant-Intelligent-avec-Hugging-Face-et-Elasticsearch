from openai import OpenAI
from service.config import Config
import os


config = Config("configuration/config.ini")
openai_config = config.get_openai_config()


os.environ["OPENAI_API_KEY"] = openai_config["api_key"]
os.environ['REQUESTS_CA_BUNDLE'] = 'configuration/Netskope_rootcacert.crt'


def generate_prompt(question, documents, instructions=None):
    prompt = "Instructions:" + instructions + "\n\n"

    prompt += "User Question:" + question + "\n\n"

    for doc in documents['hits']['hits']:
        source = doc['_source']
        title = source.get('title', '')
        description = source.get('description', '')
        tags = ', '.join(source.get('tags', []))

        # Cleaning: Include only relevant information
        cleaned_info = f"Title: {title}\nDescription: {description}\nTags: {tags}\n\n"

        prompt += "Context:" + cleaned_info

    return prompt


def llm_response(model, prompt):

    client = OpenAI()


    stream = client.chat.completions.create(
        model= model,
        messages=[{"role": "user", "content": prompt}],
        stream = True
    )

    return stream


def answer_with_context(question, documents):

    instructions = "You are devoxx assistant. You answer to the user question, given the context. If no context is present you say you have not enough information to answer to the user"

    prompt = generate_prompt(question, documents, instructions)

    return llm_response("gpt-3.5-turbo", prompt)
