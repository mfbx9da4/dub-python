"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from enum import Enum
from typing import List, Optional, Union


@dataclasses.dataclass
class GetLinksGlobals:
    workspace_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'projectSlug', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



class Sort(str, Enum):
    r"""The field to sort the links by. The default is `createdAt`, and sort order is always descending."""
    CREATED_AT = 'createdAt'
    CLICKS = 'clicks'
    LAST_CLICKED = 'lastClicked'


@dataclasses.dataclass
class GetLinksRequest:
    domain: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'domain', 'style': 'form', 'explode': True }})
    r"""The domain to filter the links by. E.g. `ac.me`. If not provided, all links for the workspace will be returned."""
    tag_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tagId', 'style': 'form', 'explode': True }})
    r"""The tag ID to filter the links by. This field is deprecated – use `tagIds` instead."""
    tag_ids: Optional[QueryParamTagIds] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tagIds', 'style': 'form', 'explode': True }})
    r"""The tag IDs to filter the links by."""
    tag_names: Optional[QueryParamTagNames] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tagNames', 'style': 'form', 'explode': True }})
    r"""The unique name of the tags assigned to the short link (case insensitive)."""
    search: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'search', 'style': 'form', 'explode': True }})
    r"""The search term to filter the links by. The search term will be matched against the short link slug and the destination url."""
    user_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'userId', 'style': 'form', 'explode': True }})
    r"""The user ID to filter the links by."""
    show_archived: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'showArchived', 'style': 'form', 'explode': True }})
    r"""Whether to include archived links in the response. Defaults to `false` if not provided."""
    with_tags: Optional[bool] = dataclasses.field(default=True, metadata={'query_param': { 'field_name': 'withTags', 'style': 'form', 'explode': True }})
    r"""Whether to include tags in the response. Defaults to `false` if not provided."""
    sort: Optional[Sort] = dataclasses.field(default=Sort.CREATED_AT, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    r"""The field to sort the links by. The default is `createdAt`, and sort order is always descending."""
    page: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'page', 'style': 'form', 'explode': True }})
    r"""The page number for pagination (each page contains 100 links)."""
    


QueryParamTagIds = Union[str, List[str]]

QueryParamTagNames = Union[str, List[str]]
