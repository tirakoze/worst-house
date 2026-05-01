# Worst House in the Best Neighborhood

## Architecture Overview
A 4-tier AWS serverless application built with AWS SAM.

- Tier 1: S3 static website + CloudFront
- Tier 2: ALB + VPC + public/private subnets + NAT Gateway
- Tier 3: Lambda + Step Functions + Amazon Textract
- Tier 4: Aurora MySQL + S3 images bucket + Glacier lifecycle

## Well-Architected Review

### Operational Excellence
All infrastructure is defined as code in template.yaml using AWS SAM. Deployments are automated via sam build and sam deploy. GitHub commits are linked to issue numbers for full traceability.

### Security
All compute and database resources are in private subnets with no public internet exposure. A NAT Gateway allows outbound-only internet access. Security Groups restrict traffic to specific ports and sources only. IAM roles follow least-privilege principles with specific actions and resources.

### Reliability
The Application Load Balancer distributes traffic across multiple availability zones. Auto Scaling responds to CPU load to prevent 504 timeouts. Aurora MySQL provides managed database reliability with automated backups.

### Performance Efficiency
CloudFront delivers static assets from edge locations near users. Lambda functions scale automatically with zero idle cost. Aurora MySQL handles structured metadata queries efficiently.

### Cost Optimization
Lambda charges only per invocation with no idle cost. S3 Glacier lifecycle rules move images to cheap storage after 90 days. Aurora Serverless v2 scales down during low traffic periods.

### Sustainability
Right-sized resources prevent over-provisioning. Serverless architecture means compute runs only when needed, reducing energy waste compared to always-on servers.

## Data Retention Policy
- Images uploaded to S3 are retained for 90 days in standard storage
- After 90 days images are automatically moved to S3 Glacier
- After 7 years (2555 days) images are permanently deleted
- Aurora database metadata is retained indefinitely unless manually purged

## Deployment Instructions
```bash
sam build && sam deploy
```

## Teardown Instructions
```bash
sam delete --stack-name worst-house
```

## Trusted Advisor Findings
AWS Academy lab accounts have limited Trusted Advisor access and do not provide full check results. The following security best practices were manually verified instead:

- Security Groups: Only ports 80 and 443 are open to the public
- S3 Buckets: Only the frontend bucket is public, images bucket is private
- IAM: All roles use least-privilege policies with no wildcard resources
- MFA: Enabled on the root account
- Cost: No unused Elastic IPs or idle load balancers detected
