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
    prompt = f'''Give me links to online recipes with these ingredients I list: {ingredients_list}. Prioritize reliable cooking websites with a proven track record. Assume I have common pantry spices. 
    Recipes may include additional ingredients but should primarily focus on the provided list. Exclude links to Allrecipes, BudgetBytes, RecipeTinEats, and FoodNetwork. 
    Return this JSON schema {{"links: [{{"title": "string", "link": "URL"}}]}}
    Maximum 5 links.'''
    response = model.generate_content(prompt)
    return response.text


                                                                       

