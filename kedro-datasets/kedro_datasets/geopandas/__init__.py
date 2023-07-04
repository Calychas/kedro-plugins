"""``GeoJSONDataSet`` is an ``AbstractVersionedDataSet`` to save and load GeoJSON files.
"""
__all__ = ["GeoJSONDataSet", "ParquetDataSet", "FeatherDataSet"]

from contextlib import suppress

with suppress(ImportError):
    from .feather_dataset import FeatherDataSet
    from .geojson_dataset import GeoJSONDataSet
    from .parquet_dataset import ParquetDataSet
