@iati-activity
Feature: Flow type

  Scenario Outline: Flow type
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `default-flow-type | transaction/flow-type` should be present

  Scenario Outline: Flow type uses standard codelist
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then every `default-flow-type/@code | transaction/flow-type/@code` should be on the FlowType codelist
