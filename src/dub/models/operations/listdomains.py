"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import domainschema as components_domainschema
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclasses.dataclass
class ListDomainsGlobals:
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'projectSlug', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



@dataclasses.dataclass
class ListDomainsRequest:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListDomainsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    domain_schemas: Optional[List[components_domainschema.DomainSchema]] = dataclasses.field(default=None)
    r"""The domains were retrieved."""
    

