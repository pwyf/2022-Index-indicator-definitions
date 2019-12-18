@iati-activity
Feature: Budget

  Scenario Outline: Budget available forward annually
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2 or 3
     And `default-aid-type/@code` is not G01
     And `activity-date[@type="3" or @type="4" or @type="end-planned" or @type="end-actual"]/@iso-date` is at least 6 months ahead
     Then `budget | planned-disbursement` should be available forward annually

  Scenario Outline: Budget available forward quarterly
    Given an IATI activity
     And the activity is current
     And `activity-status/@code` is one of 2 or 3
     And `default-aid-type/@code` is not G01
     And `activity-date[@type="3" or @type="4" or @type="end-planned" or @type="end-actual"]/@iso-date` is at least 6 months ahead
     Then `budget | planned-disbursement` should be available forward quarterly
