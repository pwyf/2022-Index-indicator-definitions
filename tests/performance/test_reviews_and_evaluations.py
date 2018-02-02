from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestReviewsAndEvaluations(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'performance',
                            '32_reviews_and_evaluations.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        feature = foxpath.load_feature(feature_txt)
        self.test = feature[1][0][1]

    def test_activity_in_implementation_so_ignore(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is None

    def test_activity_in_implementation_evaluation_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <document-link>
            <category code="A07"/>
          </document-link>>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is True

    def test_activity_in_completion_evaluation_missing(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is False

    def test_activity_in_completion_but_admin_costs(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <default-aid-type code="G01"/>
          <document-link>
            <category code="A07"/>
          </document-link>>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is None
