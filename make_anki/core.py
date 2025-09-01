"""
Core functionality for generating Anki cards
"""

def create_card(content: str, model: str = "gpt-3.5-turbo") -> dict:
    """
    Create an Anki card from the given content using the specified LLM model.
    
    Args:
        content: The text content to create a card from
        model: The LLM model to use
        
    Returns:
        dict: A dictionary containing the card front and back
    """
    # TODO: Implement card creation logic
    raise NotImplementedError("Card creation not yet implemented")

def format_card(front: str, back: str) -> dict:
    """
    Format the card content into Anki-compatible format
    
    Args:
        front: The front content of the card
        back: The back content of the card
        
    Returns:
        dict: Formatted card data ready for Anki import
    """
    return {
        "front": front,
        "back": back
    }
