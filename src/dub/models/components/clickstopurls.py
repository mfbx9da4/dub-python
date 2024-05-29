"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from dub import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ClicksTopUrls:
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""The destination URL"""
    clicks: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clicks') }})
    r"""The number of clicks from this URL"""
    

