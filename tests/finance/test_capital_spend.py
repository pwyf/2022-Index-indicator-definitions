from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestCapitalSpend(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'index_2017', 'finance',
                            '13_capital_spend.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        feature = foxpath.load_feature(feature_txt)
        self.test = feature[1][0][1]

    def test_capital_spend_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
          <default-aid-type code="A09"/>
          <transaction>
            <aid-type code="A03"/>
          </transaction>
          <capital-spend percentage="0"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is True

    def test_capital_spend_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="4"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is False

    def test_capital_spend_not_relevant_status(self):
        xml = '''
        <iati-activity>
          <activity-status code="1"/>
          <capital-spend percentage="100"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is None

    def test_capital_spend_not_relevant_aid_type(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="{}"/>
          <capital-spend percentage="100"/>
        </iati-activity>
        '''

        for aid_type in ['A01', 'A02', 'G01']:
            activity = etree.fromstring(xml.format(aid_type))
            result = self.test(activity)

            assert result[0] is None

    def test_capital_spend_not_relevant_transaction_aid_type(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction>
            <aid-type code="A01"/>
          </transaction>
          <capital-spend percentage="100"/>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is None
