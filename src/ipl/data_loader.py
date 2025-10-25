"""
Data utilities for loading and processing IPL data.
"""

import os
import pandas as pd


def _validate_file_path(filepath):
    """
    Validate that the filepath exists and is a readable file.
    
    Args:
        filepath (str): Path to validate
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the path is not a file
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    if not os.path.isfile(filepath):
        raise ValueError(f"Path is not a file: {filepath}")


def load_match_data(filepath):
    """
    Load match data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Match data
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file is not readable
    """
    _validate_file_path(filepath)
    return pd.read_csv(filepath)


def load_player_data(filepath):
    """
    Load player data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Player data
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file is not readable
    """
    _validate_file_path(filepath)
    return pd.read_csv(filepath)
