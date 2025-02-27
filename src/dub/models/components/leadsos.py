"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class LeadsOSTypedDict(TypedDict):
    os: str
    r"""The name of the OS"""
    leads: float
    r"""The number of leads from this OS"""
    

class LeadsOS(BaseModel):
    os: str
    r"""The name of the OS"""
    leads: float
    r"""The number of leads from this OS"""
    
