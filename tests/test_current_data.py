from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import bdd_tester
from lxml import etree


class TestCurrentData(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', 'test_definitions',
                            'current_data.feature')

        tester = bdd_tester(steps_path)

        self.today = '2010-01-01'
        feature = tester.load_feature(feature_path)
        self.test = feature.tests[0]

    def test_activity_is_in_implementation(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_activity_is_not_in_implementation(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is False

    def test_activity_recently_ended(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <activity-date type="4" iso-date="2009-09-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_activity_end_is_in_the_future(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <activity-date type="3" iso-date="2011-01-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_activity_has_recent_transaction(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <transaction>
            <transaction-type code="2" />
            <transaction-date iso-date="2009-12-01" />
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True
