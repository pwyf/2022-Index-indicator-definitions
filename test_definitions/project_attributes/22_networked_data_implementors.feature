@iati-activity
Feature: Networked Data - Implementors

  Scenario Outline: Implementing organisation
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     Then `participating-org[@role="Implementing" or @role="4"]/@ref | participating-org[@role="Implementing" or @role="4"]/narrative/text()` should have at least 1 characters
