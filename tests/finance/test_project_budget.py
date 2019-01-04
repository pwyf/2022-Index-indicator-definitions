from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import BDDTester
from lxml import etree


class TestProjectBudget(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'finance', '09_project_budget.feature')

        self.today = '2010-01-01'
        tester = BDDTester(steps_path)
        self.feature = tester.load_feature(feature_path)
        self.test = self.feature.tests[0]

    def test_default_aid_type_not_relevant(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <default-aid-type code="G01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is None

    def test_budget_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="end-actual" iso-date="2010-07-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is False

    def test_end_too_soon_not_relevant(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="3" iso-date="2010-06-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is None

    def test_multiple_dates_budget_not_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="3" iso-date="2010-05-01" />
          <activity-date type="4" iso-date="2010-07-01" />
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is False

    def test_annual_budget_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="4" iso-date="2010-07-01" />
          <budget>
            <period-start iso-date="2009-07-01"/>
            <period-end iso-date="2010-07-01"/>
            <value>10000</value>
          </budget>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is True

    def test_annual_budget_period_too_long(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="4" iso-date="2010-07-01" />
          <budget>
            <period-start iso-date="2009-06-01"/>
            <period-end iso-date="2010-07-01"/>
            <value>10000</value>
          </budget>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is False

    def test_annual_budget_no_dates(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="4" iso-date="2010-07-01" />
          <budget>
            <value>10000</value>
          </budget>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is False

    def test_annual_budget_bad_dates(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="4" iso-date="2010-07-01" />
          <budget>
            <period-start iso-date="hello"/>
            <period-end iso-date="uh-oh"/>
            <value>10000</value>
          </budget>
        </iati-activity>
        '''

        activity = etree.fromstring(xml)
        result = self.test(activity, today=self.today)

        assert result is False

    def test_quarterly_budget_period_too_long(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="4" iso-date="2010-07-01" />
          <budget>
            <period-start iso-date="2010-01-01"/>
            <period-end iso-date="2010-07-01"/>
            <value>10000</value>
          </budget>
        </iati-activity>
        '''

        test = self.feature.tests[1]

        activity = etree.fromstring(xml)
        result = test(activity, today=self.today)

        assert result is False

    def test_quarterly_budget_present(self):
        xml = '''
        <iati-activity>
          <activity-status code="2"/>
          <activity-date type="4" iso-date="2010-07-01" />
          <budget>
            <period-start iso-date="2010-04-01"/>
            <period-end iso-date="2010-07-01"/>
            <value>10000</value>
          </budget>
        </iati-activity>
        '''

        test = self.feature.tests[1]

        activity = etree.fromstring(xml)
        result = test(activity, today=self.today)

        assert result is True
