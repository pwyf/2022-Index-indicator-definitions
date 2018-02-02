from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestCurrentData(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', 'test_definitions',
                            'current_data.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        today = '2010-01-01'
        feature = foxpath.load_feature(feature_txt, today=today)
        self.test = feature[1][0][1]

    def test_activity_is_in_implementation(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is True

    def test_activity_is_not_in_implementation(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is False

    def test_activity_recently_ended(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <activity-date type="4" iso-date="2009-09-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is True

    def test_activity_end_is_in_the_future(self):
        xml = '''
        <iati-activity>
          <activity-status code="3"/>
          <activity-date type="4" iso-date="2011-01-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is True

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
        result = self.test(activity)

        assert result[0] is True
