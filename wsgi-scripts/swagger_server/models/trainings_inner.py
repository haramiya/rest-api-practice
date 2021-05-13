# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TrainingsInner(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, training_id: str=None, training_name: str=None, training_class: str=None, it_level: str=None, recruitment_num: float=None, participation_num: float=None, new_flg: str=None, selection_flg: str=None, start_date: date=None, end_date: date=None, skill_class: str=None):  # noqa: E501
        """TrainingsInner - a model defined in Swagger

        :param training_id: The training_id of this TrainingsInner.  # noqa: E501
        :type training_id: str
        :param training_name: The training_name of this TrainingsInner.  # noqa: E501
        :type training_name: str
        :param training_class: The training_class of this TrainingsInner.  # noqa: E501
        :type training_class: str
        :param it_level: The it_level of this TrainingsInner.  # noqa: E501
        :type it_level: str
        :param recruitment_num: The recruitment_num of this TrainingsInner.  # noqa: E501
        :type recruitment_num: float
        :param participation_num: The participation_num of this TrainingsInner.  # noqa: E501
        :type participation_num: float
        :param new_flg: The new_flg of this TrainingsInner.  # noqa: E501
        :type new_flg: str
        :param selection_flg: The selection_flg of this TrainingsInner.  # noqa: E501
        :type selection_flg: str
        :param start_date: The start_date of this TrainingsInner.  # noqa: E501
        :type start_date: date
        :param end_date: The end_date of this TrainingsInner.  # noqa: E501
        :type end_date: date
        :param skill_class: The skill_class of this TrainingsInner.  # noqa: E501
        :type skill_class: str
        """
        self.swagger_types = {
            'training_id': str,
            'training_name': str,
            'training_class': str,
            'it_level': str,
            'recruitment_num': float,
            'participation_num': float,
            'new_flg': str,
            'selection_flg': str,
            'start_date': date,
            'end_date': date,
            'skill_class': str
        }

        self.attribute_map = {
            'training_id': 'trainingId',
            'training_name': 'trainingName',
            'training_class': 'trainingClass',
            'it_level': 'ITLevel',
            'recruitment_num': 'recruitmentNum',
            'participation_num': 'participationNum',
            'new_flg': 'newFlg',
            'selection_flg': 'selectionFlg',
            'start_date': 'startDate',
            'end_date': 'endDate',
            'skill_class': 'skillClass'
        }
        self._training_id = training_id
        self._training_name = training_name
        self._training_class = training_class
        self._it_level = it_level
        self._recruitment_num = recruitment_num
        self._participation_num = participation_num
        self._new_flg = new_flg
        self._selection_flg = selection_flg
        self._start_date = start_date
        self._end_date = end_date
        self._skill_class = skill_class

    @classmethod
    def from_dict(cls, dikt) -> 'TrainingsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Trainings_inner of this TrainingsInner.  # noqa: E501
        :rtype: TrainingsInner
        """
        return util.deserialize_model(dikt, cls)

    @property
    def training_id(self) -> str:
        """Gets the training_id of this TrainingsInner.


        :return: The training_id of this TrainingsInner.
        :rtype: str
        """
        return self._training_id

    @training_id.setter
    def training_id(self, training_id: str):
        """Sets the training_id of this TrainingsInner.


        :param training_id: The training_id of this TrainingsInner.
        :type training_id: str
        """

        self._training_id = training_id

    @property
    def training_name(self) -> str:
        """Gets the training_name of this TrainingsInner.


        :return: The training_name of this TrainingsInner.
        :rtype: str
        """
        return self._training_name

    @training_name.setter
    def training_name(self, training_name: str):
        """Sets the training_name of this TrainingsInner.


        :param training_name: The training_name of this TrainingsInner.
        :type training_name: str
        """

        self._training_name = training_name

    @property
    def training_class(self) -> str:
        """Gets the training_class of this TrainingsInner.


        :return: The training_class of this TrainingsInner.
        :rtype: str
        """
        return self._training_class

    @training_class.setter
    def training_class(self, training_class: str):
        """Sets the training_class of this TrainingsInner.


        :param training_class: The training_class of this TrainingsInner.
        :type training_class: str
        """

        self._training_class = training_class

    @property
    def it_level(self) -> str:
        """Gets the it_level of this TrainingsInner.


        :return: The it_level of this TrainingsInner.
        :rtype: str
        """
        return self._it_level

    @it_level.setter
    def it_level(self, it_level: str):
        """Sets the it_level of this TrainingsInner.


        :param it_level: The it_level of this TrainingsInner.
        :type it_level: str
        """

        self._it_level = it_level

    @property
    def recruitment_num(self) -> float:
        """Gets the recruitment_num of this TrainingsInner.


        :return: The recruitment_num of this TrainingsInner.
        :rtype: float
        """
        return self._recruitment_num

    @recruitment_num.setter
    def recruitment_num(self, recruitment_num: float):
        """Sets the recruitment_num of this TrainingsInner.


        :param recruitment_num: The recruitment_num of this TrainingsInner.
        :type recruitment_num: float
        """

        self._recruitment_num = recruitment_num

    @property
    def participation_num(self) -> float:
        """Gets the participation_num of this TrainingsInner.


        :return: The participation_num of this TrainingsInner.
        :rtype: float
        """
        return self._participation_num

    @participation_num.setter
    def participation_num(self, participation_num: float):
        """Sets the participation_num of this TrainingsInner.


        :param participation_num: The participation_num of this TrainingsInner.
        :type participation_num: float
        """

        self._participation_num = participation_num

    @property
    def new_flg(self) -> str:
        """Gets the new_flg of this TrainingsInner.


        :return: The new_flg of this TrainingsInner.
        :rtype: str
        """
        return self._new_flg

    @new_flg.setter
    def new_flg(self, new_flg: str):
        """Sets the new_flg of this TrainingsInner.


        :param new_flg: The new_flg of this TrainingsInner.
        :type new_flg: str
        """

        self._new_flg = new_flg

    @property
    def selection_flg(self) -> str:
        """Gets the selection_flg of this TrainingsInner.


        :return: The selection_flg of this TrainingsInner.
        :rtype: str
        """
        return self._selection_flg

    @selection_flg.setter
    def selection_flg(self, selection_flg: str):
        """Sets the selection_flg of this TrainingsInner.


        :param selection_flg: The selection_flg of this TrainingsInner.
        :type selection_flg: str
        """

        self._selection_flg = selection_flg

    @property
    def start_date(self) -> date:
        """Gets the start_date of this TrainingsInner.


        :return: The start_date of this TrainingsInner.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this TrainingsInner.


        :param start_date: The start_date of this TrainingsInner.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def end_date(self) -> date:
        """Gets the end_date of this TrainingsInner.


        :return: The end_date of this TrainingsInner.
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date: date):
        """Sets the end_date of this TrainingsInner.


        :param end_date: The end_date of this TrainingsInner.
        :type end_date: date
        """

        self._end_date = end_date

    @property
    def skill_class(self) -> str:
        """Gets the skill_class of this TrainingsInner.


        :return: The skill_class of this TrainingsInner.
        :rtype: str
        """
        return self._skill_class

    @skill_class.setter
    def skill_class(self, skill_class: str):
        """Sets the skill_class of this TrainingsInner.


        :param skill_class: The skill_class of this TrainingsInner.
        :type skill_class: str
        """

        self._skill_class = skill_class
