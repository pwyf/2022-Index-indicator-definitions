@iati-activity
Feature: Conditions

  Scenario Outline: Conditions data
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `default-aid-type/@code` is not any of B01, B02, B03, B031, B032, B033, B04, D01, D02, E01, E02, G01, H01, H02, H03, H04 or H05
     Then `conditions` should be present

  Scenario Outline: Conditions document
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `conditions/@attached` is not 0
     And `default-aid-type/@code` is not any of B01, B02, B03, B031, B032, B033, B04, D01, D02, E01, E02, G01, H01, H02, H03, H04 or H05
     Then `document-link/category[@code="A04"]` should be present
