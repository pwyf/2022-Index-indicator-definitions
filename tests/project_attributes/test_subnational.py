from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestSubNational(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'project_attributes', '21_sub-national_location.feature')

        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[1] # location point test

    def test_basic_failure(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is False

    def test_exclusion(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <recipient-region code="998" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)


        assert result is None

    def test_transaction_exclusion(self):

        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction ref="1234" humanitarian="1">
            <aid-type code="B01" />   
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is None

    def test_transaction_exclusion_with_2_trasactions(self):

        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction ref="1234" humanitarian="1">
            <aid-type code="A01" />   
          </transaction>
          <transaction ref="1234" humanitarian="1">
            <aid-type code="B01" />   
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is None

    def test_pass(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <location>
              <point />
          </location>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result is True

