Feature: Tier 4 - Persistence layer
  Scenario: Extracted text is saved to Aurora
    Given the SaveResults Lambda receives extracted text
    When it writes to the Aurora MySQL database
    Then the record should be queryable from the metadata table

  Scenario: Images are moved to Glacier after 90 days
    Given an image has been in S3 standard storage for 90 days
    When the S3 lifecycle rule evaluates the object
    Then the image should be transitioned to S3 Glacier storage
