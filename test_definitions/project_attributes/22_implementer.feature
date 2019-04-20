@iati-activity
Feature: Implementer

  Scenario Outline: Implementing organisation
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `participating-org[@role="Implementing" or @role="4"]` should be present
