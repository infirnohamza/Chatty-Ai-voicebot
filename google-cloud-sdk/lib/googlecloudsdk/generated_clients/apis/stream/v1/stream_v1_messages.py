"""Generated message classes for stream version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'stream'


class BuildStreamContentRequest(_messages.Message):
  r"""Message for building a StreamContent

  Fields:
    contentVersionTag: Required. The user-specified version tag of the build
      if it succeeds. Must match \w{0,127}. See also https://github.com/distri
      bution/distribution/blob/main/reference/regexp.go
    requestId: Optional. A unique identifier for this request. Restricted to
      36 ASCII characters. A random UUID is recommended. This request is only
      idempotent if a `request_id` is provided."
  """

  contentVersionTag = _messages.StringField(1)
  requestId = _messages.StringField(2)


class BuildVersion(_messages.Message):
  r"""Describe user-specific version tag and server-generated unique build ID
  for a specific build.

  Fields:
    buildId: Unique build ID generated by server.
    buildLogUri: Build log uri.
    buildTime: Build time stamp
    contentVersionTag: User-specified version tag of content build.
    isFailed: Boolean value whether build failed.
  """

  buildId = _messages.StringField(1)
  buildLogUri = _messages.StringField(2)
  buildTime = _messages.StringField(3)
  contentVersionTag = _messages.StringField(4)
  isFailed = _messages.BooleanField(5)


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }
  """



class LifecycleState(_messages.Message):
  r"""Describes the lifecycle state of an Immersive Stream for XR resource.

  Enums:
    StateValueValuesEnum: Current lifecycle state of the resource (e.g. if
      it's Live or Deprecated).

  Fields:
    description: Human readable message describing details about the current
      state.
    state: Current lifecycle state of the resource (e.g. if it's Live or
      Deprecated).
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Current lifecycle state of the resource (e.g. if it's Live or
    Deprecated).

    Values:
      STATE_UNSPECIFIED: Unspecified state.
      READY: Resource is ready and available for use.
      IN_USE: Resource is being used (referenced by other resources). In order
        to delete the resource, it must go through deprecation process to
        ensure it's no longer in use by other resources.
      CREATING: Resource is being created.
      UPDATING: Resource is being updated.
      DELETING: Resource is being deleted.
      ERROR: Resource encountered an error and is in indeterministic state.
    """
    STATE_UNSPECIFIED = 0
    READY = 1
    IN_USE = 2
    CREATING = 3
    UPDATING = 4
    DELETING = 5
    ERROR = 6

  description = _messages.StringField(1)
  state = _messages.EnumField('StateValueValuesEnum', 2)


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


class ListStreamContentsResponse(_messages.Message):
  r"""Message for response to listing StreamContents

  Fields:
    nextPageToken: A token identifying a page of results the server should
      return.
    streamContents: The list of StreamContent
    unreachable: Locations that could not be reached.
  """

  nextPageToken = _messages.StringField(1)
  streamContents = _messages.MessageField('StreamContent', 2, repeated=True)
  unreachable = _messages.StringField(3, repeated=True)


class ListStreamInstancesResponse(_messages.Message):
  r"""Message for response to listing StreamInstances

  Fields:
    nextPageToken: A token identifying a page of results the server should
      return.
    streamInstances: The list of StreamInstance
    unreachable: Locations that could not be reached.
  """

  nextPageToken = _messages.StringField(1)
  streamInstances = _messages.MessageField('StreamInstance', 2, repeated=True)
  unreachable = _messages.StringField(3, repeated=True)


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


class LocationConfig(_messages.Message):
  r"""Deployment configuration of an instance in a given location.

  Fields:
    capacity: The maximum number of concurrent streaming sessions that the
      instance can support in this location.
    location: The location in which the instance is deployed. We only use
      region for now.
  """

  capacity = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  location = _messages.StringField(2)


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
  r"""Represents the metadata of the long-running operation.

  Fields:
    apiVersion: Output only. API version used to start the operation.
    createTime: Output only. The time the operation was created.
    endTime: Output only. The time the operation finished running.
    requestedCancellation: Output only. Identifies whether the user has
      requested cancellation of the operation. Operations that have been
      cancelled successfully have Operation.error value with a
      google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.
    statusMessage: Output only. Human-readable status of the operation, if
      any.
    target: Output only. Server-defined resource path for the target of the
      operation.
    verb: Output only. Name of the verb executed by the operation.
  """

  apiVersion = _messages.StringField(1)
  createTime = _messages.StringField(2)
  endTime = _messages.StringField(3)
  requestedCancellation = _messages.BooleanField(4)
  statusMessage = _messages.StringField(5)
  target = _messages.StringField(6)
  verb = _messages.StringField(7)


class RealmConfig(_messages.Message):
  r"""Deployment configuration of an instance in a given realm.

  Enums:
    RealmValueValuesEnum: A realm in which the instance is deployed.

  Fields:
    capacity: The maximum number of concurrent streaming sessions that the
      instance can support in this realm.
    contentBuildVersion: The user-specified version tag and build ID of the
      content served by this instance.
    realm: A realm in which the instance is deployed.
  """

  class RealmValueValuesEnum(_messages.Enum):
    r"""A realm in which the instance is deployed.

    Values:
      REALM_UNSPECIFIED: realm not specified
      REALM_NA_CENTRAL: us-central1
      REALM_NA_EAST: us-east[1|4]
      REALM_NA_WEST: us-west[1|2|4]
      REALM_ASIA_NORTHEAST: asia-northeast[1|3]
      REALM_ASIA_SOUTHEAST: asia-southeast[1|2]
      REALM_EU_WEST: europe-west[1-4]
    """
    REALM_UNSPECIFIED = 0
    REALM_NA_CENTRAL = 1
    REALM_NA_EAST = 2
    REALM_NA_WEST = 3
    REALM_ASIA_NORTHEAST = 4
    REALM_ASIA_SOUTHEAST = 5
    REALM_EU_WEST = 6

  capacity = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  contentBuildVersion = _messages.MessageField('BuildVersion', 2)
  realm = _messages.EnumField('RealmValueValuesEnum', 3)


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


class StreamConfig(_messages.Message):
  r"""Describes the optional configuration payload that the customer wants to
  set up with for the instance.

  Fields:
    fallbackUri: User-specified fallback uri that should be launched from the
      client when there is a streaming server stock-out.
  """

  fallbackUri = _messages.StringField(1)


class StreamContent(_messages.Message):
  r"""Message describing StreamContent object Next ID: 10

  Messages:
    LabelsValue: Labels as key value pairs

  Fields:
    bucketName: Name of the Cloud Storage bucket in the consumer project that
      stores the content source.
    buildVersions: Output only. User-specified version tags and unique build
      IDs of content builds
    contentVersionTags: Output only. User-specified version tags of content
      builds
    createTime: Output only. [Output only] Create time stamp
    labels: Labels as key value pairs
    lifecycleState: Output only. Current state of the content.
    name: name of resource
    updateTime: Output only. [Output only] Update time stamp
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Labels as key value pairs

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

  bucketName = _messages.StringField(1)
  buildVersions = _messages.MessageField('BuildVersion', 2, repeated=True)
  contentVersionTags = _messages.StringField(3, repeated=True)
  createTime = _messages.StringField(4)
  labels = _messages.MessageField('LabelsValue', 5)
  lifecycleState = _messages.MessageField('LifecycleState', 6)
  name = _messages.StringField(7)
  updateTime = _messages.StringField(8)


class StreamInstance(_messages.Message):
  r"""Message describing StreamInstance object Next ID: 14

  Messages:
    LabelsValue: Labels as key value pairs
    LocationConfigsValue: Deployment configuration of the instance by
      locations (only regions are supported now). Map keys are regions in the
      string form.

  Fields:
    apiEndpoint: Output only. The API endpoint to which an Stream client can
      connect to request a streaming session.
    apiKey: Output only. The API key that an Stream client must use when
      requesting a streaming session.
    content: The content that this instance serves.
    contentBuildVersion: The user-specified version tag and build ID of the
      content served.
    createTime: Output only. [Output only] Create time stamp
    labels: Labels as key value pairs
    lifecycleState: Output only. Current status of the instance.
    locationConfigs: Deployment configuration of the instance by locations
      (only regions are supported now). Map keys are regions in the string
      form.
    name: name of resource
    realmConfigs: Deployment configuration of the instance in realms. Note
      that this is not defined as a map for enum types (Realm) cannot be used
      as key.
    streamConfig: Optional. An optional config data to configure the client
      UI.
    updateTime: Output only. [Output only] Update time stamp
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Labels as key value pairs

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
  class LocationConfigsValue(_messages.Message):
    r"""Deployment configuration of the instance by locations (only regions
    are supported now). Map keys are regions in the string form.

    Messages:
      AdditionalProperty: An additional property for a LocationConfigsValue
        object.

    Fields:
      additionalProperties: Additional properties of type LocationConfigsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LocationConfigsValue object.

      Fields:
        key: Name of the additional property.
        value: A LocationConfig attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('LocationConfig', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  apiEndpoint = _messages.StringField(1)
  apiKey = _messages.StringField(2)
  content = _messages.StringField(3)
  contentBuildVersion = _messages.MessageField('BuildVersion', 4)
  createTime = _messages.StringField(5)
  labels = _messages.MessageField('LabelsValue', 6)
  lifecycleState = _messages.MessageField('LifecycleState', 7)
  locationConfigs = _messages.MessageField('LocationConfigsValue', 8)
  name = _messages.StringField(9)
  realmConfigs = _messages.MessageField('RealmConfig', 10, repeated=True)
  streamConfig = _messages.MessageField('StreamConfig', 11)
  updateTime = _messages.StringField(12)


class StreamProjectsLocationsGetRequest(_messages.Message):
  r"""A StreamProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class StreamProjectsLocationsListRequest(_messages.Message):
  r"""A StreamProjectsLocationsListRequest object.

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


class StreamProjectsLocationsOperationsCancelRequest(_messages.Message):
  r"""A StreamProjectsLocationsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class StreamProjectsLocationsOperationsDeleteRequest(_messages.Message):
  r"""A StreamProjectsLocationsOperationsDeleteRequest object.

  Fields:
    name: The name of the operation resource to be deleted.
  """

  name = _messages.StringField(1, required=True)


class StreamProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A StreamProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class StreamProjectsLocationsOperationsListRequest(_messages.Message):
  r"""A StreamProjectsLocationsOperationsListRequest object.

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


class StreamProjectsLocationsStreamContentsBuildRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamContentsBuildRequest object.

  Fields:
    buildStreamContentRequest: A BuildStreamContentRequest resource to be
      passed as the request body.
    name: Required. Canonical resource name of the content.
  """

  buildStreamContentRequest = _messages.MessageField('BuildStreamContentRequest', 1)
  name = _messages.StringField(2, required=True)


class StreamProjectsLocationsStreamContentsCreateRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamContentsCreateRequest object.

  Fields:
    parent: Required. Value for parent.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    streamContent: A StreamContent resource to be passed as the request body.
    streamContentId: Required. Id of the requesting object If the id is
      generated from the server-side, remove this field and stream_content_id
      from the method_signature of Create RPC
  """

  parent = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  streamContent = _messages.MessageField('StreamContent', 3)
  streamContentId = _messages.StringField(4)


class StreamProjectsLocationsStreamContentsDeleteRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamContentsDeleteRequest object.

  Fields:
    name: Required. Canonical resource name of the content.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes after the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)


class StreamProjectsLocationsStreamContentsGetRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamContentsGetRequest object.

  Fields:
    name: Required. Canonical resource name of the content.
  """

  name = _messages.StringField(1, required=True)


class StreamProjectsLocationsStreamContentsListRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamContentsListRequest object.

  Fields:
    filter: Filtering results
    orderBy: Hint for how to order the results
    pageSize: Requested page size. Server may return fewer items than
      requested. If unspecified, server will pick an appropriate default.
    pageToken: A token identifying a page of results the server should return.
    parent: Required. Parent value for ListStreamContentsRequest
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class StreamProjectsLocationsStreamContentsPatchRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamContentsPatchRequest object.

  Fields:
    name: name of resource
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    streamContent: A StreamContent resource to be passed as the request body.
    updateMask: Required. Field mask is used to specify the fields to be
      overwritten in the StreamContent resource by the update. The fields
      specified in the update_mask are relative to the resource, not the full
      request. A field will be overwritten if it is in the mask. If the user
      does not provide a mask then all fields will be overwritten.
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  streamContent = _messages.MessageField('StreamContent', 3)
  updateMask = _messages.StringField(4)


class StreamProjectsLocationsStreamInstancesCreateRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamInstancesCreateRequest object.

  Fields:
    parent: Required. Value for parent.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    streamInstance: A StreamInstance resource to be passed as the request
      body.
    streamInstanceId: Required. Id of the requesting object If the id is
      generated from the server-side, remove this field and stream_instance_id
      from the method_signature of Create RPC
  """

  parent = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  streamInstance = _messages.MessageField('StreamInstance', 3)
  streamInstanceId = _messages.StringField(4)


class StreamProjectsLocationsStreamInstancesDeleteRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamInstancesDeleteRequest object.

  Fields:
    name: Required. Canonical resource name of the instance.
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes after the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)


class StreamProjectsLocationsStreamInstancesGetRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamInstancesGetRequest object.

  Fields:
    name: Required. Canonical resource name of the instance.
  """

  name = _messages.StringField(1, required=True)


class StreamProjectsLocationsStreamInstancesListRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamInstancesListRequest object.

  Fields:
    filter: Filtering results
    orderBy: Hint for how to order the results
    pageSize: Requested page size. Server may return fewer items than
      requested. If unspecified, server will pick an appropriate default.
    pageToken: A token identifying a page of results the server should return.
    parent: Required. Parent value for ListStreamInstancesRequest
  """

  filter = _messages.StringField(1)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)


class StreamProjectsLocationsStreamInstancesPatchRequest(_messages.Message):
  r"""A StreamProjectsLocationsStreamInstancesPatchRequest object.

  Fields:
    name: name of resource
    requestId: Optional. An optional request ID to identify requests. Specify
      a unique request ID so that if you must retry your request, the server
      will know to ignore the request if it has already been completed. The
      server will guarantee that for at least 60 minutes since the first
      request. For example, consider a situation where you make an initial
      request and the request times out. If you make the request again with
      the same request ID, the server can check if original operation with the
      same request ID was received, and if so, will ignore the second request.
      This prevents clients from accidentally creating duplicate commitments.
      The request ID must be a valid UUID with the exception that zero UUID is
      not supported (00000000-0000-0000-0000-000000000000).
    streamInstance: A StreamInstance resource to be passed as the request
      body.
    updateMask: Required. Field mask is used to specify the fields to be
      overwritten in the StreamInstance resource by the update. The fields
      specified in the update_mask are relative to the resource, not the full
      request. A field will be overwritten if it is in the mask. If the user
      does not provide a mask then all fields will be overwritten.
  """

  name = _messages.StringField(1, required=True)
  requestId = _messages.StringField(2)
  streamInstance = _messages.MessageField('StreamInstance', 3)
  updateMask = _messages.StringField(4)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
