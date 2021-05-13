# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, training_name: str=None, training_class: List[str]=None, skill_class: List[str]=None, it_level: List[str]=None, recruitment_num_from: float=None, recruitment_num_to: float=None, new_flg: List[str]=None, selection_flg: List[str]=None, start_date: date=None, end_date: date=None):  # noqa: E501
        """Body1 - a model defined in Swagger

        :param training_name: The training_name of this Body1.  # noqa: E501
        :type training_name: str
        :param training_class: The training_class of this Body1.  # noqa: E501
        :type training_class: List[str]
        :param skill_class: The skill_class of this Body1.  # noqa: E501
        :type skill_class: List[str]
        :param it_level: The it_level of this Body1.  # noqa: E501
        :type it_level: List[str]
        :param recruitment_num_from: The recruitment_num_from of this Body1.  # noqa: E501
        :type recruitment_num_from: float
        :param recruitment_num_to: The recruitment_num_to of this Body1.  # noqa: E501
        :type recruitment_num_to: float
        :param new_flg: The new_flg of this Body1.  # noqa: E501
        :type new_flg: List[str]
        :param selection_flg: The selection_flg of this Body1.  # noqa: E501
        :type selection_flg: List[str]
        :param start_date: The start_date of this Body1.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this Body1.  # noqa: E501
        :type end_date: date
        """
        self.swagger_types = {
            'training_name': str,
            'training_class': List[str],
            'skill_class': List[str],
            'it_level': List[str],
            'recruitment_num_from': float,
            'recruitment_num_to': float,
            'new_flg': List[str],
            'selection_flg': List[str],
            'start_date': date,
            'end_date': date
        }

        self.attribute_map = {
            'training_name': 'trainingName',
            'training_class': 'trainingClass',
            'skill_class': 'skillClass',
            'it_level': 'ITLevel',
            'recruitment_num_from': 'recruitmentNumFrom',
            'recruitment_num_to': 'recruitmentNumTo',
            'new_flg': 'newFlg',
            'selection_flg': 'selectionFlg',
            'start_date': 'startDate',
            'end_date': 'endDate'
        }
        self._training_name = training_name
        self._training_class = training_class
        self._skill_class = skill_class
        self._it_level = it_level
        self._recruitment_num_from = recruitment_num_from
        self._recruitment_num_to = recruitment_num_to
        self._new_flg = new_flg
        self._selection_flg = selection_flg
        self._start_date = start_date
        self._end_date = end_date

    @classmethod
    def from_dict(cls, dikt) -> 'Body1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_1 of this Body1.  # noqa: E501
        :rtype: Body1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def training_name(self) -> str:
        """Gets the training_name of this Body1.


        :return: The training_name of this Body1.
        :rtype: str
        """
        return self._training_name

    @training_name.setter
    def training_name(self, training_name: str):
        """Sets the training_name of this Body1.


        :param training_name: The training_name of this Body1.
        :type training_name: str
        """

        self._training_name = training_name

    @property
    def training_class(self) -> List[str]:
        """Gets the training_class of this Body1.


        :return: The training_class of this Body1.
        :rtype: List[str]
        """
        return self._training_class

    @training_class.setter
    def training_class(self, training_class: List[str]):
        """Sets the training_class of this Body1.


        :param training_class: The training_class of this Body1.
        :type training_class: List[str]
        """

        self._training_class = training_class

    @property
    def skill_class(self) -> List[str]:
        """Gets the skill_class of this Body1.


        :return: The skill_class of this Body1.
        :rtype: List[str]
        """
        return self._skill_class

    @skill_class.setter
    def skill_class(self, skill_class: List[str]):
        """Sets the skill_class of this Body1.


        :param skill_class: The skill_class of this Body1.
        :type skill_class: List[str]
        """

        self._skill_class = skill_class

    @property
    def it_level(self) -> List[str]:
        """Gets the it_level of this Body1.


        :return: The it_level of this Body1.
        :rtype: List[str]
        """
        return self._it_level

    @it_level.setter
    def it_level(self, it_level: List[str]):
        """Sets the it_level of this Body1.


        :param it_level: The it_level of this Body1.
        :type it_level: List[str]
        """

        self._it_level = it_level

    @property
    def recruitment_num_from(self) -> float:
        """Gets the recruitment_num_from of this Body1.


        :return: The recruitment_num_from of this Body1.
        :rtype: float
        """
        return self._recruitment_num_from

    @recruitment_num_from.setter
    def recruitment_num_from(self, recruitment_num_from: float):
        """Sets the recruitment_num_from of this Body1.


        :param recruitment_num_from: The recruitment_num_from of this Body1.
        :type recruitment_num_from: float
        """

        self._recruitment_num_from = recruitment_num_from

    @property
    def recruitment_num_to(self) -> float:
        """Gets the recruitment_num_to of this Body1.


        :return: The recruitment_num_to of this Body1.
        :rtype: float
        """
        return self._recruitment_num_to

    @recruitment_num_to.setter
    def recruitment_num_to(self, recruitment_num_to: float):
        """Sets the recruitment_num_to of this Body1.


        :param recruitment_num_to: The recruitment_num_to of this Body1.
        :type recruitment_num_to: float
        """

        self._recruitment_num_to = recruitment_num_to

    @property
    def new_flg(self) -> List[str]:
        """Gets the new_flg of this Body1.


        :return: The new_flg of this Body1.
        :rtype: List[str]
        """
        return self._new_flg

    @new_flg.setter
    def new_flg(self, new_flg: List[str]):
        """Sets the new_flg of this Body1.


        :param new_flg: The new_flg of this Body1.
        :type new_flg: List[str]
        """

        self._new_flg = new_flg

    @property
    def selection_flg(self) -> List[str]:
        """Gets the selection_flg of this Body1.


        :return: The selection_flg of this Body1.
        :rtype: List[str]
        """
        return self._selection_flg

    @selection_flg.setter
    def selection_flg(self, selection_flg: List[str]):
        """Sets the selection_flg of this Body1.


        :param selection_flg: The selection_flg of this Body1.
        :type selection_flg: List[str]
        """

        self._selection_flg = selection_flg

    @property
    def start_date(self) -> date:
        """Gets the start_date of this Body1.


        :return: The start_date of this Body1.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this Body1.


        :param start_date: The start_date of this Body1.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this Body1.


        :return: The end_date of this Body1.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this Body1.


        :param end_date: The end_date of this Body1.
        :type end_date: date
        """

        self._end_date = end_date