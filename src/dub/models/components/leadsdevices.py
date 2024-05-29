"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from dub import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LeadsDevices:
    device: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('device') }})
    r"""The name of the device"""
    leads: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('leads') }})
    r"""The number of leads from this device"""
    

