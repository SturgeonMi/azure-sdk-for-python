# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._baseline_operations import build_get_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class BaselineOperations:
    """BaselineOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~$(python-base-namespace).v2018_09_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get(
        self,
        resource_uri: str,
        metricnames: Optional[str] = None,
        timespan: Optional[str] = None,
        interval: Optional[datetime.timedelta] = None,
        aggregation: Optional[str] = None,
        sensitivities: Optional[str] = None,
        result_type: Optional[Union[str, "_models.ResultType"]] = None,
        metricnamespace: Optional[str] = None,
        filter: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.BaselineResponse":
        """**Gets the baseline values for a resource**.

        :param resource_uri: The identifier of the resource. It has the following structure:
         subscriptions/{subscriptionName}/resourceGroups/{resourceGroupName}/providers/{providerName}/{resourceName}.
         For example:
         subscriptions/b368ca2f-e298-46b7-b0ab-012281956afa/resourceGroups/vms/providers/Microsoft.Compute/virtualMachines/vm1.
        :type resource_uri: str
        :param metricnames: The names of the metrics (comma separated) to retrieve. Special case: If a
         metricname itself has a comma in it then use %2 to indicate it. Eg: 'Metric,Name1' should be
         **'Metric%2Name1'**.
        :type metricnames: str
        :param timespan: The timespan of the query. It is a string with the following format
         'startDateTime_ISO/endDateTime_ISO'.
        :type timespan: str
        :param interval: The interval (i.e. timegrain) of the query.
        :type interval: ~datetime.timedelta
        :param aggregation: The aggregation type of the metric to retrieve the baseline for.
        :type aggregation: str
        :param sensitivities: The list of sensitivities (comma separated) to retrieve.
        :type sensitivities: str
        :param result_type: Allows retrieving only metadata of the baseline. On data request all
         information is retrieved.
        :type result_type: str or ~$(python-base-namespace).v2018_09_01.models.ResultType
        :param metricnamespace: Metric namespace to query metric definitions for.
        :type metricnamespace: str
        :param filter: The **$filter** is used to describe a set of dimensions with their concrete
         values which produce a specific metric's time series, in which a baseline is requested for.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: BaselineResponse, or the result of cls(response)
        :rtype: ~$(python-base-namespace).v2018_09_01.models.BaselineResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.BaselineResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            resource_uri=resource_uri,
            metricnames=metricnames,
            timespan=timespan,
            interval=interval,
            aggregation=aggregation,
            sensitivities=sensitivities,
            result_type=result_type,
            metricnamespace=metricnamespace,
            filter=filter,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('BaselineResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/{resourceUri}/providers/Microsoft.Insights/baseline'}  # type: ignore
