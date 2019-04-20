@iati-activity
Feature: Reviews and evaluations

  Scenario Outline: Project performance and evaluation document
    Given an IATI activity
     And the activity is current
     And `default-aid-type/@code` is not G01
     And either `document-link/category[@code="A07"]` is present, or `activity-status/@code` is one of 3 or 4
     Then `document-link/category[@code="A07"]` should be present
