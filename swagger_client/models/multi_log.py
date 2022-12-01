# coding: utf-8

"""
    whylogs container API

    Container that hosts the java version of whylogs behind a REST interface.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MultiLog(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'columns': 'list[str]',
        'data': 'list[list[object]]'
    }

    attribute_map = {
        'columns': 'columns',
        'data': 'data'
    }

    def __init__(self, columns=None, data=None):  # noqa: E501
        """MultiLog - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._data = None
        self.discriminator = None
        self.columns = columns
        self.data = data

    @property
    def columns(self):
        """Gets the columns of this MultiLog.  # noqa: E501


        :return: The columns of this MultiLog.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this MultiLog.


        :param columns: The columns of this MultiLog.  # noqa: E501
        :type: list[str]
        """
        if columns is None:
            raise ValueError("Invalid value for `columns`, must not be `None`")  # noqa: E501

        self._columns = columns

    @property
    def data(self):
        """Gets the data of this MultiLog.  # noqa: E501


        :return: The data of this MultiLog.  # noqa: E501
        :rtype: list[list[object]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this MultiLog.


        :param data: The data of this MultiLog.  # noqa: E501
        :type: list[list[object]]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MultiLog, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MultiLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other