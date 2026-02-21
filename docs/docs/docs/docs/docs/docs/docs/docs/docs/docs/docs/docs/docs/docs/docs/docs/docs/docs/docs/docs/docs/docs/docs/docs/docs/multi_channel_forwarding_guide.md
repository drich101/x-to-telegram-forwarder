# Multi-Channel Forwarding Guide — Base Ecosystem Forwarder Bot

## Overview
This guide explains how the bot forwards posts to multiple Telegram channels while enforcing subscription rules.

## Flow
1. Unified Social Stream receives post from X, Farcaster, or Calaxy
2. Middleware checks channel/user subscription status
3. If active → forward post
4. If inactive → block forwarding or send reminder
5. Log all forwarding events for analytics

## Features
- Multi-channel delivery
- Subscription enforcement per channel/user
- Retry logic for failed deliveries
- Priority-based forwarding
- Analytics integration (feature27.md)

## Admin Notes
- View eligible channels for forwarding
- Track delivery logs
- Monitor retry events
- Ensure all subscribers are up-to-date

## Security Considerations
- Prevent unauthorized access
- Avoid duplicate forwarding
- Ensure logs are tamper-proof
