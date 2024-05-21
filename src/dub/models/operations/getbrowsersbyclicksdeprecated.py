"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import countrycode as components_countrycode
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from dub import utils
from enum import Enum
from typing import List, Optional


@dataclasses.dataclass
class GetBrowsersByClicksDeprecatedGlobals:
    workspace_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'projectSlug', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



class GetBrowsersByClicksDeprecatedQueryParamInterval(str, Enum):
    r"""The interval to retrieve analytics for. Takes precedence over start and end. If undefined, defaults to 24h."""
    ONEH = '1h'
    TWENTY_FOURH = '24h'
    SEVEND = '7d'
    THIRTYD = '30d'
    NINETYD = '90d'
    YTD = 'ytd'
    ONEY = '1y'
    ALL = 'all'


@dataclasses.dataclass
class GetBrowsersByClicksDeprecatedRequest:
    domain: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'domain', 'style': 'form', 'explode': True }})
    r"""The domain to filter analytics for."""
    key: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'key', 'style': 'form', 'explode': True }})
    r"""The short link slug."""
    link_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'linkId', 'style': 'form', 'explode': True }})
    r"""The unique ID of the short link on Dub."""
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'externalId', 'style': 'form', 'explode': True }})
    r"""This is the ID of the link in the your database. Must be prefixed with 'ext_' when passed as a query parameter."""
    interval: Optional[GetBrowsersByClicksDeprecatedQueryParamInterval] = dataclasses.field(default=GetBrowsersByClicksDeprecatedQueryParamInterval.TWENTY_FOURH, metadata={'query_param': { 'field_name': 'interval', 'style': 'form', 'explode': True }})
    r"""The interval to retrieve analytics for. Takes precedence over start and end. If undefined, defaults to 24h."""
    start: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start', 'style': 'form', 'explode': True }})
    r"""The start date and time when to retrieve analytics from."""
    end: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end', 'style': 'form', 'explode': True }})
    r"""The end date and time when to retrieve analytics from. If not provided, defaults to the current date."""
    country: Optional[components_countrycode.CountryCode] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'country', 'style': 'form', 'explode': True }})
    r"""The country to retrieve analytics for."""
    city: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'city', 'style': 'form', 'explode': True }})
    r"""The city to retrieve analytics for."""
    device: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'device', 'style': 'form', 'explode': True }})
    r"""The device to retrieve analytics for."""
    browser: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'browser', 'style': 'form', 'explode': True }})
    r"""The browser to retrieve analytics for."""
    os: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'os', 'style': 'form', 'explode': True }})
    r"""The OS to retrieve analytics for."""
    referer: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'referer', 'style': 'form', 'explode': True }})
    r"""The referer to retrieve analytics for."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'url', 'style': 'form', 'explode': True }})
    r"""The URL to retrieve analytics for."""
    tag_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tagId', 'style': 'form', 'explode': True }})
    r"""The tag ID to retrieve analytics for."""
    qr: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'qr', 'style': 'form', 'explode': True }})
    r"""Filter for QR code scans. If true, filter for QR codes only. If false, filter for links only. If undefined, return both."""
    root: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'root', 'style': 'form', 'explode': True }})
    r"""Filter for root domains. If true, filter for domains only. If false, filter for links only. If undefined, return both."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetBrowsersByClicksDeprecatedResponseBody:
    browser: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('browser') }})
    r"""The name of the browser"""
    clicks: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('clicks') }})
    r"""The number of clicks from this browser"""
    



@dataclasses.dataclass
class GetBrowsersByClicksDeprecatedResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    response_bodies: Optional[List[GetBrowsersByClicksDeprecatedResponseBody]] = dataclasses.field(default=None)
    r"""The top browsers by number of clicks"""
    

