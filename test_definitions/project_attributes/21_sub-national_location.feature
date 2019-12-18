@iati-activity
Feature: Sub-national location

  Scenario Outline: Location (sub-national)
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `recipient-region/@code` is not 998
     And `default-aid-type/@code` is not G01
     And `default-aid-type/@code` is not B01
     And `default-aid-type/@code` is not B02
     And `transaction/aid-type/@code` is not B01
     And `transaction/aid-type/@code` is not B02
     Then `location` should be present

  Scenario Outline: Location (sub-national) coordinates or point
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2, 3 or 4
     And `recipient-region/@code` is not 998
     And `default-aid-type/@code` is not G01
     And `default-aid-type/@code` is not B01
     And `default-aid-type/@code` is not B02
     And `transaction/aid-type/@code` is not B01
     And `transaction/aid-type/@code` is not B02
     Then `location[coordinates or point]` should be present
