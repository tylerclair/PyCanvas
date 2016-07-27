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
import base64
import urllib3

try:
    import httplib
except ImportError:
    # for python3
    import http.client as httplib

import sys
import logging

from six import iteritems


class Configuration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """
    __shared_state = {}

    def __init__(self,
                 host='https://canvas.instructure.com/api',
                 api_client=None,
                 temp_folder_path=None,
                 logger_format='%(asctime)s %(levelname)s %(message)s',
                 logger_stream_handler=None,
                 logger_file_handler=None,
                 logger_file=None,
                 debug=False,
                 verify_ssl=True,
                 ssl_ca_cert=None,
                 cert_file=None,
                 key_file=None,
                 access_token="",
                 access_token_prefix="Bearer"):
        """
        Constructor
        """
        # Using the borg pattern by alex martelli, multiple instances but shared state, simpler than singletons.
        self.__dict__ = self.__shared_state
        if self.__shared_state == {}:
            # This seems like a hack but lets the existing codegen templates work as is.
            # In a lot of areas the templates create new instances of Configuration with no args.
            # Default Base url
            self.host = host
            # Default api client
            self.api_client = api_client
            # Temp file folder for downloading files
            self.temp_folder_path = temp_folder_path

            # Authentication Settings
            # access token for OAuth
            self.access_token = access_token
            self.access_token_prefix = access_token_prefix

            # Logging Settings
            self.logger = {}
            self.logger["package_logger"] = logging.getLogger("swagger_client")
            self.logger["urllib3_logger"] = logging.getLogger("urllib3")
            # Log format
            self.logger_format = logger_format
            # Log stream handler
            self.logger_stream_handler = logger_stream_handler
            # Log file handler
            self.logger_file_handler = logger_file_handler
            # Debug file location
            self.logger_file = logger_file
            # Debug switch
            self.debug = debug

            # SSL/TLS verification
            # Set this to false to skip verifying SSL certificate when calling API from https server.
            self.verify_ssl = verify_ssl
            # Set this to customize the certificate file to verify the peer.
            self.ssl_ca_cert = ssl_ca_cert
            # client certificate file
            self.cert_file = cert_file
            # client key file
            self.key_file = key_file

    @property
    def logger_file(self):
        """
        Gets the logger_file.
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """
        Sets the logger_file.

        If the logger_file is None, then add stream handler and remove file handler.
        Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """
        Gets the debug status.
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """
        Sets the debug status.

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """
        Gets the logger_format.
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """
        Sets the logger_format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def auth_settings(self):
        """
        Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        return {
            'canvas': 
                {
                    'type': 'oauth2',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': self.access_token_prefix + ' ' + self.access_token
                },
        }

    def to_debug_report(self):
        """
        Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)