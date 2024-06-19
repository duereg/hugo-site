---
title: RACI Charts
date: 2024-03-05T11:52:59-08:00
description: My lessons learned
draft: true
tags: ["Engineering Management", "Management", "Direct Reports", "1-1", "1:1", "one on one"]
categories: ["management", "direct reports"]
---

Primary Role
Time allocation
32 points

Onboarding
Shadow someone for 1 week, watch and understand what is being done/answered
Then have someone shadow you for 1 week as you answer questions.
Responsibilities
Answer Support/Sales questions
#support-devices
#ask-devices
Be the first responder to incidents
You might need to be the Incident Commander until someone more senior comes.
Weekday daily check at 11am the KPIs (Dashboards below) and investigate if they are lower than expected
Work on Support tickets, respect the SLAs.
Every Support ticket should be closed within a week after your on-call rotation ends
We have a policy of closing tickets if there has been no response from customer/support in 5 days
Attend Support Standup
Be aware of the history of the ongoing tickets
Write the notes for the Monday Handoff meeting.
What are the trends?
What remains to be done?
What’s the volume?
Keep an eye for the alert channels
#device-experience-alerts, #device-foundation-alerts
Most of them are spammy.
Keep an eye for ETAs Utilization (it shouldn’t be 100% for long)
https://app.datadoghq.com/notebook/5792826/device-hardware-etas
https://app.datadoghq.com/monitors/122259726?live=4h
There’s an alert in #device-foundation-alerts that should auto-trigger.

Don’t delete/mute Opsgenie app
Not Responsibilities
Release Manager
Warehouse On-call
That’s the Secondary On-call role
Slack Channels
#support-devices
Usually where support asks questions
#devices-all-teams
Usually where other on-calls from other teams will transfer support tickets/ask questions
#ask-devices
Sometimes people may tag you about features etc. - usually you can defer to Ways Hassas or ask in channel
Any tags from @df-oncall group in slack
Runbooks
Handoff checklist:
https://rippling.atlassian.net/wiki/spaces/HW/pages/3322904948/DF+oncall+handoff+to+do+list

DF On-Call Notes
https://rippling.atlassian.net/wiki/spaces/HW/pages/3443130530/DF+on-call+notes
Dashboards
Pangolin ops dashboard:
https://app.datadoghq.com/dashboard/kwx-msf-g53/terraform-pangolin-overview-dashboard?from_ts=1686850740300&to_ts=1686852540300&live=true

Pangolin service dashboard (device health):
https://app.datadoghq.com/dashboard/chv-3ej-za4/device-management-health-dashboard?from_ts=1686766181885&to_ts=1686852581885&live=true

Tray service dashboard:
https://app.datadoghq.com/dashboard/gm9-xce-vg8/terraform-devices-tray-dashboard?from_ts=1686838258145&to_ts=1686852658145&live=true

Secondary Role
Time allocation
16 points

Onboarding
Shadow someone for 1 week, watch and understand what is being done/answered
Then have someone shadow you for 1 week as you answer questions.
Responsibilities

The warehouse is responsible for assigning devices to the proper end employee for many clients, and they ensure that the agent is running properly. If a warehouse agent encounters an issue during these parts related to the agent, it’s the warehouse on-call person’s responsibility to help troubleshoot and resolve these issues.

The warehouse will tag the on-call person if they have issues. They are responsible for debugging and responding to these issues within a day. Time to respond should be within 2 hours.

Additionally, the warehouse on-call will track and report their issues, as well as bandwidth utilized, in the weekly on-call notes document.
Slack Channels

#rippling-doneboard
#rippling-doneboard-dev

Runbooks
Handoff checklist
https://rippling.atlassian.net/wiki/spaces/HW/pages/3322904948/DF+oncall+handoff+to+do+list#DF-warehouse-oncall
The Monday handoff meeting is for both primary and secondary on-call handoffs.

Responsibilities/Protocols/Debugging
https://rippling.atlassian.net/wiki/spaces/HW/pages/3359310367/Warehouse+On-Call+Handbook

Weekly On-call Summary/Notes
https://rippling.atlassian.net/wiki/spaces/HW/pages/3443001100/Warehouse+Handoff+Notes
Dashboards

Reassign actions
https://app.datadoghq.com/s/l0azadoluvx8wg4d/wuj-pp5-dhb
https://app.datadoghq.com/s/l0azadoluvx8wg4d/wuj-pp5-dhb
https://app.datadoghq.com/s/l0azadoluvx8wg4d/ht5-kg5-dmq
Assign actions
https://app.datadoghq.com/s/l0azadoluvx8wg4d/ecr-t9g-nug
https://app.datadoghq.com/s/l0azadoluvx8wg4d/9dv-fhy-sf8
https://app.datadoghq.com/s/l0azadoluvx8wg4d/9dv-fhy-sf8
Soft wipe actions
https://app.datadoghq.com/s/l0azadoluvx8wg4d/pqu-24e-wn8
https://app.datadoghq.com/s/l0azadoluvx8wg4d/g6h-vzp-fsv
https://app.datadoghq.com/s/l0azadoluvx8wg4d/g6h-vzp-fsv
