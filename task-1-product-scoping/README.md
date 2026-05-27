# Performance Assistant Tool

## Objective

This project is part of the Data & AI Product Engineer assessment.

The goal of this task is to scope an internal marketing performance tool that helps marketing teams quickly understand how campaigns are performing across multiple channels without manually collecting data from different platforms.

The focus of this submission is product thinking, scope definition, usability, and system design rather than building a fully functional application.

---

# Problem Statement

Marketing analysts currently spend significant time manually checking multiple tools such as:
- Google Ads
- Meta Ads
- CRM platforms
- Analytics dashboards

to answer common business questions like:

> “How is our marketing performing right now, and where should we focus?”

This process is:
- time-consuming
- inconsistent
- dependent on specific team members
- difficult to scale

The proposed solution aims to centralize performance visibility and reduce repetitive reporting effort.

---

# Proposed Solution

The proposed v1 solution is an internal dashboard that:
- aggregates marketing performance data from multiple channels
- provides unified KPI visibility
- highlights channel performance comparisons
- surfaces simple actionable insights
- reduces manual reporting effort

The tool is intentionally scoped to remain simple, useful, and easy to adopt within existing workflows.

---
# Out of Scope

The following features were intentionally excluded from the first version of the product:

- AI-generated campaign recommendations
- Predictive analytics and forecasting
- Automated budget optimization
- Real-time streaming analytics
- Client-facing dashboard portal
- Multi-language support
- Advanced attribution modeling
- Chatbot or conversational assistant
- Custom dashboard builder
- Automated campaign execution

These features were excluded to keep the initial version focused, maintainable, and easier to adopt.

The primary goal of v1 is to reduce manual reporting effort and improve visibility across marketing channels before introducing advanced automation or intelligence layers.

Adding too many features in the first release could increase:
- engineering complexity
- maintenance overhead
- implementation time
- onboarding difficulty

The proposed v1 focuses on solving the core operational problem first while leaving room for future expansion.
 
---

# Primary Users

## Internal Marketing Analysts
Primary daily users responsible for:
- reporting
- campaign monitoring
- performance analysis

## Account Managers
Users who communicate campaign performance updates to clients and stakeholders.

---

# Repository Structure

```txt
task-1-product-scoping/
│
├── productbrief.md
├── scope-definition.md
├── product-decisions.md
├── walkthrough.md
│
├── wireframes/
│   ├── dashboard-wireframe.png
│   ├── campaign-detail-wireframe.png
│   └── export-report-wireframe.png
│
└── flow-diagrams/
    ├── system-flow.png
    └── user-flow.png
