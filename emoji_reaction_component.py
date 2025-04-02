import streamlit as st
import pandas as pd
import json
import os
import time
from datetime import datetime

def emoji_reaction_component(title="How did you like this?", 
                            emojis=["👍", "❤️", "😄", "🎉", "🤔"], 
                            key="default",
                            save_to_file=True):
    """
    Create a component for emoji reactions in Streamlit
    
    Parameters:
    title (str): Title to display above the reaction buttons
    emojis (list): List of emojis to use as reaction options
    key (str): Unique key for this component instance
    save_to_file (bool): Whether to save reactions to a CSV file
    
    Returns:
    dict: Dictionary with counts of each emoji reaction
    """
    # Initialize session state for storing reactions if it doesn't exist
    if f"reactions_{key}" not in st.session_state:
        st.session_state[f"reactions_{key}"] = {emoji: 0 for emoji in emojis}
    
    # Display the title
    st.write(f"### {title}")
    
    # Create columns for each emoji button
    cols = st.columns(len(emojis))
    
    # Display the emoji buttons
    for i, emoji in enumerate(emojis):
        # Show current count
        reaction_count = st.session_state[f"reactions_{key}"][emoji]
        
        # Create the button with the emoji and count
        if cols[i].button(f"{emoji} {reaction_count}", key=f"{key}_{emoji}"):
            # Increment the count when clicked
            st.session_state[f"reactions_{key}"][emoji] += 1
            
            # Save reaction to file if enabled
            if save_to_file:
                save_reaction(key, emoji)
            
            # Force a rerun to update the UI immediately
            st.rerun()
    
    # Initialize refresh counter if not exists
    if "refresh_counter" not in st.session_state:
        st.session_state.refresh_counter = 0

    # Increment counter every 5 seconds to force refresh
    st.session_state.refresh_counter = int(time.time() / 5)

    # Display latest reactions (this will update every 5 seconds)
    reaction_counts = get_reaction_stats(key)
    st.write(f"Latest reactions: {reaction_counts}")
    
    # Return the current reactions
    return st.session_state[f"reactions_{key}"]

def save_reaction(component_key, emoji):
    """Save a reaction to a CSV file with timestamp"""
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")
    
    # Create or append to the reactions file
    filename = f"data/reactions_{component_key}.csv"
    
    # Create a new dataframe for this reaction
    new_reaction = pd.DataFrame({
        'timestamp': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'emoji': [emoji]
    })
    
    # Append to existing file or create new one
    if os.path.exists(filename):
        reactions_df = pd.read_csv(filename)
        reactions_df = pd.concat([reactions_df, new_reaction])
    else:
        reactions_df = new_reaction
    
    # Save to CSV
    reactions_df.to_csv(filename, index=False)


def get_reaction_stats(key="default"):
    """Get statistics about reactions for a component"""
    filename = f"data/reactions_{key}.csv"
    
    if os.path.exists(filename):
        reactions_df = pd.read_csv(filename)
        return reactions_df['emoji'].value_counts().to_dict()
    else:
        return {}
    
    