# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.employee_info_attend_trainings import EmployeeInfoAttendTrainings  # noqa: F401,E501
from swagger_server.models.employee_info_certification_info import EmployeeInfoCertificationInfo  # noqa: F401,E501
from swagger_server.models.employee_info_employees_address import EmployeeInfoEmployeesAddress  # noqa: F401,E501
from swagger_server.models.employees import Employees  # noqa: F401,E501
from swagger_server import util


class EmployeeInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, employees: Employees=None, employees_address: EmployeeInfoEmployeesAddress=None, attend_trainings: List[EmployeeInfoAttendTrainings]=None, certification_info: List[EmployeeInfoCertificationInfo]=None):  # noqa: E501
        """EmployeeInfo - a model defined in Swagger

        :param employees: The employees of this EmployeeInfo.  # noqa: E501
        :type employees: Employees
        :param employees_address: The employees_address of this EmployeeInfo.  # noqa: E501
        :type employees_address: EmployeeInfoEmployeesAddress
        :param attend_trainings: The attend_trainings of this EmployeeInfo.  # noqa: E501
        :type attend_trainings: List[EmployeeInfoAttendTrainings]
        :param certification_info: The certification_info of this EmployeeInfo.  # noqa: E501
        :type certification_info: List[EmployeeInfoCertificationInfo]
        """
        self.swagger_types = {
            'employees': Employees,
            'employees_address': EmployeeInfoEmployeesAddress,
            'attend_trainings': List[EmployeeInfoAttendTrainings],
            'certification_info': List[EmployeeInfoCertificationInfo]
        }

        self.attribute_map = {
            'employees': 'employees',
            'employees_address': 'employeesAddress',
            'attend_trainings': 'attendTrainings',
            'certification_info': 'certificationInfo'
        }
        self._employees = employees
        self._employees_address = employees_address
        self._attend_trainings = attend_trainings
        self._certification_info = certification_info

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeeInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EmployeeInfo of this EmployeeInfo.  # noqa: E501
        :rtype: EmployeeInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def employees(self) -> Employees:
        """Gets the employees of this EmployeeInfo.


        :return: The employees of this EmployeeInfo.
        :rtype: Employees
        """
        return self._employees

    @employees.setter
    def employees(self, employees: Employees):
        """Sets the employees of this EmployeeInfo.


        :param employees: The employees of this EmployeeInfo.
        :type employees: Employees
        """

        self._employees = employees

    @property
    def employees_address(self) -> EmployeeInfoEmployeesAddress:
        """Gets the employees_address of this EmployeeInfo.


        :return: The employees_address of this EmployeeInfo.
        :rtype: EmployeeInfoEmployeesAddress
        """
        return self._employees_address

    @employees_address.setter
    def employees_address(self, employees_address: EmployeeInfoEmployeesAddress):
        """Sets the employees_address of this EmployeeInfo.


        :param employees_address: The employees_address of this EmployeeInfo.
        :type employees_address: EmployeeInfoEmployeesAddress
        """

        self._employees_address = employees_address

    @property
    def attend_trainings(self) -> List[EmployeeInfoAttendTrainings]:
        """Gets the attend_trainings of this EmployeeInfo.


        :return: The attend_trainings of this EmployeeInfo.
        :rtype: List[EmployeeInfoAttendTrainings]
        """
        return self._attend_trainings

    @attend_trainings.setter
    def attend_trainings(self, attend_trainings: List[EmployeeInfoAttendTrainings]):
        """Sets the attend_trainings of this EmployeeInfo.


        :param attend_trainings: The attend_trainings of this EmployeeInfo.
        :type attend_trainings: List[EmployeeInfoAttendTrainings]
        """

        self._attend_trainings = attend_trainings

    @property
    def certification_info(self) -> List[EmployeeInfoCertificationInfo]:
        """Gets the certification_info of this EmployeeInfo.


        :return: The certification_info of this EmployeeInfo.
        :rtype: List[EmployeeInfoCertificationInfo]
        """
        return self._certification_info

    @certification_info.setter
    def certification_info(self, certification_info: List[EmployeeInfoCertificationInfo]):
        """Sets the certification_info of this EmployeeInfo.


        :param certification_info: The certification_info of this EmployeeInfo.
        :type certification_info: List[EmployeeInfoCertificationInfo]
        """

        self._certification_info = certification_info
