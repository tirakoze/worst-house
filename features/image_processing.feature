Feature: Document image processing
  Scenario: User uploads a valid image
    Given I am authenticated on the platform
    When I upload a JPG image to the S3 bucket
    Then Step Functions should trigger within 5 seconds
    And Textract should return extracted text

  Scenario: Image is moved to Glacier after 90 days
    Given an image has been in S3 for 90 days
    When the lifecycle rule runs
    Then the image should be moved to Glacier storage
