Feature: Tier 1 - Presentation layer
  Scenario: Static website is accessible via CloudFront
    Given the SAM stack is deployed
    When a user visits the CloudFront URL
    Then the S3 static website should load successfully
    And the response code should be 200

  Scenario: S3 bucket is not publicly writable
    Given the frontend S3 bucket exists
    When an unauthorized user attempts to upload a file
    Then the upload should be denied with a 403 error
