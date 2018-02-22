from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import bdd_tester
from lxml import etree


class TestProcurement(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'joining_up', '29_project_procurement.feature')

        tester = bdd_tester(steps_path)
        feature = tester.load_feature(feature_path)
        self.test = feature.tests[1]

    def test_contract_is_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
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

        assert result is True
