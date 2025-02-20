import typer

from application.character_creator import CharacterCreator
from application.character_inspector import CharacterInspector
from application.character_remover import CharacterRemover
from domain.entities.schemas import CharacterSchema
from infra.repositories.sql.character_repository import CharacterRepository

app = typer.Typer(
    help="""
Character CRUD CLI

This console interface allows you to manage characters with the following functionalities:\n
\n
- 📜 **list-characters**: Lists all stored characters.\n
- 🔍 **get-character**: Retrieves a specific character by its ID.\n
- ➕ **add-character**: Creates a new character by providing the necessary data.\n
- 🗑️ **delete-character**: Deletes an existing character by its ID.\n\n

Example usage:\n\n

    python app.py list-characters\n
    python app.py get-character 1\n
    python app.py add-character --name "Luke" --height 172 --mass 77 --hair-color "blond" --skin-color "fair" --eye-color "blue" --birth-year 19\n
    python app.py delete-character 1\n
"""
)


@app.command(help="📜 Lists all registered characters.")
def list_characters():
    """List all characters."""
    character_inspector = CharacterInspector(CharacterRepository())
    try:
        characters = character_inspector.list_characters()
        for character in characters:
            typer.echo(character.model_dump_json(indent=2))
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}")


@app.command(help="🔍 Retrieves a character by its ID.")
def get_character(
    character_id: int = typer.Argument(
        ..., help="ID of the character to retrieve."
    )
):
    """
    Get a character by ID.

    Args:
        character_id (int): The ID of the character.
    """
    character_inspector = CharacterInspector(CharacterRepository())
    try:
        character = character_inspector.get_character(character_id)
        if character:
            typer.echo(character.model_dump_json(indent=2))
        else:
            typer.echo("⚠️ Character not found.")
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}")


@app.command(
    help="➕ Creates a new character by providing the necessary data."
)
def add_character(
    name: str = typer.Option(..., help="Character's name."),
    height: float = typer.Option(..., help="Character's height (in cm)."),
    mass: float = typer.Option(..., help="Character's mass (in kg)."),
    hair_color: str = typer.Option(..., help="Character's hair color."),
    skin_color: str = typer.Option(..., help="Character's skin color."),
    eye_color: str = typer.Option(..., help="Character's eye color."),
    birth_year: int = typer.Option(..., help="Character's year of birth."),
):
    """
    Add a new character.

    Args:
        name (str): Character's name.
        height (float): Character's height (in cm).
        mass (float): Character's mass (in kg).
        hair_color (str): Character's hair color.
        skin_color (str): Character's skin color.
        eye_color (str): Character's eye color.
        birth_year (int): Character's year of birth.
    """
    character_creator = CharacterCreator(CharacterRepository())
    try:
        input_data = CharacterSchema(
            id=None,
            name=name,
            height=height,
            mass=mass,
            hair_color=hair_color,
            skin_color=skin_color,
            eye_color=eye_color,
            birth_year=birth_year,
        )
        character = character_creator.create_character(input_data)
        typer.echo("✅ Character created successfully:")
        typer.echo(character.model_dump_json(indent=2))
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}")


@app.command(help="🗑️ Deletes a character by its ID.")
def delete_character(
    character_id: int = typer.Argument(
        ..., help="ID of the character to delete."
    )
):
    """
    Delete a character by ID.

    Args:
        character_id (int): The ID of the character.
    """
    character_remover = CharacterRemover(CharacterRepository())
    try:
        removed = character_remover.remove_character(character_id)
        if removed:
            typer.echo("✅ Character deleted successfully.")
        else:
            typer.echo("⚠️ Character not found.")
    except Exception as e:
        typer.echo(f"❌ Error: {str(e)}")
