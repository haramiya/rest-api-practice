# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.employee_info import EmployeeInfo  # noqa: E501
from swagger_server.models.employees import Employees  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEmployeeController(BaseTestCase):
    """EmployeeController integration test stubs"""

    def test_get_employees_employee_id(self):
        """Test case for get_employees_employee_id

        Get an employee info
        """
        response = self.client.open(
            '/employees/{employeeId}'.format(employee_id='employee_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_employees_search_results(self):
        """Test case for get_employees_search_results

        Get employee's search results
        """
        body = Body()
        response = self.client.open(
            '/employees/search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
