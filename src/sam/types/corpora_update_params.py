# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CorporaUpdateParams", "CrawlSpec", "CreatedBy", "UpdatedBy"]


class CorporaUpdateParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]

    name: Required[str]

    active: bool

    crawl_spec: Annotated[CrawlSpec, PropertyInfo(alias="crawlSpec")]

    created_by: Annotated[CreatedBy, PropertyInfo(alias="createdBy")]

    exclude_last_updated_before: Annotated[
        Union[str, datetime], PropertyInfo(alias="excludeLastUpdatedBefore", format="iso8601")
    ]

    html_transformer: Annotated[
        Literal["NONE", "EXTRACTUS", "READABLE_TEXT", "READABLE_TEXT_IF_POSSIBLE"],
        PropertyInfo(alias="htmlTransformer"),
    ]

    included_kb_article_ids: Annotated[List[str], PropertyInfo(alias="includedKbArticleIds")]

    integration: Literal["SALESFORCE", "ZENDESK", "FRESHDESK", "SLACK_QA_BOT", "TWILIO"]

    integration_category_id: Annotated[str, PropertyInfo(alias="integrationCategoryId")]

    source_url: Annotated[str, PropertyInfo(alias="sourceUrl")]

    status: Literal["PROCESSING", "READY", "FAILED"]

    tags: List[str]

    type: Literal[
        "URL", "MANUAL", "FILE_UPLOAD", "EXTERNAL_INTEGRATION", "FRESHDESK_KB", "ZENDESK_KB", "CSV", "UNKNOWN"
    ]

    updated_by: Annotated[UpdatedBy, PropertyInfo(alias="updatedBy")]

    url_exclusion_patterns: Annotated[List[str], PropertyInfo(alias="urlExclusionPatterns")]


class CrawlSpec(TypedDict, total=False):
    exclusion_patterns: Annotated[List[str], PropertyInfo(alias="exclusionPatterns")]

    html_transformer: Annotated[
        Literal["NONE", "EXTRACTUS", "READABLE_TEXT", "READABLE_TEXT_IF_POSSIBLE"],
        PropertyInfo(alias="htmlTransformer"),
    ]

    ingestion_workflow_id: Annotated[str, PropertyInfo(alias="ingestionWorkflowId")]

    initial_concurrency: Annotated[int, PropertyInfo(alias="initialConcurrency")]

    max_concurrency: Annotated[int, PropertyInfo(alias="maxConcurrency")]

    max_crawl_depth: Annotated[int, PropertyInfo(alias="maxCrawlDepth")]

    max_crawl_pages: Annotated[int, PropertyInfo(alias="maxCrawlPages")]

    remove_elements_css_selector: Annotated[str, PropertyInfo(alias="removeElementsCssSelector")]

    save_html: Annotated[bool, PropertyInfo(alias="saveHtml")]

    save_markdown: Annotated[bool, PropertyInfo(alias="saveMarkdown")]

    start_urls: Annotated[List[str], PropertyInfo(alias="startUrls")]

    timeout_seconds: Annotated[int, PropertyInfo(alias="timeoutSeconds")]

    use_sitemaps: Annotated[bool, PropertyInfo(alias="useSitemaps")]


class CreatedBy(TypedDict, total=False):
    id: str

    name: str


class UpdatedBy(TypedDict, total=False):
    id: str

    name: str
