from .spellbook import record_spell
def validate_ingredients(ingredients: str) -> str:
      valid_elements = ["fire", "water", "earth", "air"]
      for element in valid_elements:
          if element in ingredients:
              return f"{ingredients} - VALID"
      return f"{ingredients} - INVALID"