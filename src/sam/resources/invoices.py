# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._resource import SyncAPIResource, AsyncAPIResource


class Invoices(SyncAPIResource):
    def create(self, **kwargs) -> dict:
        """Create a new invoice."""
        return self._post("/invoices", body=kwargs)

    def list(self) -> list:
        """List all invoices."""
        return self._get("/invoices")

    def retrieve(self, invoice_id: str) -> dict:
        """Retrieve a single invoice."""
        return self._get(f"/invoices/{invoice_id}")

    def void(self, invoice_id: str) -> dict:
        """Void an invoice."""
        return self._post(f"/invoices/{invoice_id}/void")


class AsyncInvoices(AsyncAPIResource):
    async def create(self, **kwargs) -> dict:
        """Create a new invoice."""
        return await self._post("/invoices", body=kwargs)

    async def list(self) -> list:
        """List all invoices."""
        return await self._get("/invoices")

    async def retrieve(self, invoice_id: str) -> dict:
        """Retrieve a single invoice."""
        return await self._get(f"/invoices/{invoice_id}")

    async def void(self, invoice_id: str) -> dict:
        """Void an invoice."""
        return await self._post(f"/invoices/{invoice_id}/void")
