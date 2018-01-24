from datetime import date
from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestTotalOrganisationBudget(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'index_2017', 'finance',
                            '07_total_organisation_budget.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        today = date(2014, 6, 1)
        self.feature = foxpath.load_feature(feature_txt, today=today)

    def test_not_an_organisation_file(self):
        xml = '''
        <iati-activity>
          <iati-identifier>asdf1234</iati-identifier>
        </iati-activity>
        '''

        test = self.feature[1][0][1]

        activity = etree.fromstring(xml)
        result = test(activity)

        assert result[0] is None

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

        test = self.feature[1][0][1]

        activity = etree.fromstring(xml)
        result = test(activity)

        assert result[0] is True

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

        test = self.feature[1][1][1]

        activity = etree.fromstring(xml)
        result = test(activity)

        assert result[0] is False

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

        for test in [x[1] for x in self.feature[1]]:
            activity = etree.fromstring(xml)
            result = test(activity)

            assert result[0] is True
