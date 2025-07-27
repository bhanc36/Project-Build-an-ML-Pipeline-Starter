import pandas as pd
import numpy as np

def test_row_count():
    """Test the cleaned data"""
    df = pd.read_csv("clean_sample.csv")
    min_rows, max_rows = 12000, 500000
    assert min_rows < df.shape[0] < max_rows, f"{df.shape[0]} rows not in expected range"

def test_price_range():
    """Test all prices within configured limits"""
    df = pd.read_csv("clean_sample.csv")
    min_price, max_price = 15, 400
    out_of_bounds = df.loc[~df['price'].between(min_price, max_price)]
    assert out_of_bounds.empty, f"{out_of_bounds.shape[0]} rows with prices out of range."

def test_longitude_latitude_nyc():
    """Check within NYC"""
    df = pd.read_csv("clean_sample.csv")
    nyc_lon_bounds = (-74.3, -73.4)
    nyc_lat_bounds = (40.45, 41.3)
    bad_coords = df.loc[
        ~df['longitude'].between(*nyc_lon_bounds) |
        ~df['latitude'].between(*nyc_lat_bounds)
    ]
    assert bad_coords.empty, f"{bad_coords.shape[0]} rows outside NYC bounds!"

def test_no_missing_critical_columns():
    """Verify missing values in columns for modeling."""
    df = pd.read_csv("clean_sample.csv")
    critical_columns = ['price', 'room_type', 'neighbourhood', 'latitude', 'longitude']
    for col in critical_columns:
        assert df[col].notnull().all(), f"Column '{col}' contains missing values."

def test_unique_listing_ids():
    """Validate unique IDs."""
    df = pd.read_csv("clean_sample.csv")
    assert df['id'].is_unique, "There are duplicate listing IDs in the data."