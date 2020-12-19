# coding: utf-8

"""
    Selling Partner API for Orders

    The Selling Partner API for Orders helps you programmatically retrieve order information. These APIs let you develop fast, flexible, custom applications in areas like order synchronization, order research, and demand-based decision support tools.  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class OrderItemsBuyerInfoList(object):
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
        'order_items': 'OrderItemBuyerInfoList',
        'next_token': 'str',
        'amazon_order_id': 'str'
    }

    attribute_map = {
        'order_items': 'OrderItems',
        'next_token': 'NextToken',
        'amazon_order_id': 'AmazonOrderId'
    }

    def __init__(self, order_items=None, next_token=None, amazon_order_id=None):  # noqa: E501
        """OrderItemsBuyerInfoList - a model defined in Swagger"""  # noqa: E501
        self._order_items = None
        self._next_token = None
        self._amazon_order_id = None
        self.discriminator = None
        self.order_items = order_items
        if next_token is not None:
            self.next_token = next_token
        self.amazon_order_id = amazon_order_id

    @property
    def order_items(self):
        """Gets the order_items of this OrderItemsBuyerInfoList.  # noqa: E501


        :return: The order_items of this OrderItemsBuyerInfoList.  # noqa: E501
        :rtype: OrderItemBuyerInfoList
        """
        return self._order_items

    @order_items.setter
    def order_items(self, order_items):
        """Sets the order_items of this OrderItemsBuyerInfoList.


        :param order_items: The order_items of this OrderItemsBuyerInfoList.  # noqa: E501
        :type: OrderItemBuyerInfoList
        """
        if order_items is None:
            raise ValueError("Invalid value for `order_items`, must not be `None`")  # noqa: E501

        self._order_items = order_items

    @property
    def next_token(self):
        """Gets the next_token of this OrderItemsBuyerInfoList.  # noqa: E501

        When present and not empty, pass this string token in the next request to return the next response page.  # noqa: E501

        :return: The next_token of this OrderItemsBuyerInfoList.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this OrderItemsBuyerInfoList.

        When present and not empty, pass this string token in the next request to return the next response page.  # noqa: E501

        :param next_token: The next_token of this OrderItemsBuyerInfoList.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def amazon_order_id(self):
        """Gets the amazon_order_id of this OrderItemsBuyerInfoList.  # noqa: E501

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :return: The amazon_order_id of this OrderItemsBuyerInfoList.  # noqa: E501
        :rtype: str
        """
        return self._amazon_order_id

    @amazon_order_id.setter
    def amazon_order_id(self, amazon_order_id):
        """Sets the amazon_order_id of this OrderItemsBuyerInfoList.

        An Amazon-defined order identifier, in 3-7-7 format.  # noqa: E501

        :param amazon_order_id: The amazon_order_id of this OrderItemsBuyerInfoList.  # noqa: E501
        :type: str
        """
        if amazon_order_id is None:
            raise ValueError("Invalid value for `amazon_order_id`, must not be `None`")  # noqa: E501

        self._amazon_order_id = amazon_order_id

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
        if issubclass(OrderItemsBuyerInfoList, dict):
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
        if not isinstance(other, OrderItemsBuyerInfoList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other