---
title: Setting up an on-call roll
date: 2024-06-21T12:25:15-08:00
description: My lessons learned
draft: false
tags: ["Engineering Management", "Management", "Direct Reports", "on-call", "incident management"]
categories: ["management", "direct reports", "incident management"]
---
# Structuring an On-Call Rotation: A Guide for Engineering Managers

On-call rotations are more than “who picks up the phone”—they’re a critical way to balance incident response, customer support, and operational health without burning out your team. Below is a template you can adapt, illustrated with examples from my time leading a device-management on-call rotation at a fast-growing tech company.

---

## 1. Define a Clear Primary On-Call Role

Rather than vague “points,” **be explicit about the time commitment** you expect each engineer to spend on-call:

| Rotation            | Weekly Time Commitment | Focus Areas                                |
|---------------------|------------------------|--------------------------------------------|
| **Primary On-Call** | 20–30 hours per week   | • Incident response & escalation<br>       |
|                     |                        | • Customer/support queue<br>               |
|                     |                        | • Daily system health checks               |

> **Tip:** Survey your team to agree on a realistic hours-per-week target before finalizing the rotation schedule.

---

## 2. Onboarding (2-Week Pairing)

1. **Week 1: Shadow**  
   - New on-call owner watches the current engineer handle live incidents, support tickets, and handoffs.  
2. **Week 2: Reverse Shadow**  
   - New owner takes the lead; outgoing engineer observes and provides real-time feedback.  

This structured pairing ensures tribal knowledge—playbooks, alert-noise patterns, escalation paths—transfers quickly.

---

## 3. Primary On-Call Responsibilities

### 3.1 Incident Response & Command

- **Triage Alerts** in your monitoring system (e.g. Datadog, Prometheus) and designated “alerts” channel.  
- **Act as Incident Commander** until a senior engineer arrives to lead the war room.  

### 3.2 Customer & Sales Support

- **Monitor the support-ticket queue** (Zendesk, Jira Service Desk, Intercom).  
- **Acknowledge** new tickets within your SLA (e.g. within 2 hours).  
- **Resolve or escalate** within a defined window (e.g. 5 days), and close tickets with no customer response after a set period (e.g. 5 days).

### 3.3 Daily System Health Check

- **At a fixed time** each day (e.g. 11 AM), review core dashboards:  
  - Error rates, API latency, backlog metrics  
  - Resource-utilization (CPU, memory, agent heartbeats)  
- **Investigate anomalies** immediately to prevent cascading failures.

### 3.4 Stand-Up & Weekly Handoff

- **Daily stand-up**: report open incidents, ticket trends, and blockers.  
- **Weekly handoff document**: cover  
  - Trend analysis (incidents vs. prior week)  
  - Outstanding action items  
  - Volume metrics (tickets opened vs. closed)

### 3.5 Maintain Runbooks & Playbooks

- **Centralize all instructions** in a wiki or docs repo:  
  - On-call checklist (monitor links, escalation contacts)  
  - Playbooks for common failure scenarios  
  - Postmortem and incident-review templates

---

## 4. Tooling & Communication Best Practices

- **Collaboration Channels**  
  - Separate channels for support, alerts, and feature questions.  
  - Use group pings (e.g. `@oncall-primary`) to reach the right person instantly.

- **Monitoring & Dashboards**  
  - Provide direct links to real-time dashboards and notebooks.  
  - Automate alert thresholds to open or escalate tickets automatically.

- **Ticketing System SLAs**  
  - Enforce and track SLAs with reminders and escalation rules.  
  - Regularly review ticket aging and backlog trends.

---

## 5. Continuous Improvement

- **Load Balancing**  
  - Rotate evenly—aim for a “1 in N” schedule so no one is on-call too frequently.

- **Noise Reduction**  
  - Hold quarterly on-call retrospectives to prune or tune noisy alerts.

- **Automation**  
  - Replace repetitive daily checks with scheduled reports or scripts when possible.

- **Recognition & Feedback**  
  - Credit engineers for on-call improvements in your sprint retros and performance reviews.

---

### In Summary

A well-structured on-call program hinges on **clear time commitments**, **paired onboarding**, **defined responsibilities**, and **robust tooling**. Use these guidelines as a starting point, then iterate based on your product’s unique failure modes and your organization’s culture. By doing so, you’ll foster a resilient support framework that scales with your team—and keeps everyone sane.
