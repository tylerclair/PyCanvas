# coding: utf-8

"""


    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ...base_api import BaseApi
from ...configuration import Configuration
from ..api_client import ApiClient


class AppointmentgroupsApi(BaseApi):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    # OPERATIONID: create_appointment_group
    def create_appointment_group(self, appointment_group_context_codes, appointment_group_title, **kwargs):
        """
        Create an appointment group
        Create and return a new appointment group. If new_appointments are specified, the response will return a new_appointments array (same format as appointments array, see \"List appointment groups\" action)

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_appointment_group_with_http_info(appointment_group_context_codes, appointment_group_title, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] appointment_group_context_codes: Array of context codes (courses, e.g. course_1) this group should be linked to (1 or more). Users in the course(s) with appropriate permissions will be able to sign up for this appointment group. (required)
        :param str appointment_group_title: Short title for the appointment group. (required)
        :param list[str] appointment_group_sub_context_codes: Array of sub context codes (course sections or a single group category) this group should be linked to. Used to limit the appointment group to particular sections. If a group category is specified, students will sign up in groups and the participant_type will be \"Group\" instead of \"User\".
        :param str appointment_group_description: Longer text description of the appointment group.
        :param str appointment_group_location_name: Location name of the appointment group.
        :param str appointment_group_location_address: Location address.
        :param bool appointment_group_publish: Indicates whether this appointment group should be published (i.e. made available for signup). Once published, an appointment group cannot be unpublished. Defaults to false.
        :param int appointment_group_participants_per_appointment: Maximum number of participants that may register for each time slot. Defaults to null (no limit).
        :param int appointment_group_min_appointments_per_participant: Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots.
        :param int appointment_group_max_appointments_per_participant: Maximum number of time slots a user may register for.
        :param list[str] appointment_group_new_appointments_x: Nested array of start time/end time pairs indicating time slots for this appointment group. Refer to the example request.
        :param str appointment_group_participant_visibility: \"private\":: participants cannot see who has signed up for a particular time slot \"protected\":: participants can see who has signed up. Defaults to \"private\".
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['appointment_group_context_codes', 'appointment_group_title', 'appointment_group_sub_context_codes', 'appointment_group_description', 'appointment_group_location_name', 'appointment_group_location_address', 'appointment_group_publish', 'appointment_group_participants_per_appointment', 'appointment_group_min_appointments_per_participant', 'appointment_group_max_appointments_per_participant', 'appointment_group_new_appointments_x', 'appointment_group_participant_visibility']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_appointment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'appointment_group_context_codes' is set
        if ('appointment_group_context_codes' not in params) or (params['appointment_group_context_codes'] is None):
            raise ValueError("Missing the required parameter `appointment_group_context_codes` when calling `create_appointment_group`")
        # verify the required parameter 'appointment_group_title' is set
        if ('appointment_group_title' not in params) or (params['appointment_group_title'] is None):
            raise ValueError("Missing the required parameter `appointment_group_title` when calling `create_appointment_group`")

        resource_path = '/v1/appointment_groups'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'appointment_group_context_codes' in params:
            form_params.append(('appointment_group[context_codes]', params['appointment_group_context_codes']))
        if 'appointment_group_sub_context_codes' in params:
            form_params.append(('appointment_group[sub_context_codes]', params['appointment_group_sub_context_codes']))
        if 'appointment_group_title' in params:
            form_params.append(('appointment_group[title]', params['appointment_group_title']))
        if 'appointment_group_description' in params:
            form_params.append(('appointment_group[description]', params['appointment_group_description']))
        if 'appointment_group_location_name' in params:
            form_params.append(('appointment_group[location_name]', params['appointment_group_location_name']))
        if 'appointment_group_location_address' in params:
            form_params.append(('appointment_group[location_address]', params['appointment_group_location_address']))
        if 'appointment_group_publish' in params:
            form_params.append(('appointment_group[publish]', params['appointment_group_publish']))
        if 'appointment_group_participants_per_appointment' in params:
            form_params.append(('appointment_group[participants_per_appointment]', params['appointment_group_participants_per_appointment']))
        if 'appointment_group_min_appointments_per_participant' in params:
            form_params.append(('appointment_group[min_appointments_per_participant]', params['appointment_group_min_appointments_per_participant']))
        if 'appointment_group_max_appointments_per_participant' in params:
            form_params.append(('appointment_group[max_appointments_per_participant]', params['appointment_group_max_appointments_per_participant']))
        if 'appointment_group_new_appointments_x' in params:
            form_params.append(('appointment_group[new_appointments][X]', params['appointment_group_new_appointments_x']))
        if 'appointment_group_participant_visibility' in params:
            form_params.append(('appointment_group[participant_visibility]', params['appointment_group_participant_visibility']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: delete_appointment_group
    def delete_appointment_group(self, id, **kwargs):
        """
        Delete an appointment group
        Delete an appointment group (and associated time slots and reservations)  and return the deleted group

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_appointment_group_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID (required)
        :param str cancel_reason: Reason for deleting/canceling the appointment group.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'cancel_reason']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_appointment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_appointment_group`")

        resource_path = '/v1/appointment_groups/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'cancel_reason' in params:
            query_params['cancel_reason'] = params['cancel_reason']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: get_single_appointment_group
    def get_single_appointment_group(self, id, **kwargs):
        """
        Get a single appointment group
        Returns information for a single appointment group

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_single_appointment_group_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID (required)
        :param list[str] include: Array of additional information to include. Ssee include[] argument of \"List appointment groups\" action. \"child_events\":: reservations of time slots time slots \"appointments\":: will always be returned
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_single_appointment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_single_appointment_group`")

        resource_path = '/v1/appointment_groups/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'include' in params:
            query_params['include'] = params['include']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_appointment_groups
    def list_appointment_groups(self, **kwargs):
        """
        List appointment groups
        Retrieve the list of appointment groups that can be reserved or managed by the current user.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_appointment_groups_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str scope: Defaults to \"reservable\"
        :param list[str] context_codes: Array of context codes used to limit returned results.
        :param bool include_past_appointments: Defaults to false. If true, includes past appointment groups
        :param list[str] include: Array of additional information to include. \"appointments\":: calendar event time slots for this appointment group \"child_events\":: reservations of those time slots \"participant_count\":: number of reservations \"reserved_times\":: the event id, start time and end time of reservations the current user has made)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['scope', 'context_codes', 'include_past_appointments', 'include']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_appointment_groups" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/appointment_groups'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'scope' in params:
            query_params['scope'] = params['scope']
        if 'context_codes' in params:
            query_params['context_codes'] = params['context_codes']
        if 'include_past_appointments' in params:
            query_params['include_past_appointments'] = params['include_past_appointments']
        if 'include' in params:
            query_params['include'] = params['include']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_student_group_participants
    def list_student_group_participants(self, id, **kwargs):
        """
        List student group participants
        List student groups that are (or may be) participating in this appointment group. Refer to the Groups API for the response fields. Returns no results for appointment groups with the \"User\" participant_type.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_student_group_participants_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID (required)
        :param str registration_status: Limits results to the a given participation status, defaults to \"all\"
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'registration_status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_student_group_participants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_student_group_participants`")

        resource_path = '/v1/appointment_groups/{id}/groups'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'registration_status' in params:
            query_params['registration_status'] = params['registration_status']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: list_user_participants
    def list_user_participants(self, id, **kwargs):
        """
        List user participants
        List users that are (or may be) participating in this appointment group. Refer to the Users API for the response fields. Returns no results for appointment groups with the \"Group\" participant_type.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_user_participants_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID (required)
        :param str registration_status: Limits results to the a given participation status, defaults to \"all\"
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'registration_status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_participants" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_user_participants`")

        resource_path = '/v1/appointment_groups/{id}/users'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'registration_status' in params:
            query_params['registration_status'] = params['registration_status']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    # OPERATIONID: update_appointment_group
    def update_appointment_group(self, id, appointment_group_context_codes, **kwargs):
        """
        Update an appointment group
        Update and return an appointment group. If new_appointments are specified, the response will return a new_appointments array (same format as appointments array, see \"List appointment groups\" action).

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_appointment_group_with_http_info(id, appointment_group_context_codes, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: ID (required)
        :param list[str] appointment_group_context_codes: Array of context codes (courses, e.g. course_1) this group should be linked to (1 or more). Users in the course(s) with appropriate permissions will be able to sign up for this appointment group. (required)
        :param list[str] appointment_group_sub_context_codes: Array of sub context codes (course sections or a single group category) this group should be linked to. Used to limit the appointment group to particular sections. If a group category is specified, students will sign up in groups and the participant_type will be \"Group\" instead of \"User\".
        :param str appointment_group_title: Short title for the appointment group.
        :param str appointment_group_description: Longer text description of the appointment group.
        :param str appointment_group_location_name: Location name of the appointment group.
        :param str appointment_group_location_address: Location address.
        :param bool appointment_group_publish: Indicates whether this appointment group should be published (i.e. made available for signup). Once published, an appointment group cannot be unpublished. Defaults to false.
        :param int appointment_group_participants_per_appointment: Maximum number of participants that may register for each time slot. Defaults to null (no limit).
        :param int appointment_group_min_appointments_per_participant: Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots.
        :param int appointment_group_max_appointments_per_participant: Maximum number of time slots a user may register for.
        :param list[str] appointment_group_new_appointments_x: Nested array of start time/end time pairs indicating time slots for this appointment group. Refer to the example request.
        :param str appointment_group_participant_visibility: \"private\":: participants cannot see who has signed up for a particular time slot \"protected\":: participants can see who has signed up. Defaults to \"private\".
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'appointment_group_context_codes', 'appointment_group_sub_context_codes', 'appointment_group_title', 'appointment_group_description', 'appointment_group_location_name', 'appointment_group_location_address', 'appointment_group_publish', 'appointment_group_participants_per_appointment', 'appointment_group_min_appointments_per_participant', 'appointment_group_max_appointments_per_participant', 'appointment_group_new_appointments_x', 'appointment_group_participant_visibility']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('per_page')
        all_params.append('page')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_appointment_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_appointment_group`")
        # verify the required parameter 'appointment_group_context_codes' is set
        if ('appointment_group_context_codes' not in params) or (params['appointment_group_context_codes'] is None):
            raise ValueError("Missing the required parameter `appointment_group_context_codes` when calling `update_appointment_group`")

        resource_path = '/v1/appointment_groups/{id}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = {}
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'page' in params:
            query_params['page'] = params['page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'appointment_group_context_codes' in params:
            form_params.append(('appointment_group[context_codes]', params['appointment_group_context_codes']))
        if 'appointment_group_sub_context_codes' in params:
            form_params.append(('appointment_group[sub_context_codes]', params['appointment_group_sub_context_codes']))
        if 'appointment_group_title' in params:
            form_params.append(('appointment_group[title]', params['appointment_group_title']))
        if 'appointment_group_description' in params:
            form_params.append(('appointment_group[description]', params['appointment_group_description']))
        if 'appointment_group_location_name' in params:
            form_params.append(('appointment_group[location_name]', params['appointment_group_location_name']))
        if 'appointment_group_location_address' in params:
            form_params.append(('appointment_group[location_address]', params['appointment_group_location_address']))
        if 'appointment_group_publish' in params:
            form_params.append(('appointment_group[publish]', params['appointment_group_publish']))
        if 'appointment_group_participants_per_appointment' in params:
            form_params.append(('appointment_group[participants_per_appointment]', params['appointment_group_participants_per_appointment']))
        if 'appointment_group_min_appointments_per_participant' in params:
            form_params.append(('appointment_group[min_appointments_per_participant]', params['appointment_group_min_appointments_per_participant']))
        if 'appointment_group_max_appointments_per_participant' in params:
            form_params.append(('appointment_group[max_appointments_per_participant]', params['appointment_group_max_appointments_per_participant']))
        if 'appointment_group_new_appointments_x' in params:
            form_params.append(('appointment_group[new_appointments][X]', params['appointment_group_new_appointments_x']))
        if 'appointment_group_participant_visibility' in params:
            form_params.append(('appointment_group[participant_visibility]', params['appointment_group_participant_visibility']))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['canvas']

        return self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))