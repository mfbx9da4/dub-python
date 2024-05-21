"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from dub import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrackCustomerRequestBody:
    UNSET='__SPEAKEASY_UNSET__'
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerId') }})
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    customer_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerName'), 'exclude': lambda f: f is TrackCustomerRequestBody.UNSET }})
    r"""Name of the customer in the client's app."""
    customer_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerEmail'), 'exclude': lambda f: f is TrackCustomerRequestBody.UNSET }})
    r"""Email of the customer in the client's app."""
    customer_avatar: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerAvatar'), 'exclude': lambda f: f is TrackCustomerRequestBody.UNSET }})
    r"""Avatar of the customer in the client's app."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrackCustomerResponseBody:
    r"""A customer was tracked."""
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerId') }})
    customer_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerName') }})
    customer_email: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerEmail') }})
    customer_avatar: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerAvatar') }})
    



@dataclasses.dataclass
class TrackCustomerResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    object: Optional[TrackCustomerResponseBody] = dataclasses.field(default=None)
    r"""A customer was tracked."""
    

