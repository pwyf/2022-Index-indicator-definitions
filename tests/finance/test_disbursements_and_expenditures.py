from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestDisbursementsAndExpenditures(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'finance', '12_disbursements_and_expenditures.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        feature = foxpath.load_feature(feature_txt)
        self.test = feature[1][0][1]

    def test_disbursement_or_expenditure_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction>
            <transaction-type code="{}"/>
          </transaction>
        </iati-activity>
        '''

        for transaction_type in ['3', 'D', '4', 'E']:
            activity = etree.fromstring(xml.format(transaction_type))
            result = self.test(activity)

            assert result[0] is True

    def test_disbursement_or_expenditure_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction>
            <transaction-type code="C"/>
          </transaction>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity)

        assert result[0] is False
