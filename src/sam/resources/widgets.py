# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._resource import SyncAPIResource, AsyncAPIResource


class Widgets(SyncAPIResource):
    def list(self) -> list:
        """List all widgets."""
        return self._get("/widgets")

    def retrieve(self, widget_id: str) -> dict:
        """Retrieve a single widget."""
        return self._get(f"/widgets/{widget_id}")


class AsyncWidgets(AsyncAPIResource):
    async def list(self) -> list:
        """List all widgets."""
        return await self._get("/widgets")

    async def retrieve(self, widget_id: str) -> dict:
        """Retrieve a single widget."""
        return await self._get(f"/widgets/{widget_id}")
