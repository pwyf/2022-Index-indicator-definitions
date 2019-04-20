@iati-activity
Feature: Planned dates

  Scenario Outline: Planned start date is present
    Given an IATI activity
     And the activity is current
     Then `activity-date[@type="1" or @type="start-planned"]` should be present

  Scenario Outline: Planned end date is present
    Given an IATI activity
     And the activity is current
     Then `activity-date[@type="3" or @type="end-planned"]` should be present
