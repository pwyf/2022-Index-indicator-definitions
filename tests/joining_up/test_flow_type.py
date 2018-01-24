from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestFlowType(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'index_2017', 'joining_up',
                            '24_flow_type.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        codelists = {'FlowType': ['10', '20', '21', '22', '30',
                                  '35', '36', '37', '40', '50']}
        feature = foxpath.load_feature(feature_txt, codelists=codelists)
        self.test = feature[1][1][1]

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
        result = self.test(activity)

        assert result[0] is True

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
        result = self.test(activity)

        assert result[0] is False

    def test_flow_type_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <transaction>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is False
