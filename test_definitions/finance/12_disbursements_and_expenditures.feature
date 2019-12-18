@iati-activity
Feature: Disbursements and expenditures

  Scenario Outline: Disbursements or expenditures are present
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `transaction[transaction-type/@code="3"  or transaction-type/@code="4"]` should be present
