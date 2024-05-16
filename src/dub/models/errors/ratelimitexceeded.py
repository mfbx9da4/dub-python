"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from dub import utils
from enum import Enum
from typing import Optional


class RateLimitExceededCode(str, Enum):
    r"""A short code indicating the error code returned."""
    RATE_LIMIT_EXCEEDED = 'rate_limit_exceeded'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RateLimitExceededError:
    code: RateLimitExceededCode = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('code') }})
    r"""A short code indicating the error code returned."""
    message: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message') }})
    r"""A human readable explanation of what went wrong."""
    doc_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doc_url'), 'exclude': lambda f: f is None }})
    r"""A link to our documentation with more details about this error code"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RateLimitExceeded(Exception):
    r"""The user has sent too many requests in a given amount of time (\\"rate limiting\\")"""
    error: RateLimitExceededError = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error') }})
    

    def __str__(self) -> str:
        return utils.marshal_json(self, type(self))
