@iati-activity
Feature: Sector

  Scenario Outline: Sector is present
    Given an IATI activity
     And the activity is current
     Then `sector | transaction/sector` should be present

  Scenario Outline: Sector uses DAC CRS 5 digit purpose codes
    Given an IATI activity
     And the activity is current
     Then every `sector[not(@vocabulary) or @vocabulary="1"]/@code | transaction/sector[@vocabulary="1" or not(@vocabulary)]/@code` should be on the Sector codelist
