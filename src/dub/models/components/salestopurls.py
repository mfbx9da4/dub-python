"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from dub import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SalesTopUrls:
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""The destination URL"""
    sales: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sales') }})
    r"""The number of sales from this URL"""
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The total amount of sales from this URL"""
    

