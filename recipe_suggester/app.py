from flask import Flask, render_template, request

app = Flask(__name__)

# Sample set of recipes with instructions and nutritional information
recipes = {
    "Pasta Salad": {
        "ingredients": ["pasta", "tomato", "cucumber", "olive oil", "feta cheese"],
        "instructions": "1. Cook the pasta and let it cool.\n2. Chop the tomato and cucumber.\n3. Mix all ingredients with olive oil and crumbled feta cheese.",
        "nutrition": {
            "calories": 350,
            "protein": 10,  # grams
            "fat": 15,      # grams
            "carbs": 45     # grams
        }
    },
    "Omelette": {
        "ingredients": ["eggs", "milk", "cheese", "tomato", "onion"],
        "instructions": "1. Beat the eggs with milk.\n2. Pour the mixture into a hot pan.\n3. Add chopped tomato, onion, and cheese.\n4. Cook until the eggs are set.",
        "nutrition": {
            "calories": 250,
            "protein": 18,  # grams
            "fat": 20,      # grams
            "carbs": 5      # grams
        }
    },
    "Pancakes": {
        "ingredients": ["flour", "milk", "egg", "sugar", "baking powder"],
        "instructions": "1. Mix the dry ingredients.\n2. Add milk and egg, and mix until smooth.\n3. Cook on a hot griddle until bubbles form and edges are dry.\n4. Flip and cook until golden brown.",
        "nutrition": {
            "calories": 200,
            "protein": 5,   # grams
            "fat": 8,       # grams
            "carbs": 30     # grams
        }
    },
    "Daal Curry": {
        "ingredients": ["lentils", "tomato", "onion", "garlic", "turmeric", "cumin", "coriander", "salt"],
        "instructions": "1. Cook the lentils until tender.\n2. Sauté onions, garlic, and tomatoes with spices.\n3. Combine lentils and the sautéed mixture. Cook until well blended.",
        "nutrition": {
            "calories": 180,
            "protein": 12,  # grams
            "fat": 2,       # grams
            "carbs": 30     # grams
        }
    },
    "Indian Chicken Curry": {
        "ingredients": ["chicken", "onion", "tomato", "garlic", "ginger", "turmeric", "cumin", "coriander", "garam masala", "coconut milk"],
        "instructions": "1. Sauté onions, garlic, and ginger.\n2. Add spices and cook until fragrant.\n3. Add chicken and cook until browned.\n4. Add tomatoes and coconut milk, simmer until chicken is cooked through.",
        "nutrition": {
            "calories": 400,
            "protein": 30,  # grams
            "fat": 25,      # grams
            "carbs": 10     # grams
        }
    },
    "Naan": {
        "ingredients": ["flour", "yeast", "sugar", "salt", "yogurt", "water"],
        "instructions": "1. Combine flour, yeast, sugar, and salt.\n2. Add yogurt and water to form dough.\n3. Let the dough rise.\n4. Roll out and cook on a hot griddle until puffy and golden brown.",
        "nutrition": {
            "calories": 250,
            "protein": 8,   # grams
            "fat": 4,       # grams
            "carbs": 45     # grams
        }
    },
    "Red Lentil Curry": {
        "ingredients": ["red lentils", "onion", "tomato", "garlic", "ginger", "turmeric", "cumin", "coriander", "coconut milk"],
        "instructions": "1. Cook red lentils until tender.\n2. Sauté onions, garlic, and ginger with spices.\n3. Add tomatoes and coconut milk, simmer until well blended.",
        "nutrition": {
            "calories": 220,
            "protein": 10,  # grams
            "fat": 7,       # grams
            "carbs": 30     # grams
        }
    },
    "Kheer": {
        "ingredients": ["rice", "milk", "sugar", "cardamom", "nuts"],
        "instructions": "1. Cook rice in milk until soft.\n2. Add sugar and cardamom, cook until thickened.\n3. Garnish with nuts.",
        "nutrition": {
            "calories": 300,
            "protein": 8,   # grams
            "fat": 10,      # grams
            "carbs": 45     # grams
        }
    },
    "Chicken Makhani": {
        "ingredients": ["chicken", "tomato", "butter", "cream", "garlic", "ginger", "cumin", "coriander", "garam masala"],
        "instructions": "1. Sauté garlic and ginger with spices.\n2. Add chicken and cook until browned.\n3. Add tomatoes, butter, and cream, simmer until chicken is cooked through.",
        "nutrition": {
            "calories": 450,
            "protein": 28,  # grams
            "fat": 30,      # grams
            "carbs": 15     # grams
        }
    },
    "Chana Masala": {
        "ingredients": ["chickpeas", "onion", "tomato", "garlic", "ginger", "cumin", "coriander", "turmeric", "garam masala"],
        "instructions": "1. Sauté onions, garlic, and ginger with spices.\n2. Add tomatoes and chickpeas, simmer until well blended.",
        "nutrition": {
            "calories": 250,
            "protein": 12,  # grams
            "fat": 8,       # grams
            "carbs": 35     # grams
        }
    },
    "Biryani": {
        "ingredients": ["rice", "chicken", "yogurt", "onion", "tomato", "garlic", "ginger", "turmeric", "cumin", "coriander", "garam masala", "saffron"],
        "instructions": "1. Marinate chicken in yogurt and spices.\n2. Cook onions, garlic, and ginger.\n3. Layer rice and marinated chicken, cook until rice is tender.",
        "nutrition": {
            "calories": 500,
            "protein": 25,  # grams
            "fat": 20,      # grams
            "carbs": 60     # grams
        }
    },
    "Lasagna": {
        "ingredients": ["lasagna noodles", "ground beef", "tomato sauce", "ricotta cheese", "mozzarella cheese", "parmesan cheese", "garlic", "onion"],
        "instructions": "1. Cook lasagna noodles according to package instructions.\n2. Brown ground beef with garlic and onion.\n3. Layer noodles with beef mixture, tomato sauce, ricotta cheese, mozzarella cheese, and parmesan cheese.\n4. Bake in oven until bubbly and cheese is melted.",
        "nutrition": {
            "calories": 450,
            "protein": 30,  # grams
            "fat": 25,      # grams
            "carbs": 35     # grams
        }
    },
    "Stir-fried Noodles": {
        "ingredients": ["noodles", "vegetables (bell pepper, broccoli, carrot)", "soy sauce", "garlic", "ginger", "sesame oil"],
        "instructions": "1. Cook noodles according to package instructions.\n2. Stir-fry garlic and ginger with vegetables in sesame oil.\n3. Add cooked noodles and soy sauce, toss until well combined.",
        "nutrition": {
            "calories": 300,
            "protein": 12,  # grams
            "fat": 10,      # grams
            "carbs": 40     # grams
        }
    },
    "Fish Tacos": {
        "ingredients": ["fish fillets (cod, tilapia)", "tortillas", "cabbage slaw", "avocado", "lime", "cilantro", "sour cream", "cumin", "paprika"],
        "instructions": "1. Season fish with cumin, paprika, and lime juice.\n2. Grill or pan-fry fish until cooked through.\n3. Assemble tacos with grilled fish, cabbage slaw, avocado slices, cilantro, and sour cream.",
        "nutrition": {
            "calories": 350,
            "protein": 25,  # grams
            "fat": 15,      # grams
            "carbs": 30     # grams
        }
    },
    "Caprese Salad": {
        "ingredients": ["tomatoes", "fresh mozzarella cheese", "basil leaves", "olive oil", "balsamic vinegar", "salt", "pepper"],
        "instructions": "1. Slice tomatoes and mozzarella cheese.\n2. Arrange on a plate with basil leaves.\n3. Drizzle with olive oil and balsamic vinegar.\n4. Season with salt and pepper.",
        "nutrition": {
            "calories": 200,
            "protein": 10,  # grams
            "fat": 15,      # grams
            "carbs": 5      # grams
        }
    },
    "Vegetable Curry": {
        "ingredients": ["mixed vegetables (potato, carrot, bell pepper, peas)", "coconut milk", "onion", "garlic", "ginger", "curry powder", "turmeric", "cumin", "coriander", "chili pepper (optional)"],
        "instructions": "1. Sauté onion, garlic, and ginger until fragrant.\n2. Add mixed vegetables and sauté briefly.\n3. Stir in coconut milk and spices, simmer until vegetables are tender.",
        "nutrition": {
            "calories": 250,
            "protein": 8,   # grams
            "fat": 10,      # grams
            "carbs": 35     # grams
        }
    }
}

def suggest_recipe(ingredients):
    possible_recipes = []
    for recipe, details in recipes.items():
        if all(item in ingredients for item in details["ingredients"]):
            possible_recipes.append({
                "name": recipe,
                "ingredients": details["ingredients"],
                "instructions": details["instructions"],
                "nutrition": details["nutrition"]
            })
    
    return possible_recipes

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ingredients = request.form['ingredients'].lower().split(',')
        ingredients = [ingredient.strip() for ingredient in ingredients]
        suggested_recipes = suggest_recipe(ingredients)
        return render_template('index.html', recipes=suggested_recipes, ingredients=request.form['ingredients'])
    return render_template('index.html', recipes=None)

if __name__ == '__main__':
    app.run(debug=True)
