# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.training_info import TrainingInfo  # noqa: E501
from swagger_server.models.trainings import Trainings  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTrainingController(BaseTestCase):
    """TrainingController integration test stubs"""

    def test_delete_trainings_training_id(self):
        """Test case for delete_trainings_training_id

        Delete a training row
        """
        response = self.client.open(
            '/trainings/{trainingId}'.format(training_id='training_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_trainings_search_results(self):
        """Test case for get_trainings_search_results

        Get trainings search results
        """
        body = Body1()
        response = self.client.open(
            '/trainings/search',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_trainings_training_id(self):
        """Test case for get_trainings_training_id

        Get a training info
        """
        response = self.client.open(
            '/trainings/{trainingId}'.format(training_id='training_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_trainings_training_id(self):
        """Test case for post_trainings_training_id

        Create a training info
        """
        body = Body2()
        response = self.client.open(
            '/trainings/{trainingId}'.format(training_id='training_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
