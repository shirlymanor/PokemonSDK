from pokemon_sdk import PokeSDK
import streamlit as st

sdk = PokeSDK()
st.title("PokeAPI SDK Example")

pokemon_name = st.text_input("Enter a Pokémon name:", "pikachu")

if st.button("Search"):
    try:
        pokemon = sdk.pokemon.get_pokemon(pokemon_name)
        st.balloons()
        st.write(f"You searched for: {pokemon_name}")
        ''' Display basic information'''
        
        # Display sprite
        if 'sprites' in pokemon and 'front_default' in pokemon['sprites']:
            st.image(pokemon['sprites']['front_default'], caption=f"{pokemon['name'].capitalize()} Sprite")
        
        st.write(f"ID: {pokemon['id']}")
        st.write(f"Height: {pokemon['height']} dm")
        st.write(f"Weight: {pokemon['weight']} hg")
        
        # Display types
        st.write("Types:")
        for type_info in pokemon['types']:
            st.write(f"- {type_info['type']['name'].capitalize()}")
        
        # Display abilities
        st.write("Abilities:")
        for ability in pokemon['abilities']:
            st.write(f"- {ability['ability']['name'].capitalize()}")
        
       
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.snow()
