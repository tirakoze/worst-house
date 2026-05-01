# Time Log

## Epic: Migrate legacy 3-tier to 4-tier AWS serverless architecture

### Feature: VPC Infrastructure
| Story | Task | Estimated | Actual |
|-------|------|-----------|--------|
| Deploy VPC with public/private subnets | Add VPC to template.yaml | 30m | 45m |
| Configure NAT Gateway | Add NAT Gateway and route tables | 30m | 30m |

### Feature: Edge and routing (Tier 1)
| Story | Task | Estimated | Actual |
|-------|------|-----------|--------|
| Host static site on S3 | Add S3 bucket with website config | 30m | 45m |
| Distribute via CloudFront | Add CloudFront distribution | 30m | 30m |

### Feature: Sync API (Tier 2)
| Story | Task | Estimated | Actual |
|-------|------|-----------|--------|
| Route traffic via ALB | Add ALB and target group | 45m | 1.5h |
| Auto scale EC2 on high CPU | Add Auto Scaling Group | 30m | 45m |

### Feature: Async orchestration (Tier 3)
| Story | Task | Estimated | Actual |
|-------|------|-----------|--------|
| Trigger workflow on image upload | Add S3 event notification | 30m | 30m |
| Orchestrate Lambdas via Step Functions | Add state machine definition | 1h | 1.5h |
| Extract text with Textract | Write Lambda: app.py | 45m | 1h |
| Fetch image from S3 | Write Lambda: fetch_image.py | 30m | 30m |
| Save results to database | Write Lambda: save_results.py | 30m | 30m |

### Feature: Persistence (Tier 4)
| Story | Task | Estimated | Actual |
|-------|------|-----------|--------|
| Store images in S3 | Add images bucket | 15m | 15m |
| Store metadata in Aurora | Add Aurora cluster | 45m | 1h |
| Archive old images to Glacier | Add S3 lifecycle rule | 20m | 20m |

### Feature: Well-Architected review and TCO
| Story | Task | Estimated | Actual |
|-------|------|-----------|--------|
| Write 6-pillar review | Add to README.md | 1h | 1h |
| Build TCO report | AWS Pricing Calculator | 45m | 1h |
| Document Trusted Advisor | Add to README.md | 30m | 30m |

## Total
| | Estimated | Actual |
|-|-----------|--------|
| Total hours | 10h | 13h |
