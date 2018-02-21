from os.path import dirname, join, realpath
from unittest import TestCase

from bdd_tester import bdd_tester
from lxml import etree


class TestTotalOrgBudgetNow(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'finance', '07_total_organisation_budget.feature')

        tester = bdd_tester(steps_path)
        self.feature = tester.load_feature(feature_path)

    def test_organisation_file(self):
        xml = '''
        <iati-organisation>
          <total-budget>
          <period-start iso-date="2016-01-01"/>
          <period-end iso-date="2016-12-31"/>
          <value value-date="2016-01-01">4348000300.00</value>
          <budget-line>
          <value value-date="2016-01-01">4348000300.00</value>
          <narrative>Disbursements trajectory</narrative>
          </budget-line>
          </total-budget>
          <total-budget>
          <period-start iso-date="2017-01-01"/>
          <period-end iso-date="2017-12-31"/>
          <value value-date="2017-01-01">368350016.00</value>
          <budget-line>
          <value value-date="2017-01-01">368350016.00</value>
          <narrative>Administrative Budget</narrative>
          </budget-line>
          </total-budget>
          <total-budget>
          <period-start iso-date="2017-01-01"/>
          <period-end iso-date="2017-12-31"/>
          <value value-date="2017-01-01">5651999700.00</value>
          <budget-line>
          <value value-date="2017-01-01">5651999700.00</value>
          <narrative>Disbursements trajectory</narrative>
          </budget-line>
          </total-budget>
          <total-budget>
          <period-start iso-date="2018-01-01"/>
          <period-end iso-date="2018-12-31"/>
          <value value-date="2018-01-01">392240000.00</value>
          <budget-line>
          <value value-date="2018-01-01">392240000.00</value>
          <narrative>Administrative Budget</narrative>
          </budget-line>
          </total-budget>
          <total-budget>
          <period-start iso-date="2018-01-01"/>
          <period-end iso-date="2018-12-31"/>
          <value value-date="2018-01-01">6303000100.00</value>
          <budget-line>
          <value value-date="2018-01-01">6303000100.00</value>
          <narrative>Disbursements trajectory</narrative>
          </budget-line>
          </total-budget>
          <total-budget>
          <period-start iso-date="2019-01-01"/>
          <period-end iso-date="2019-12-31"/>
          <value value-date="2019-01-01">397880000.00</value>
          <budget-line>
          <value value-date="2019-01-01">397880000.00</value>
          <narrative>Administrative Budget</narrative>
          </budget-line>
          </total-budget>
        </iati-organisation>
        '''

        expected_results = [True, True, False]
        for test in self.feature.tests:
            activity = etree.fromstring(xml)
            expected_result = expected_results.pop(0)
            assert test(activity) is expected_result
