# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_list_runtime_versions_request(
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/providers/Microsoft.AppPlatform/runtimeVersions")

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

class RuntimeVersionsOperations(object):
    """RuntimeVersionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.appplatform.v2022_03_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_runtime_versions(
        self,
        **kwargs: Any
    ) -> "_models.AvailableRuntimeVersions":
        """Lists all of the available runtime versions supported by Microsoft.AppPlatform provider.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AvailableRuntimeVersions, or the result of cls(response)
        :rtype: ~azure.mgmt.appplatform.v2022_03_01_preview.models.AvailableRuntimeVersions
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AvailableRuntimeVersions"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-03-01-preview")  # type: str

        
        request = build_list_runtime_versions_request(
            api_version=api_version,
            template_url=self.list_runtime_versions.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AvailableRuntimeVersions', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_runtime_versions.metadata = {'url': "/providers/Microsoft.AppPlatform/runtimeVersions"}  # type: ignore
