"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import workspaceschema as components_workspaceschema
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclasses.dataclass
class GetWorkspaceRequest:
    id_or_slug: str = dataclasses.field(metadata={'path_param': { 'field_name': 'idOrSlug', 'style': 'simple', 'explode': False }})
    r"""The ID or slug of the workspace."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetWorkspaceResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    workspace_schema: Optional[components_workspaceschema.WorkspaceSchema] = dataclasses.field(default=None)
    r"""The retrieved workspace"""
    

