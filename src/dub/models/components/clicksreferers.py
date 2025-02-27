"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from dub.types import BaseModel
from typing import TypedDict


class ClicksReferersTypedDict(TypedDict):
    referer: str
    r"""The name of the referer. If unknown, this will be `(direct)`"""
    clicks: float
    r"""The number of clicks from this referer"""
    

class ClicksReferers(BaseModel):
    referer: str
    r"""The name of the referer. If unknown, this will be `(direct)`"""
    clicks: float
    r"""The number of clicks from this referer"""
    
