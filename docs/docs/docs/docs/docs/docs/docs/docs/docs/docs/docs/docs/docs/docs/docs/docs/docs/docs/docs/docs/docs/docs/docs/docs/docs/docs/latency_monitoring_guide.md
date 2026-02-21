# Latency Monitoring & Logging Guide — Base Ecosystem Forwarder Bot

## Overview
This guide explains how the Latency Monitoring & Logging system tracks detection, processing, and forwarding times for all platforms (X, Farcaster, Calaxy).

## Metrics
- **Detection latency:** Time from post creation to event received
- **Processing latency:** Time to normalize, filter, and prioritize
- **Forwarding latency:** Time to deliver to Telegram channels
- **Retry events:** Number of failed deliveries retried
- **Failed delivery attempts:** Events that could not be delivered

## Admin Dashboard
- Real-time graphs of latency metrics
- Alerts for delays above 5 seconds
- Detailed logs for debugging

## Notes
- Integrates with Unified Social Stream (feature32.md)
- Supports scalable multi-platform forwarding
- Critical for professional-grade SaaS monitoring
