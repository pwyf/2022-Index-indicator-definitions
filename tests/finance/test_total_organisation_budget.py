from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import bdd_tester
from lxml import etree


class TestTotalOrganisationBudget(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'finance', '07_total_organisation_budget.feature')

        tester = bdd_tester(steps_path)
        self.feature = tester.load_feature(feature_path)

        self.test = self.feature.tests[0]

        self.today = '2014-06-01'

    def test_not_an_organisation_file(self):
        xml = '''
        <iati-activity>
          <iati-identifier>asdf1234</iati-identifier>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is None

    def test_total_org_budget_one_year_forward(self):
        xml = '''
        <iati-organisation>
          <total-budget>
            <period-start iso-date="2014-01-01" />
            <period-end iso-date="2014-12-31" />
            <value>10000</value>
          </total-budget>
        </iati-organisation>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_total_org_budget_two_years_forward_not_available(self):
        xml = '''
        <iati-organisation>
          <total-budget>
            <period-start iso-date="2014-01-01" />
            <period-end iso-date="2014-12-31" />
            <value>10000</value>
          </total-budget>
        </iati-organisation>
        '''

        test = self.feature.tests[1]

        activity = etree.fromstring(xml)
        result = test(activity, today=self.today)

        assert result is False

    def test_total_org_budget_available_forward_three_years(self):
        xml = '''
        <iati-organisation>
          <total-budget>
            <period-start iso-date="2014-01-01" />
            <period-end iso-date="2014-12-31" />
            <value currency="USD" value-date="2014-01-01">250000000</value>
          </total-budget>
          <total-budget>
            <period-start iso-date="2015-01-01" />
            <period-end iso-date="2015-12-31" />
            <value currency="USD" value-date="2014-01-01">300000000</value>
          </total-budget>
          <total-budget>
            <period-start iso-date="2016-01-01" />
            <period-end iso-date="2016-12-31" />
            <value currency="USD" value-date="2014-01-01">350000000</value>
          </total-budget>
        </iati-organisation>
        '''

        for test in self.feature.tests:
            activity = etree.fromstring(xml)
            result = test(activity, today=self.today)

            assert result is True
