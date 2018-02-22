Feature: Sector

  Scenario Outline: Sector is present
    Given the activity is current
     Then `sector | transaction/sector` should be present

  Scenario Outline: Sector uses DAC CRS 5 digit purpose codes
    Given the activity is current
     Then every `sector[@vocabulary="DAC" or not(@vocabulary) or @vocabulary="1"]/@code | transaction/sector[@vocabulary="1" or not(@vocabulary)]/@code` should be on the Sector codelist
