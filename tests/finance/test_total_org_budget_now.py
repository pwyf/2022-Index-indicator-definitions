from os.path import dirname, join, realpath
from unittest import TestCase

from foxpath import Foxpath
from lxml import etree


class TestTotalOrgBudgetNow(TestCase):
    def setUp(self):
        self.FILEPATH = dirname(realpath(__file__))
        steps_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                          'step_definitions.py')
        feature_path = join(self.FILEPATH, '..', '..', 'test_definitions',
                            'finance', '07_total_organisation_budget.feature')

        foxpath = Foxpath(steps_path)
        with open(feature_path, 'rb') as f:
            feature_txt = f.read().decode('utf8')

        self.feature = foxpath.load_feature(feature_txt)

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

        results = []
        for test in [x[1] for x in self.feature[1]]:
            activity = etree.fromstring(xml)
            result = test(activity)
            results.append(result[0])
        assert results == [True, True, False]
