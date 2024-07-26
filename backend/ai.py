import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})


def create_recipe(ingredients):
    ingredients_list = ingredients["ingredients"]
    prompt = f'''Make me a recipe with only these ingredients I list: {ingredients_list}. Assume I have pantry spices.
    Return this JSON schema: {{"title": string, "ingredients": list[Name: item], "steps": list[steps]}}'''
    response = model.generate_content(prompt)
    return response.text


test = {"ingredients": "ribeye, potatoes, mushrooms, broccoli"}
print(create_recipe(test))


                                                                       

