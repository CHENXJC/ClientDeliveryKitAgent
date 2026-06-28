# Workflow Map

## End-To-End Flow

```text
Client Intake
  -> Business Context Extraction
  -> Pain Point Diagnosis
  -> Workflow Bottleneck Mapping
  -> Automation Opportunity Scoring
  -> Useful Signals
  -> Recommended Actions
  -> Delivery Report / Proposal Summary
  -> AgentHubControlCenter Integration
```

## Stage Responsibilities

### Client Intake

Capture basic business context, current workflow tools, constraints, and success definition from synthetic demo input.

### Business Context Extraction

Identify business model, customer types, workflow channels, and operating pattern.

### Pain Point Diagnosis

Map repeated pain points to workflow areas and business impact.

### Workflow Bottleneck Mapping

Show where delays, handoff issues, visibility gaps, or manual review requirements appear.

### Automation Opportunity Scoring

Score each candidate based on impact, repeatability, data availability, effort, risk, and human review need.

### Useful Signals

Convert high-value findings into AgentHub-compatible signal summaries.

### Recommended Actions

Produce clear consultant recommendations such as "start with lead triage summary" or "keep customer-facing send actions manual."

### Delivery Report / Proposal Summary

Build a public-safe Markdown report template that can later export to local files.

### AgentHubControlCenter Integration

Expose manifest, actions, useful signals, connector readiness, and report summary metadata.

## Safety Boundary

Any action that sends, writes, modifies, deletes, or touches real customer workflow data must remain blocked until a future approval design is implemented.
