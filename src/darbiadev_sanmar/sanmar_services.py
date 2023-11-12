"""A module for wrapping SanMar's SOAP API."""

from typing import Self

import requests
import xmltodict


class SanMarServices:
    """A class wrapping SanMar's SOAP API.

    This class wraps SanMar's API, using HTTP POST requests to send SOAP envelopes.
    """

    def __init__(self: Self, base_url: str, pac_url: str, version: str, username: str, password: str) -> None:  # noqa: PLR0913
        self.base_url = base_url
        self.pac_url = pac_url
        self.version: str = version
        self.username: str = username
        self.password: str = password

    def _make_request(
        self: Self,
        service: str,
        soap_envelope: str,
    ) -> str:
        response = requests.request(
            method="post",
            url=self.base_url + service,
            data=soap_envelope,
            headers={"Content-Type": "text/xml;charset=utf-8"},
        )
        response.raise_for_status()
        return response.content.decode()

    def get_packing_slip(
        self: Self,
        service: str,
        license_plate: str,
    ) -> dict:
        """Get a packing slip from SanMar's API."""
        service_pac_name = service.replace("Service", "")

        soap_envelope = f"""
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:pac="{self.pac_url + service_pac_name}">
           <soapenv:Header/>
           <soapenv:Body>
              <pac:GetPackingSlip>
                 <pac:wsVersion>{self.version}</pac:wsVersion>
                 <pac:UserId>{self.username}</pac:UserId>
                 <pac:Password>{self.password}</pac:Password>
                 <pac:PackingSlipId>{license_plate}</pac:PackingSlipId>
              </pac:GetPackingSlip>
           </soapenv:Body>
        </soapenv:Envelope>
        """

        content = self._make_request(service=service, soap_envelope=soap_envelope)
        data = xmltodict.parse(content, dict_constructor=dict)

        headless_data = data["S:Envelope"]["S:Body"]["GetPackingSlipResponse"]["PackingSlip"]
        headless_data["_original"] = content

        return headless_data
