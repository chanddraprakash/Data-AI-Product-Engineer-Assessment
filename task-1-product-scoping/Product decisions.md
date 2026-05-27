# Product Decisions

## Why Internal Users First?

The first version of the tool is designed primarily for internal marketing analysts and account managers rather than external clients.

Internal users experience the operational pain most directly because they repeatedly gather data manually from multiple platforms such as Google Ads, Meta Ads, and CRM systems. They spend significant time consolidating reports, validating numbers, and answering recurring performance questions.

By solving the workflow problems of internal users first, the tool can:
- reduce repetitive manual reporting work
- improve consistency in how performance is interpreted
- decrease dependency on specific team members
- speed up client communication

Focusing on internal users also allows faster iteration because feedback can be collected frequently from daily users before exposing the tool to clients.

Client-facing access may be considered in future versions after validating the usefulness and reliability of the internal workflow.

---

## Why Daily Refresh Instead of Real-Time?

The v1 product uses daily data refreshes instead of real-time analytics.

Most marketing performance decisions are not made minute-by-minute. Daily aggregated data is generally sufficient for identifying trends, comparing channel performance, and preparing reports for stakeholders.

Implementing real-time synchronization would introduce:
- higher infrastructure complexity
- API rate-limit concerns
- increased operational costs
- additional monitoring requirements
- more difficult debugging and maintenance

Since the main goal of v1 is to reduce manual reporting effort and improve consistency, daily updates provide a strong balance between usefulness and simplicity.

This decision helps keep the system reliable and easier to maintain during the initial rollout.

---

## Why Dashboard Instead of Chatbot?

The tool is designed as a dashboard rather than a conversational chatbot.

Marketing analysts already work primarily with:
- dashboards
- tables
- charts
- filters
- performance summaries

A dashboard aligns naturally with their existing workflows and reduces the learning curve for adoption.

Dashboards are also more effective for:
- comparing multiple channels side-by-side
- scanning KPIs quickly
- identifying trends visually
- exporting reports efficiently

While conversational interfaces may be useful in future versions, introducing a chatbot in v1 could add unnecessary complexity without significantly improving the core workflow.

The priority for v1 is clarity, speed, and usability rather than advanced interaction models.
