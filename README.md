# AWS Generative AI with Amazon Bedrock

This repository contains Jupyter notebooks demonstrating Amazon Bedrock capabilities, developed while completing the Coursera course ["Generative AI Applications with Amazon Bedrock"](https://www.coursera.org/learn/generative-ai-applications-amazon-bedrock).

## Overview

These notebooks explore various aspects of generative AI using AWS Bedrock, covering foundation models, prompt engineering, safety measures, and production implementation patterns. Each notebook includes detailed explanations and best practices learned during the course.

## Repository Structure

```
aws-gen-ai/
├── bedrock-text-updated.ipynb           # Basic text generation with foundation models
├── bedrock-streaming-updated.ipynb      # Real-time streaming responses
├── bedrock-guardrails-updated.ipynb     # AI safety and content filtering
├── bedrock-prompt-management-2.ipynb    # Centralized prompt management
├── bedrock-video-updated.ipynb          # Video generation with Nova Reel
└── README.md                           # This file
```

## Notebooks Overview

### Text Generation (`bedrock-text-updated.ipynb`)
Demonstrates basic text generation using Amazon Bedrock's invoke_model API. Covers model invocation, inference parameters, response handling, and cost optimization strategies.

### Streaming Responses (`bedrock-streaming-updated.ipynb`)
Implements real-time text generation using streaming APIs. Shows how to process event streams, handle progressive rendering, and build responsive applications with lower perceived latency.

### Guardrails (`bedrock-guardrails-updated.ipynb`)
Explores responsible AI implementation through content filtering and safety measures. Covers content policies, PII protection, prompt injection prevention, contextual grounding, and programmatic guardrail creation.

### Prompt Management (`bedrock-prompt-management-2.ipynb`)
Demonstrates centralized prompt template management and versioning. Includes template variables, version control, prompt optimization, A/B testing, and enterprise governance patterns.

### Video Generation (`bedrock-video-updated.ipynb`)
Shows video creation from text descriptions using Amazon Nova Reel. Covers asynchronous processing, S3 integration, job management, and prompt engineering for video generation.

## Technical Implementation

### Key Technologies Used
- Amazon Bedrock: Fully managed foundation model service
- Amazon Nova: AWS foundation model family (Micro and Reel)
- AWS SDK (Boto3): Python SDK for AWS services
- Jupyter Notebooks: Interactive development environment
- Amazon S3: Object storage for generated content

### Architecture Patterns Demonstrated
1. Synchronous Generation: Direct model invocation for immediate responses
2. Asynchronous Processing: Long-running tasks with job management
3. Streaming Architecture: Real-time response processing
4. Template Management: Centralized prompt governance
5. Safety Integration: Content filtering and compliance

## Setup Requirements

### Prerequisites
- AWS Account with Amazon Bedrock permissions
- Python 3.8+ with Jupyter notebook support
- AWS CLI configured with credentials
- Required packages: `boto3`, `jupyter`, `ipython`

### AWS Permissions Required
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:CreatePrompt",
                "bedrock:GetPrompt",
                "bedrock:UpdatePrompt",
                "bedrock:DeletePrompt",
                "bedrock:ListPrompts",
                "bedrock:CreatePromptVersion",
                "bedrock:ApplyGuardrail",
                "bedrock:StartAsyncInvoke",
                "bedrock:GetAsyncInvoke",
                "bedrock-agent:OptimizePrompt",
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "*"
        }
    ]
}
```

## Key Learnings

### Foundation Models
- Understanding different model capabilities and use cases
- Implementing basic and advanced text generation patterns
- Optimizing inference parameters for specific requirements

### Streaming Implementation
- Building responsive applications with real-time AI responses
- Handling event streams and progressive content rendering
- Managing connection issues and error handling

### Safety and Governance
- Implementing responsible AI practices with guardrails
- Content filtering for enterprise applications
- PII protection and compliance requirements

### Prompt Engineering
- Creating and managing reusable prompt templates
- Version control and optimization strategies
- Enterprise governance and collaboration patterns

### Multimodal Capabilities
- Text-to-video generation with Nova Reel
- Asynchronous job management for long-running tasks
- Integration with AWS storage services

## Production Considerations

### Cost Management
- Model selection based on use case requirements
- Token usage monitoring and optimization
- Resource cleanup strategies

### Security Best Practices
- IAM permissions with least-privilege access
- Content filtering implementation
- Sensitive information handling
- Audit logging and monitoring

### Performance Optimization
- Appropriate API selection (streaming vs batch)
- Error handling and retry strategies
- Resource utilization optimization

## Additional Resources

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [AWS Generative AI Learning Path](https://aws.amazon.com/training/learn-about/machine-learning/)
- [AWS Samples Repository](https://github.com/aws-samples/amazon-bedrock-samples)

## Note

This repository represents practical learning outcomes from the AWS Coursera course on generative AI applications. The implementations follow AWS best practices and include detailed explanations for educational reference.



create s3 bucket com o dataset