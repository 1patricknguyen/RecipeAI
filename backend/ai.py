import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash', generation_config={"response_mime_type": "application/json"})


def create_recipe(ingredients):
    ingredients_list = ingredients["ingredients"]
    prompt = f'''Make me a recipe with only these ingredients I list: {ingredients_list}. Assume I have pantry spices.
    Return this JSON schema: {{"title": string, "ingredients": list[Name: string (with quantities)], "steps": list[steps]}}'''
    response = model.generate_content(prompt)
    return response.text



def link_recipe(ingredients):
    ingredients_list = ingredients["ingredients"]
    prompt = f'''Give me links to online recipes with these ingredients I list: {ingredients_list}. Assume I have pantry spices. Additionally, these
    recipes could have additional ingredients but try to keep it mostly within the list.
    Return this JSON schema {{"links: [{{"title": "string", "link": "URL"}}]}}
    Maximum 5 links.'''
    response = model.generate_content(prompt)
    return response.text

ing = {"ingredients": "chicken, rice, soy sauce, garlic, ginger, green onions, sesame oil, sugar, cornstarch, vinegar, salt, pepper, oil"}
print(create_recipe(ing))
                                                                       

