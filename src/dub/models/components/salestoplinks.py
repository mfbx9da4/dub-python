"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from dub import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SalesTopLinks:
    link: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link') }})
    r"""The unique ID of the short link

    Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible.
    """
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The unique ID of the short link"""
    domain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain') }})
    r"""The domain of the short link"""
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""The key of the short link"""
    short_link: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('shortLink') }})
    r"""The short link URL"""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""The destination URL of the short link"""
    created_at: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt') }})
    r"""The creation timestamp of the short link"""
    sales: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sales') }})
    r"""The number of sales from this link"""
    amount: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('amount') }})
    r"""The total amount of sales from this link"""
    

