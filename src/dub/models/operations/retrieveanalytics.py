"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import clicksbrowsers as components_clicksbrowsers
from ...models.components import clickscities as components_clickscities
from ...models.components import clickscount as components_clickscount
from ...models.components import clickscountries as components_clickscountries
from ...models.components import clicksdevices as components_clicksdevices
from ...models.components import clicksos as components_clicksos
from ...models.components import clicksreferers as components_clicksreferers
from ...models.components import clickstimeseries as components_clickstimeseries
from ...models.components import clickstoplinks as components_clickstoplinks
from ...models.components import clickstopurls as components_clickstopurls
from ...models.components import countrycode as components_countrycode
from ...models.components import httpmetadata as components_httpmetadata
from ...models.components import leadsbrowsers as components_leadsbrowsers
from ...models.components import leadscities as components_leadscities
from ...models.components import leadscount as components_leadscount
from ...models.components import leadscountries as components_leadscountries
from ...models.components import leadsdevices as components_leadsdevices
from ...models.components import leadsos as components_leadsos
from ...models.components import leadsreferers as components_leadsreferers
from ...models.components import leadstimeseries as components_leadstimeseries
from ...models.components import leadstoplinks as components_leadstoplinks
from ...models.components import leadstopurls as components_leadstopurls
from ...models.components import salesbrowsers as components_salesbrowsers
from ...models.components import salescities as components_salescities
from ...models.components import salescount as components_salescount
from ...models.components import salescountries as components_salescountries
from ...models.components import salesdevices as components_salesdevices
from ...models.components import salesos as components_salesos
from ...models.components import salesreferers as components_salesreferers
from ...models.components import salestimeseries as components_salestimeseries
from ...models.components import salestoplinks as components_salestoplinks
from ...models.components import salestopurls as components_salestopurls
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import List, Optional, Union


@dataclasses.dataclass
class RetrieveAnalyticsGlobals:
    workspace_id: str = dataclasses.field(metadata={'query_param': { 'field_name': 'workspaceId', 'style': 'form', 'explode': True }})
    project_slug: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'projectSlug', 'style': 'form', 'explode': True }})
    r"""Deprecated field: This will be removed in a future release, please migrate away from it as soon as possible."""
    



class Event(str, Enum):
    r"""The type of event to retrieve analytics for. Defaults to 'clicks'."""
    CLICKS = 'clicks'
    LEADS = 'leads'
    SALES = 'sales'
    COMPOSITE = 'composite'


class QueryParamGroupBy(str, Enum):
    r"""The parameter to group the analytics data points by. Defaults to 'count' if undefined."""
    COUNT = 'count'
    TIMESERIES = 'timeseries'
    COUNTRIES = 'countries'
    CITIES = 'cities'
    DEVICES = 'devices'
    BROWSERS = 'browsers'
    OS = 'os'
    REFERERS = 'referers'
    TOP_LINKS = 'top_links'
    TOP_URLS = 'top_urls'
    TRIGGER = 'trigger'


class Interval(str, Enum):
    r"""The interval to retrieve analytics for. Takes precedence over start and end. If undefined, defaults to 24h."""
    TWENTY_FOURH = '24h'
    SEVEND = '7d'
    THIRTYD = '30d'
    NINETYD = '90d'
    YTD = 'ytd'
    ONEY = '1y'
    ALL = 'all'
    ALL_UNFILTERED = 'all_unfiltered'


@dataclasses.dataclass
class RetrieveAnalyticsRequest:
    event: Optional[Event] = dataclasses.field(default=Event.CLICKS, metadata={'query_param': { 'field_name': 'event', 'style': 'form', 'explode': True }})
    r"""The type of event to retrieve analytics for. Defaults to 'clicks'."""
    group_by: Optional[QueryParamGroupBy] = dataclasses.field(default=QueryParamGroupBy.COUNT, metadata={'query_param': { 'field_name': 'groupBy', 'style': 'form', 'explode': True }})
    r"""The parameter to group the analytics data points by. Defaults to 'count' if undefined."""
    domain: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'domain', 'style': 'form', 'explode': True }})
    r"""The domain to filter analytics for."""
    key: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'key', 'style': 'form', 'explode': True }})
    r"""The short link slug."""
    link_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'linkId', 'style': 'form', 'explode': True }})
    r"""The unique ID of the short link on Dub."""
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'externalId', 'style': 'form', 'explode': True }})
    r"""This is the ID of the link in the your database. Must be prefixed with 'ext_' when passed as a query parameter."""
    interval: Optional[Interval] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'interval', 'style': 'form', 'explode': True }})
    r"""The interval to retrieve analytics for. Takes precedence over start and end. If undefined, defaults to 24h."""
    start: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start', 'style': 'form', 'explode': True }})
    r"""The start date and time when to retrieve analytics from."""
    end: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end', 'style': 'form', 'explode': True }})
    r"""The end date and time when to retrieve analytics from. If not provided, defaults to the current date."""
    timezone: Optional[str] = dataclasses.field(default='UTC', metadata={'query_param': { 'field_name': 'timezone', 'style': 'form', 'explode': True }})
    r"""The IANA time zone code for aligning timeseries granularity (e.g. America/New_York). Defaults to UTC."""
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
    


RetrieveAnalyticsResponseBody = Union[components_clickscount.ClicksCount, List[components_clickstimeseries.ClicksTimeseries], List[components_clickscountries.ClicksCountries], List[components_clickscities.ClicksCities], List[components_clicksdevices.ClicksDevices], List[components_clicksbrowsers.ClicksBrowsers], List[components_clicksos.ClicksOS], List[components_clicksreferers.ClicksReferers], List[components_clickstoplinks.ClicksTopLinks], List[components_clickstopurls.ClicksTopUrls], components_leadscount.LeadsCount, List[components_leadstimeseries.LeadsTimeseries], List[components_leadscountries.LeadsCountries], List[components_leadscities.LeadsCities], List[components_leadsdevices.LeadsDevices], List[components_leadsbrowsers.LeadsBrowsers], List[components_leadsos.LeadsOS], List[components_leadsreferers.LeadsReferers], List[components_leadstoplinks.LeadsTopLinks], List[components_leadstopurls.LeadsTopUrls], components_salescount.SalesCount, List[components_salestimeseries.SalesTimeseries], List[components_salescountries.SalesCountries], List[components_salescities.SalesCities], List[components_salesdevices.SalesDevices], List[components_salesbrowsers.SalesBrowsers], List[components_salesos.SalesOS], List[components_salesreferers.SalesReferers], List[components_salestoplinks.SalesTopLinks], List[components_salestopurls.SalesTopUrls]]


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class RetrieveAnalyticsResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field(metadata={'dataclasses_json': { 'exclude': lambda f: True }})
    one_of: Optional[RetrieveAnalyticsResponseBody] = dataclasses.field(default=None)
    r"""Analytics data"""
    

