# Webhook Setup Guide — Base Ecosystem Forwarder Bot

## Overview
This guide explains how to set up secure webhook endpoints for real-time forwarding of posts from X, Farcaster, and Calaxy.

## Steps

### 1. Provision Server
- Use a public HTTPS endpoint
- Recommended: Node.js or Python server

### 2. Configure Webhooks

#### X (Twitter/X)
- Use X API to register webhook URL
- Subscribe to account events

#### Farcaster
- Subscribe to casts/events via Farcaster API
- Validate signatures

#### Calaxy
- Subscribe to creator post events
- Use official Base ecosystem integration

### 3. Security
- Validate incoming requests using HMAC or API token
- Reject duplicate or unauthorized events
- Rate-limit incoming requests if needed

### 4. Test Forwarding
- Send test posts
- Verify latency (<2s detection, <5s forwarding)
- Confirm logging and analytics

## Notes
- Integrates with Unified Social Stream (feature32.md)
- Supports real-time, multi-platform forwarding
- Critical for subscription-based Web3 SaaS
