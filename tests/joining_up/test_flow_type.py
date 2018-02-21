from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import bdd_tester
from lxml import etree


class TestFlowType(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'joining_up', '24_flow_type.feature')

        tester = bdd_tester(steps_path)
        feature = tester.load_feature(feature_path)
        self.test = feature.tests[1]
        # remove the current data test
        self.test.steps.pop(0)
        self.codelists = {'FlowType': ['10', '20', '21', '22', '30',
                                       '35', '36', '37', '40', '50']}

    def test_flow_types_on_codelist(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <default-flow-type code="20"/>
          <transaction>
            <flow-type code="21"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is True

    def test_flow_types_not_on_codelist(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <default-flow-type code="19"/>
          <transaction>
            <flow-type code="21"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is False

    def test_flow_type_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <transaction>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, codelists=self.codelists)

        assert result is False
