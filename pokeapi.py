

import os 
import requests as req
from image_lib2 import download_image, save_image_file

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon' 

def fetch_poke_info(poke_name):
    """
    Retrieves Pokemon Information
    """
    # Clean up the Pokemon input
    clean_name = poke_name.strip()
    clean_name = clean_name.lower()

    # Check the API for that pokemon
    poke_info = req.get(f'https://pokeapi.co/api/v2/pokemon/{clean_name}')
    # Check if the reponse succeded
    if poke_info.status_code == req.codes.ok:
        print('Success')
        poke_dict = poke_info.json()
        return poke_dict

def get_pokemon_names(offset=0, limit=100000):
    """
    Get all of the pokemon names from the pokeapi 
    """
    query_str_params = {
        'limit': limit,
        'offset': offset
    }

    print(f'Getting list of Pokemon names...', end='')
    resp_msg = req.get(POKE_API_URL, params=query_str_params)

    if resp_msg.status_code == req.codes.ok:
        resp_dict = resp_msg.json()
        name_lst = [val['name'] for val in resp_dict['results']]
        print('Success')
        return name_lst
    else:
        print('Failure')
        print(f'Response code: {resp_msg.status_code} ({resp_msg.reason})')
        return None 

def download_pokemon_artwork(pokemon_name, save_dir):
    """
    Download and save the pokemon images
    """
    # Get the pokemon's info dict 
    pokemon_info = fetch_poke_info(pokemon_name)
    if pokemon_info is None:
        return 
    
    # Url to the image 
    artwork_url = pokemon_info['sprites']['other']['official-artwork']['front_default']
    # Download the image 
    img_bin = download_image(artwork_url)

    # Check if it was successful 
    if img_bin is None:
        return 
    
    # Get the image type from the end of the url 
    file_ext = artwork_url.split('.')[-1]
    # Create the path to save the file and save the file
    image_path = os.path.join(save_dir, f'{pokemon_name}.{file_ext}')
    save_image_file(img_bin, image_path)

main()

