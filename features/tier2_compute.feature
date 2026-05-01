Feature: Tier 2 - API and compute layer
  Scenario: Load balancer routes traffic to EC2
    Given the Application Load Balancer is deployed
    When a request is sent to the ALB DNS name
    Then the request should be forwarded to the target group
    And the response should not be a 504 Gateway Timeout

  Scenario: Auto Scaling responds to high CPU
    Given the Auto Scaling Group is configured
    When CPU utilization exceeds 70 percent
    Then a new EC2 instance should be launched automatically
