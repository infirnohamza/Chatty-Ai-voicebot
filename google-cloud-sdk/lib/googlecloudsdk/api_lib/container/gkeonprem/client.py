# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Base class for Anthos GKE On-Prem API client resources."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.calliope import arg_parsers
import six


# pylint: disable=invalid-name
class ClientBase(object):
  """Base class for Anthos GKE On-Prem API clients."""

  def __init__(self, service=None):
    self._client = apis.GetClientInstance('gkeonprem', 'v1')
    self._messages = self._client.MESSAGES_MODULE
    self._service = service

  def GetMessage(self):
    """Returns the gkeonprem message module."""
    return self._messages

  def GetFlag(self, args, flag, default=None):
    """Returns the flag value if it's set, otherwise returns None.

    Args:
      args: An argparser Namespace class instance.
      flag: A string type flag name.
      default: The default value to return if not found in the argparser
        namespace.

    Returns:
      The flag value if it is set by the user. If the flag is not added to the
      interface, or it is added by not specified by the user, returns the
      default value.
    """
    if flag in args.GetSpecifiedArgsDict():
      return getattr(args, flag)
    else:
      return default

  def IsSet(self, kwargs):
    """Returns True if any of the kwargs is set to not None value.

    The added condition handles the case when user specified boolean False
    for the given args, and it should return True, which does not work with
    normal Python identity comparison.

    Args:
      kwargs: dict, a mapping from proto field to its respective constructor
        function.

    Returns:
      True if there exists a field that contains a user specified argument.
    """
    for value in kwargs.values():
      if isinstance(value, bool):
        return True
      elif value:
        return True
    return False

  def Describe(self, resource_ref):
    """Gets a gkeonprem API resource."""
    req = self._service.GetRequestType('Get')(name=resource_ref.RelativeName())
    return self._service.Get(req)

  def _user_cluster_ref(self, args):
    """Parses user cluster resource argument and returns its reference."""
    if getattr(args.CONCEPTS, 'cluster', None):
      return args.CONCEPTS.cluster.Parse()
    return None

  def _admin_cluster_ref(self, args):
    """Parses admin cluster resource argument and returns its reference."""
    if getattr(args.CONCEPTS, 'admin_cluster', None):
      return args.CONCEPTS.admin_cluster.Parse()
    return None

  def _location_ref(self, args):
    """Parses location resource argument and returns its reference."""
    if getattr(args.CONCEPTS, 'location', None):
      return args.CONCEPTS.location.Parse()
    return None

  def _location_name(self, args):
    """Parses location from args and returns its name."""
    location_ref = self._location_ref(args)
    if location_ref:
      return location_ref.RelativeName()
    return None

  def _user_cluster_name(self, args):
    """Parses user cluster from args and returns its name."""
    user_cluster_ref = self._user_cluster_ref(args)
    if user_cluster_ref:
      return user_cluster_ref.RelativeName()
    return None

  def _user_cluster_parent(self, args):
    """Parses user cluster from args and returns its parent name."""
    user_cluster_ref = self._user_cluster_ref(args)
    if user_cluster_ref:
      return user_cluster_ref.Parent().RelativeName()
    return None

  def _user_cluster_id(self, args):
    """Parses user cluster from args and returns its ID."""
    user_cluster_ref = self._user_cluster_ref(args)
    if user_cluster_ref:
      return user_cluster_ref.Name()
    return None

  def _admin_cluster_name(self, args):
    """Parses admin cluster from args and returns its name."""
    admin_cluster_ref = self._admin_cluster_ref(args)
    if admin_cluster_ref:
      return admin_cluster_ref.RelativeName()
    return None

  def _admin_cluster_parent(self, args):
    """Parses admin cluster from args and returns its parent name."""
    admin_cluster_ref = self._admin_cluster_ref(args)
    if admin_cluster_ref:
      return admin_cluster_ref.Parent().RelativeName()
    return None

  def _admin_cluster_id(self, args):
    """Parses admin cluster from args and returns its ID."""
    admin_cluster_ref = self._admin_cluster_ref(args)
    if admin_cluster_ref:
      return admin_cluster_ref.Name()
    return None

  def _admin_cluster_membership_ref(self, args):
    """Parses admin cluster resource argument and returns its reference."""
    if getattr(args.CONCEPTS, 'admin_cluster_membership', None):
      return args.CONCEPTS.admin_cluster_membership.Parse()
    return None

  def _admin_cluster_membership_name(self, args):
    """Parses admin cluster from args and returns its name."""
    admin_cluster_ref = self._admin_cluster_membership_ref(args)
    if admin_cluster_ref:
      return admin_cluster_ref.RelativeName()
    return None

  def _node_pool_ref(self, args):
    """Parses node pool resource argument and returns its reference."""
    if getattr(args.CONCEPTS, 'node_pool', None):
      return args.CONCEPTS.node_pool.Parse()
    return None

  def _node_pool_name(self, args):
    """Parses node pool from args and returns its name."""
    node_pool_ref = self._node_pool_ref(args)
    if node_pool_ref:
      return node_pool_ref.RelativeName()
    return None

  def _node_pool_id(self, args):
    """Parses node pool from args and returns its ID."""
    node_pool_ref = self._node_pool_ref(args)
    if node_pool_ref:
      return node_pool_ref.Name()

  def _node_pool_parent(self, args):
    """Parses node pool from args and returns its parent name."""
    node_pool_ref = self._node_pool_ref(args)
    if node_pool_ref:
      return node_pool_ref.Parent().RelativeName()
    return None

  def _parse_node_taint(self, node_taint):
    """Validates and parses a node taint object.

    Args:
      node_taint: tuple, of format (TAINT_KEY, value), where value is a string
        of format TAINT_VALUE=EFFECT.

    Returns:
      If taint is valid, returns a dict mapping message NodeTaint to its value;
      otherwise, raise ArgumentTypeError.
      For example,
      {
          'key': TAINT_KEY
          'value': TAINT_VALUE
          'effect': EFFECT
      }
    """
    taint_effect_enum = self._messages.NodeTaint.EffectValueValuesEnum
    taint_effect_mapping = {
        'NoSchedule': taint_effect_enum.NO_SCHEDULE,
        'PreferNoSchedule': taint_effect_enum.PREFER_NO_SCHEDULE,
        'NoExecute': taint_effect_enum.NO_EXECUTE,
    }

    input_node_taint = '='.join(node_taint)
    valid_node_taint_effects = ', '.join(
        six.text_type(key) for key in sorted(taint_effect_mapping.keys())
    )

    if len(node_taint) != 2:
      raise arg_parsers.ArgumentTypeError(
          'Node taint [{}] not in correct format, expect KEY=VALUE:EFFECT.'
          .format(input_node_taint)
      )
    taint_key = node_taint[0]

    effect_delimiter_count = node_taint[1].count(':')
    if effect_delimiter_count > 1:
      raise arg_parsers.ArgumentTypeError(
          'Node taint [{}] not in correct format, expect KEY=VALUE:EFFECT.'
          .format(input_node_taint)
      )

    if effect_delimiter_count == 0:
      taint_value = node_taint[1]
      raise arg_parsers.ArgumentTypeError(
          'Taint effect unspecified: [{}], expect one of [{}].'.format(
              input_node_taint, valid_node_taint_effects
          )
      )

    if effect_delimiter_count == 1:
      taint_value, taint_effect = node_taint[1].split(':', 1)
      if taint_effect not in taint_effect_mapping:
        raise arg_parsers.ArgumentTypeError(
            'Invalid taint effect in [{}] , expect one of [{}]'.format(
                input_node_taint, valid_node_taint_effects
            )
        )

      taint_effect = taint_effect_mapping[taint_effect]

    return {'key': taint_key, 'value': taint_value, 'effect': taint_effect}

  def _standalone_cluster_ref(self, args):
    """Parses standalone cluster resource argument and returns its reference."""
    if getattr(args.CONCEPTS, 'standalone_cluster', None):
      return args.CONCEPTS.standalone_cluster.Parse()
    return None

  def _standalone_cluster_name(self, args):
    """Parses standalone cluster from args and returns its name."""
    standalone_cluster_ref = self._standalone_cluster_ref(args)
    if standalone_cluster_ref:
      return standalone_cluster_ref.RelativeName()
    return None

  def _standalone_cluster_parent(self, args):
    """Parses standalone cluster from args and returns its parent name."""
    standalone_cluster_ref = self._standalone_cluster_ref(args)
    if standalone_cluster_ref:
      return standalone_cluster_ref.Parent().RelativeName()
    return None

  def _standalone_cluster_id(self, args):
    """Parses standalone cluster from the given args and returns its ID."""
    standalone_cluster_ref = self._standalone_cluster_ref(args)
    if standalone_cluster_ref:
      return standalone_cluster_ref.Name()
    return None

  def _standalone_cluster_membership_ref(self, args):
    """Parses standalone cluster resource argument and returns its reference."""
    if getattr(args.CONCEPTS, 'membership', None):
      return args.CONCEPTS.membership.Parse()
    return None

  def _standalone_cluster_membership_name(self, args):
    """Parses standalone cluster from args and returns its name."""
    standalone_cluster_ref = self._standalone_cluster_membership_ref(args)
    if standalone_cluster_ref:
      return standalone_cluster_ref.RelativeName()
    return None
