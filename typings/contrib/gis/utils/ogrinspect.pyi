from typing import Any

from django.contrib.gis.gdal import DataSource

def mapping(
    data_source: str | DataSource, geom_name: str = ..., layer_key: int | str = ..., multi_geom: bool = ...
) -> dict[str, str]: ...
def ogrinspect(data_source: str | DataSource, model_name: str, *args: Any, **kwargs: Any) -> str: ...