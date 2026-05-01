Feature: Tier 3 - Orchestration layer
  Scenario: Image upload triggers Step Functions
    Given an image is uploaded to the S3 images bucket
    When the S3 event notification fires
    Then the Step Functions state machine should start execution

  Scenario: Textract extracts text from image
    Given the Step Functions state machine is running
    When the ExtractText Lambda is invoked with a valid image
    Then Amazon Textract should return extracted text blocks
    And the text should be passed to the SaveResults Lambda
