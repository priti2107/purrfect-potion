from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

app = Ursina()

# Path to models folder
MODELS_DIR = 'models'

# Function to load all models from a folder
def load_models_from_folder(folder_path, position_offset=(0, 0, 0)):
    loaded_entities = []
    for file in os.listdir(folder_path):
        if file.endswith('.gltf'):  # Ursina will auto-load .bin with it
            model_path = os.path.join(folder_path, file).replace("\\", "/")
            entity = Entity(model=model_path, scale=1, position=position_offset)
            loaded_entities.append(entity)
            print(f"Loaded model: {model_path}")
    return loaded_entities

# Create different rooms
def setup_rooms():
    load_models_from_folder(os.path.join(MODELS_DIR, 'bathroom'), position_offset=(0, 0, 0))
    load_models_from_folder(os.path.join(MODELS_DIR, 'bedroom'), position_offset=(5, 0, 0))
    load_models_from_folder(os.path.join(MODELS_DIR, 'kitchen'), position_offset=(-5, 0, 0))
    load_models_from_folder(os.path.join(MODELS_DIR, 'lair'), position_offset=(0, 0, 5))
    load_models_from_folder(os.path.join(MODELS_DIR, 'livingroom'), position_offset=(0, 0, -5))
    load_models_from_folder(os.path.join(MODELS_DIR, 'other'), position_offset=(8, 0, 0))
    load_models_from_folder(os.path.join(MODELS_DIR, 'sky'), position_offset=(0, 0, 0))
    load_models_from_folder(os.path.join(MODELS_DIR, 'collectibles'), position_offset=(3, 0, 3))

# Ground
ground = Entity(model='plane', scale=(50, 1, 50), texture='white_cube', texture_scale=(50, 50), collider='box', color=color.gray)

# Player
player = FirstPersonController()
player.gravity = 0.5
player.cursor.visible = True

Sky()
setup_rooms()

app.run()
