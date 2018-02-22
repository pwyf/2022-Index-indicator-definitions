from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import bdd_tester
from lxml import etree


class TestReviewsAndEvaluations(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'performance',
                            '32_reviews_and_evaluations.feature')

        tester = bdd_tester(steps_path)
        feature = tester.load_feature(feature_path)
        self.test = feature.tests[0]

    def test_activity_in_implementation_so_ignore(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is None

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

        assert result is True

    def test_activity_in_completion_evaluation_missing(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <activity-date type="4" iso-date="2011-01-01"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today="2011-02-01")

        assert result is False

    def test_activity_in_completion_but_admin_costs(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <activity-date type="4" iso-date="2011-01-01"/>
          <default-aid-type code="G01"/>
          <document-link>
            <category code="A07"/>
          </document-link>>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today="2011-02-01")

        assert result is None
