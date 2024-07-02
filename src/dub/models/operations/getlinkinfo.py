"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from typing import Optional


@dataclasses.dataclass
class GetLinkInfoGlobals:
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'projectSlug', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



@dataclasses.dataclass
class GetLinkInfoRequest:
    domain: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'domain', 'style': 'form', 'explode': True }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'key', 'style': 'form', 'explode': True }})
    r"""The key of the link to retrieve. E.g. for `d.to/github`, the key is `github`."""
    link_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'linkId', 'style': 'form', 'explode': True }})
    r"""The unique ID of the short link."""
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'externalId', 'style': 'form', 'explode': True }})
    r"""This is the ID of the link in the your database. Must be prefixed with `ext_` when passed as a query parameter."""
    

