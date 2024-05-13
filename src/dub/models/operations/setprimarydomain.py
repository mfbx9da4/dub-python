"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import domainschema as components_domainschema
from ...models.components import httpmetadata as components_httpmetadata
from typing import Optional


@dataclasses.dataclass
class SetPrimaryDomainGlobals:
    workspace_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'projectSlug', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



@dataclasses.dataclass
class SetPrimaryDomainRequest:
    slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'slug', 'style': 'simple', 'explode': False }})
    r"""The domain name."""
    



@dataclasses.dataclass
class SetPrimaryDomainResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    domain_schema: Optional[components_domainschema.DomainSchema] = dataclasses.field(default=None)
    r"""The domain was set as primary"""
    

