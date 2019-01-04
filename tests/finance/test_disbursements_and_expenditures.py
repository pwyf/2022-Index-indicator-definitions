from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestDisbursementsAndExpenditures(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'finance',
                            '12_disbursements_and_expenditures.feature')

        tester = BDDTester(steps_path)
        feature = tester.load_feature(feature_path)
        self.test = feature.tests[0]

    def test_disbursement_or_expenditure_non_zero(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction>
            <transaction-type code="{}"/>
            <value>123.45</value>
          </transaction>
        </iati-activity>
        '''

        for transaction_type in ['3', 'D', '4', 'E']:
            activity = etree.fromstring(xml.format(transaction_type))
            result = self.test(activity)

            assert result is True

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

        assert result is False

    def test_disbursement_or_expenditure_zero(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <transaction>
            <transaction-type code="{}"/>
            <value>{}</value>
          </transaction>
        </iati-activity>
        '''

        for transaction_type in ['3', 'D', '4', 'E']:
            for value in ['0', '']:
                activity = etree.fromstring(xml.format(
                    transaction_type,
                    value,
                ))
                result = self.test(activity)

                assert result is False
