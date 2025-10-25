"""
Data utilities for loading and processing IPL data.
"""

import pandas as pd


def load_match_data(filepath):
    """
    Load match data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Match data
    """
    return pd.read_csv(filepath)


def load_player_data(filepath):
    """
    Load player data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Player data
    """
    return pd.read_csv(filepath)
