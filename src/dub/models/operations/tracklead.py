"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from dub import utils
from typing import Any, Dict, Optional


@dataclasses.dataclass
class TrackLeadGlobals:
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'projectSlug', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrackLeadRequestBody:
    UNSET='__SPEAKEASY_UNSET__'
    click_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clickId') }})
    r"""The ID of the click in th Dub. You can read this value from `dclid` cookie."""
    event_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eventName') }})
    r"""The name of the event to track."""
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerId') }})
    r"""This is the unique identifier for the customer in the client's app. This is used to track the customer's journey."""
    customer_name: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerName'), 'exclude': lambda f: f is TrackLeadRequestBody.UNSET }})
    r"""Name of the customer in the client's app."""
    customer_email: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerEmail'), 'exclude': lambda f: f is TrackLeadRequestBody.UNSET }})
    r"""Email of the customer in the client's app."""
    customer_avatar: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerAvatar'), 'exclude': lambda f: f is TrackLeadRequestBody.UNSET }})
    r"""Avatar of the customer in the client's app."""
    metadata: Optional[Dict[str, Any]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is TrackLeadRequestBody.UNSET }})
    r"""Additional metadata to be stored with the lead event"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrackLeadResponseBody:
    r"""A lead was tracked."""
    click_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clickId') }})
    event_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('eventName') }})
    customer_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerId') }})
    customer_name: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerName') }})
    customer_email: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerEmail') }})
    customer_avatar: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerAvatar') }})
    metadata: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TrackLeadResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    object: Optional[TrackLeadResponseBody] = dataclasses.field(default=None)
    r"""A lead was tracked."""
    

