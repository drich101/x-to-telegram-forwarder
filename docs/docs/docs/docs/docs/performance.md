# Performance — Tweet Forwarder Bot

## Overview
This document explains best practices to maintain high performance and low latency in forwarding tweets.

## Optimizations
- Use WebSocket or streaming API for near real-time updates
- Limit unnecessary API calls and data processing
- Efficient multi-account handling

## Metrics
- Target forwarding speed: 2–5 seconds after tweet posted
- Monitor logs to detect bottlenecks (feature3.md)

## Notes
- Designed for high-traffic Telegram channels
- Ensures reliability for Web3/Base communities
