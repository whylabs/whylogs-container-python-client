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

class Message(object):
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
        'attributes': 'dict(str, str)',
        'data': 'str',
        'message_id': 'str',
        'publish_time': 'str',
        'ordering_key': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'data': 'data',
        'message_id': 'messageId',
        'publish_time': 'publishTime',
        'ordering_key': 'orderingKey'
    }

    def __init__(self, attributes=None, data=None, message_id=None, publish_time=None, ordering_key=None):  # noqa: E501
        """Message - a model defined in Swagger"""  # noqa: E501
        self._attributes = None
        self._data = None
        self._message_id = None
        self._publish_time = None
        self._ordering_key = None
        self.discriminator = None
        if attributes is not None:
            self.attributes = attributes
        self.data = data
        self.message_id = message_id
        self.publish_time = publish_time
        if ordering_key is not None:
            self.ordering_key = ordering_key

    @property
    def attributes(self):
        """Gets the attributes of this Message.  # noqa: E501


        :return: The attributes of this Message.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this Message.


        :param attributes: The attributes of this Message.  # noqa: E501
        :type: dict(str, str)
        """

        self._attributes = attributes

    @property
    def data(self):
        """Gets the data of this Message.  # noqa: E501

        The message data field. If this field is empty, the message must contain at least one attribute.  # noqa: E501

        :return: The data of this Message.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Message.

        The message data field. If this field is empty, the message must contain at least one attribute.  # noqa: E501

        :param data: The data of this Message.  # noqa: E501
        :type: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def message_id(self):
        """Gets the message_id of this Message.  # noqa: E501


        :return: The message_id of this Message.  # noqa: E501
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this Message.


        :param message_id: The message_id of this Message.  # noqa: E501
        :type: str
        """
        if message_id is None:
            raise ValueError("Invalid value for `message_id`, must not be `None`")  # noqa: E501

        self._message_id = message_id

    @property
    def publish_time(self):
        """Gets the publish_time of this Message.  # noqa: E501

        A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits  # noqa: E501

        :return: The publish_time of this Message.  # noqa: E501
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this Message.

        A timestamp in RFC3339 UTC 'Zulu' format, with nanosecond resolution and up to nine fractional digits  # noqa: E501

        :param publish_time: The publish_time of this Message.  # noqa: E501
        :type: str
        """
        if publish_time is None:
            raise ValueError("Invalid value for `publish_time`, must not be `None`")  # noqa: E501

        self._publish_time = publish_time

    @property
    def ordering_key(self):
        """Gets the ordering_key of this Message.  # noqa: E501

        If non-empty, identifies related messages for which publish order should be respected  # noqa: E501

        :return: The ordering_key of this Message.  # noqa: E501
        :rtype: str
        """
        return self._ordering_key

    @ordering_key.setter
    def ordering_key(self, ordering_key):
        """Sets the ordering_key of this Message.

        If non-empty, identifies related messages for which publish order should be respected  # noqa: E501

        :param ordering_key: The ordering_key of this Message.  # noqa: E501
        :type: str
        """

        self._ordering_key = ordering_key

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
        if issubclass(Message, dict):
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
        if not isinstance(other, Message):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
