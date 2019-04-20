@iati-activity
Feature: Contact details

  Scenario Outline: Contact info is present
    Given an IATI activity
     And the activity is current
     Then `contact-info` should be present
