from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestProcurement(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'index_2017', 'joining_up',
                            '29_project_procurement.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        feature = foxpath.load_feature(feature_txt)
        self.test = feature[1][1][1]

    def test_contract_is_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <default-aid-type code="C01"/>
          <document-link>
            <category code="A11"/>
          </document-link>
          <document-link>
            <category code="A06"/>
          </document-link>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is True
