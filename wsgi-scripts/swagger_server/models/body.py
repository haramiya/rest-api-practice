# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, employee_id: str=None, employee_name: str=None, dept: List[str]=None, joining_year_from: date=None, joining_year_to: date=None, title: List[str]=None, grade: List[str]=None, recruitment_class: List[str]=None, leave_flg: List[str]=None, gender: List[str]=None, birthdate_from: date=None, birthdate_to: date=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param employee_id: The employee_id of this Body.  # noqa: E501
        :type employee_id: str
        :param employee_name: The employee_name of this Body.  # noqa: E501
        :type employee_name: str
        :param dept: The dept of this Body.  # noqa: E501
        :type dept: List[str]
        :param joining_year_from: The joining_year_from of this Body.  # noqa: E501
        :type joining_year_from: date
        :param joining_year_to: The joining_year_to of this Body.  # noqa: E501
        :type joining_year_to: date
        :param title: The title of this Body.  # noqa: E501
        :type title: List[str]
        :param grade: The grade of this Body.  # noqa: E501
        :type grade: List[str]
        :param recruitment_class: The recruitment_class of this Body.  # noqa: E501
        :type recruitment_class: List[str]
        :param leave_flg: The leave_flg of this Body.  # noqa: E501
        :type leave_flg: List[str]
        :param gender: The gender of this Body.  # noqa: E501
        :type gender: List[str]
        :param birthdate_from: The birthdate_from of this Body.  # noqa: E501
        :type birthdate_from: date
        :param birthdate_to: The birthdate_to of this Body.  # noqa: E501
        :type birthdate_to: date
        """
        self.swagger_types = {
            'employee_id': str,
            'employee_name': str,
            'dept': List[str],
            'joining_year_from': date,
            'joining_year_to': date,
            'title': List[str],
            'grade': List[str],
            'recruitment_class': List[str],
            'leave_flg': List[str],
            'gender': List[str],
            'birthdate_from': date,
            'birthdate_to': date
        }

        self.attribute_map = {
            'employee_id': 'employeeId',
            'employee_name': 'employeeName',
            'dept': 'dept',
            'joining_year_from': 'joiningYearFrom',
            'joining_year_to': 'joiningYearTo',
            'title': 'title',
            'grade': 'grade',
            'recruitment_class': 'recruitmentClass',
            'leave_flg': 'leaveFlg',
            'gender': 'gender',
            'birthdate_from': 'birthdateFrom',
            'birthdate_to': 'birthdateTo'
        }
        self._employee_id = employee_id
        self._employee_name = employee_name
        self._dept = dept
        self._joining_year_from = joining_year_from
        self._joining_year_to = joining_year_to
        self._title = title
        self._grade = grade
        self._recruitment_class = recruitment_class
        self._leave_flg = leave_flg
        self._gender = gender
        self._birthdate_from = birthdate_from
        self._birthdate_to = birthdate_to

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def employee_id(self) -> str:
        """Gets the employee_id of this Body.


        :return: The employee_id of this Body.
        :rtype: str
        """
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id: str):
        """Sets the employee_id of this Body.


        :param employee_id: The employee_id of this Body.
        :type employee_id: str
        """

        self._employee_id = employee_id

    @property
    def employee_name(self) -> str:
        """Gets the employee_name of this Body.


        :return: The employee_name of this Body.
        :rtype: str
        """
        return self._employee_name

    @employee_name.setter
    def employee_name(self, employee_name: str):
        """Sets the employee_name of this Body.


        :param employee_name: The employee_name of this Body.
        :type employee_name: str
        """

        self._employee_name = employee_name

    @property
    def dept(self) -> List[str]:
        """Gets the dept of this Body.


        :return: The dept of this Body.
        :rtype: List[str]
        """
        return self._dept

    @dept.setter
    def dept(self, dept: List[str]):
        """Sets the dept of this Body.


        :param dept: The dept of this Body.
        :type dept: List[str]
        """

        self._dept = dept

    @property
    def joining_year_from(self) -> date:
        """Gets the joining_year_from of this Body.


        :return: The joining_year_from of this Body.
        :rtype: date
        """
        return self._joining_year_from

    @joining_year_from.setter
    def joining_year_from(self, joining_year_from: date):
        """Sets the joining_year_from of this Body.


        :param joining_year_from: The joining_year_from of this Body.
        :type joining_year_from: date
        """

        self._joining_year_from = joining_year_from

    @property
    def joining_year_to(self) -> date:
        """Gets the joining_year_to of this Body.


        :return: The joining_year_to of this Body.
        :rtype: date
        """
        return self._joining_year_to

    @joining_year_to.setter
    def joining_year_to(self, joining_year_to: date):
        """Sets the joining_year_to of this Body.


        :param joining_year_to: The joining_year_to of this Body.
        :type joining_year_to: date
        """

        self._joining_year_to = joining_year_to

    @property
    def title(self) -> List[str]:
        """Gets the title of this Body.


        :return: The title of this Body.
        :rtype: List[str]
        """
        return self._title

    @title.setter
    def title(self, title: List[str]):
        """Sets the title of this Body.


        :param title: The title of this Body.
        :type title: List[str]
        """

        self._title = title

    @property
    def grade(self) -> List[str]:
        """Gets the grade of this Body.


        :return: The grade of this Body.
        :rtype: List[str]
        """
        return self._grade

    @grade.setter
    def grade(self, grade: List[str]):
        """Sets the grade of this Body.


        :param grade: The grade of this Body.
        :type grade: List[str]
        """

        self._grade = grade

    @property
    def recruitment_class(self) -> List[str]:
        """Gets the recruitment_class of this Body.


        :return: The recruitment_class of this Body.
        :rtype: List[str]
        """
        return self._recruitment_class

    @recruitment_class.setter
    def recruitment_class(self, recruitment_class: List[str]):
        """Sets the recruitment_class of this Body.


        :param recruitment_class: The recruitment_class of this Body.
        :type recruitment_class: List[str]
        """

        self._recruitment_class = recruitment_class

    @property
    def leave_flg(self) -> List[str]:
        """Gets the leave_flg of this Body.


        :return: The leave_flg of this Body.
        :rtype: List[str]
        """
        return self._leave_flg

    @leave_flg.setter
    def leave_flg(self, leave_flg: List[str]):
        """Sets the leave_flg of this Body.


        :param leave_flg: The leave_flg of this Body.
        :type leave_flg: List[str]
        """

        self._leave_flg = leave_flg

    @property
    def gender(self) -> List[str]:
        """Gets the gender of this Body.


        :return: The gender of this Body.
        :rtype: List[str]
        """
        return self._gender

    @gender.setter
    def gender(self, gender: List[str]):
        """Sets the gender of this Body.


        :param gender: The gender of this Body.
        :type gender: List[str]
        """

        self._gender = gender

    @property
    def birthdate_from(self) -> date:
        """Gets the birthdate_from of this Body.


        :return: The birthdate_from of this Body.
        :rtype: date
        """
        return self._birthdate_from

    @birthdate_from.setter
    def birthdate_from(self, birthdate_from: date):
        """Sets the birthdate_from of this Body.


        :param birthdate_from: The birthdate_from of this Body.
        :type birthdate_from: date
        """

        self._birthdate_from = birthdate_from

    @property
    def birthdate_to(self) -> date:
        """Gets the birthdate_to of this Body.


        :return: The birthdate_to of this Body.
        :rtype: date
        """
        return self._birthdate_to

    @birthdate_to.setter
    def birthdate_to(self, birthdate_to: date):
        """Sets the birthdate_to of this Body.


        :param birthdate_to: The birthdate_to of this Body.
        :type birthdate_to: date
        """

        self._birthdate_to = birthdate_to
