# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class EmployeeInfoAttendTrainings(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, training_name: str=None, start_date: date=None, attendance_state: str=None, satisfaction_score: float=None):  # noqa: E501
        """EmployeeInfoAttendTrainings - a model defined in Swagger

        :param training_name: The training_name of this EmployeeInfoAttendTrainings.  # noqa: E501
        :type training_name: str
        :param start_date: The start_date of this EmployeeInfoAttendTrainings.  # noqa: E501
        :type start_date: date
        :param attendance_state: The attendance_state of this EmployeeInfoAttendTrainings.  # noqa: E501
        :type attendance_state: str
        :param satisfaction_score: The satisfaction_score of this EmployeeInfoAttendTrainings.  # noqa: E501
        :type satisfaction_score: float
        """
        self.swagger_types = {
            'training_name': str,
            'start_date': date,
            'attendance_state': str,
            'satisfaction_score': float
        }

        self.attribute_map = {
            'training_name': 'trainingName',
            'start_date': 'startDate',
            'attendance_state': 'attendance_state',
            'satisfaction_score': 'satisfactionScore'
        }
        self._training_name = training_name
        self._start_date = start_date
        self._attendance_state = attendance_state
        self._satisfaction_score = satisfaction_score

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeeInfoAttendTrainings':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmployeeInfo_attendTrainings of this EmployeeInfoAttendTrainings.  # noqa: E501
        :rtype: EmployeeInfoAttendTrainings
        """
        return util.deserialize_model(dikt, cls)

    @property
    def training_name(self) -> str:
        """Gets the training_name of this EmployeeInfoAttendTrainings.


        :return: The training_name of this EmployeeInfoAttendTrainings.
        :rtype: str
        """
        return self._training_name

    @training_name.setter
    def training_name(self, training_name: str):
        """Sets the training_name of this EmployeeInfoAttendTrainings.


        :param training_name: The training_name of this EmployeeInfoAttendTrainings.
        :type training_name: str
        """

        self._training_name = training_name

    @property
    def start_date(self) -> date:
        """Gets the start_date of this EmployeeInfoAttendTrainings.


        :return: The start_date of this EmployeeInfoAttendTrainings.
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date: date):
        """Sets the start_date of this EmployeeInfoAttendTrainings.


        :param start_date: The start_date of this EmployeeInfoAttendTrainings.
        :type start_date: date
        """

        self._start_date = start_date

    @property
    def attendance_state(self) -> str:
        """Gets the attendance_state of this EmployeeInfoAttendTrainings.


        :return: The attendance_state of this EmployeeInfoAttendTrainings.
        :rtype: str
        """
        return self._attendance_state

    @attendance_state.setter
    def attendance_state(self, attendance_state: str):
        """Sets the attendance_state of this EmployeeInfoAttendTrainings.


        :param attendance_state: The attendance_state of this EmployeeInfoAttendTrainings.
        :type attendance_state: str
        """

        self._attendance_state = attendance_state

    @property
    def satisfaction_score(self) -> float:
        """Gets the satisfaction_score of this EmployeeInfoAttendTrainings.


        :return: The satisfaction_score of this EmployeeInfoAttendTrainings.
        :rtype: float
        """
        return self._satisfaction_score

    @satisfaction_score.setter
    def satisfaction_score(self, satisfaction_score: float):
        """Sets the satisfaction_score of this EmployeeInfoAttendTrainings.


        :param satisfaction_score: The satisfaction_score of this EmployeeInfoAttendTrainings.
        :type satisfaction_score: float
        """

        self._satisfaction_score = satisfaction_score
