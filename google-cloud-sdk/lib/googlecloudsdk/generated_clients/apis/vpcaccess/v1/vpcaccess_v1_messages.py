"""Generated message classes for vpcaccess version v1.

API for managing VPC access connectors.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'vpcaccess'


class Connector(_messages.Message):
  r"""Definition of a Serverless VPC Access connector.

  Enums:
    StateValueValuesEnum: Output only. State of the VPC access connector.

  Fields:
    connectedProjects: Output only. List of projects using the connector.
    ipCidrRange: The range of internal addresses that follows RFC 4632
      notation. Example: `10.132.0.0/28`.
    machineType: Machine type of VM Instance underlying connector. Default is
      e2-micro
    maxInstances: Maximum value of instances in autoscaling group underlying
      the connector.
    maxThroughput: Maximum throughput of the connector in Mbps. Default is
      300, max is 1000.
    minInstances: Minimum value of instances in autoscaling group underlying
      the connector.
    minThroughput: Minimum throughput of the connector in Mbps. Default and
      min is 200.
    name: The resource name in the format
      `projects/*/locations/*/connectors/*`.
    network: Name of a VPC network.
    state: Output only. State of the VPC access connector.
    subnet: The subnet in which to house the VPC Access Connector.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Output only. State of the VPC access connector.

    Values:
      STATE_UNSPECIFIED: Invalid state.
      READY: Connector is deployed and ready to receive traffic.
      CREATING: An Insert operation is in progress. Transient condition.
      DELETING: A Delete operation is in progress. Transient condition.
      ERROR: Connector is in a bad state, manual deletion recommended.
      UPDATING: The connector is being updated.
    """
    STATE_UNSPECIFIED = 0
    READY = 1
    CREATING = 2
    DELETING = 3
    ERROR = 4
    UPDATING = 5

  connectedProjects = _messages.StringField(1, repeated=True)
  ipCidrRange = _messages.StringField(2)
  machineType = _messages.StringField(3)
  maxInstances = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  maxThroughput = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  minInstances = _messages.IntegerField(6, variant=_messages.Variant.INT32)
  minThroughput = _messages.IntegerField(7, variant=_messages.Variant.INT32)
  name = _messages.StringField(8)
  network = _messages.StringField(9)
  state = _messages.EnumField('StateValueValuesEnum', 10)
  subnet = _messages.MessageField('Subnet', 11)


class ListConnectorsResponse(_messages.Message):
  r"""Response for listing Serverless VPC Access connectors.

  Fields:
    connectors: List of Serverless VPC Access connectors.
    nextPageToken: Continuation token.
  """

  connectors = _messages.MessageField('Connector', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  r"""A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success. If
      the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal response of the operation in case of success. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal response of the operation in case of success. If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadata(_messages.Message):
  r"""Metadata for google.longrunning.Operation.

  Fields:
    createTime: Output only. Time when the operation was created.
    endTime: Output only. Time when the operation completed.
    method: Output only. Method that initiated the operation e.g.
      google.cloud.vpcaccess.v1.Connectors.CreateConnector.
    target: Output only. Name of the resource that this operation is acting on
      e.g. projects/my-project/locations/us-central1/connectors/v1.
  """

  createTime = _messages.StringField(1)
  endTime = _messages.StringField(2)
  method = _messages.StringField(3)
  target = _messages.StringField(4)


class OperationMetadataV1Alpha1(_messages.Message):
  r"""Metadata for google.longrunning.Operation.

  Fields:
    endTime: Output only. Time when the operation completed.
    insertTime: Output only. Time when the operation was created.
    method: Output only. Method that initiated the operation e.g.
      google.cloud.vpcaccess.v1alpha1.Connectors.CreateConnector.
    target: Output only. Name of the resource that this operation is acting on
      e.g. projects/my-project/locations/us-central1/connectors/v1.
  """

  endTime = _messages.StringField(1)
  insertTime = _messages.StringField(2)
  method = _messages.StringField(3)
  target = _messages.StringField(4)


class OperationMetadataV1Beta1(_messages.Message):
  r"""Metadata for google.longrunning.Operation.

  Fields:
    createTime: Output only. Time when the operation was created.
    endTime: Output only. Time when the operation completed.
    method: Output only. Method that initiated the operation e.g.
      google.cloud.vpcaccess.v1beta1.Connectors.CreateConnector.
    target: Output only. Name of the resource that this operation is acting on
      e.g. projects/my-project/locations/us-central1/connectors/v1.
  """

  createTime = _messages.StringField(1)
  endTime = _messages.StringField(2)
  method = _messages.StringField(3)
  target = _messages.StringField(4)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class Subnet(_messages.Message):
  r"""The subnet in which to house the connector

  Fields:
    name: Subnet name (relative, not fully qualified). E.g. if the full subnet
      selfLink is https://compute.googleapis.com/compute/v1/projects/{project}
      /regions/{region}/subnetworks/{subnetName} the correct input for this
      field would be {subnetName}
    projectId: Project in which the subnet exists. If not set, this project is
      assumed to be the project for which the connector create request was
      issued.
  """

  name = _messages.StringField(1)
  projectId = _messages.StringField(2)


class VpcaccessProjectsLocationsConnectorsCreateRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsConnectorsCreateRequest object.

  Fields:
    connector: A Connector resource to be passed as the request body.
    connectorId: Required. The ID to use for this connector.
    parent: Required. The project and location in which the configuration
      should be created, specified in the format `projects/*/locations/*`.
  """

  connector = _messages.MessageField('Connector', 1)
  connectorId = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class VpcaccessProjectsLocationsConnectorsDeleteRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsConnectorsDeleteRequest object.

  Fields:
    name: Required. Name of a Serverless VPC Access connector to delete.
  """

  name = _messages.StringField(1, required=True)


class VpcaccessProjectsLocationsConnectorsGetRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsConnectorsGetRequest object.

  Fields:
    name: Required. Name of a Serverless VPC Access connector to get.
  """

  name = _messages.StringField(1, required=True)


class VpcaccessProjectsLocationsConnectorsListRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsConnectorsListRequest object.

  Fields:
    pageSize: Maximum number of functions to return per call.
    pageToken: Continuation token.
    parent: Required. The project and location from which the routes should be
      listed.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class VpcaccessProjectsLocationsConnectorsPatchRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsConnectorsPatchRequest object.

  Fields:
    connector: A Connector resource to be passed as the request body.
    name: The resource name in the format
      `projects/*/locations/*/connectors/*`.
    updateMask: The fields to update on the entry group. If absent or empty,
      all modifiable fields are updated.
  """

  connector = _messages.MessageField('Connector', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class VpcaccessProjectsLocationsListRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsListRequest object.

  Fields:
    filter: A filter to narrow down results to a preferred subset. The
      filtering language accepts strings like `"displayName=tokyo"`, and is
      documented in more detail in [AIP-160](https://google.aip.dev/160).
    name: The resource that owns the locations collection, if applicable.
    pageSize: The maximum number of results to return. If not set, the service
      selects a default.
    pageToken: A page token received from the `next_page_token` field in the
      response. Send that page token to receive the subsequent page.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class VpcaccessProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class VpcaccessProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A VpcaccessProjectsLocationsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
