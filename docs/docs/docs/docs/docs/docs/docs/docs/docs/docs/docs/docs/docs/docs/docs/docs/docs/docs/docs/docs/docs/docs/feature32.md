# Feature 32 — Unified Social Stream Engine

## Description
The Unified Social Stream Engine aggregates content from multiple platforms 
(X, Farcaster, Calaxy) into a standardized internal format before forwarding.

## Purpose
- Eliminate platform-specific logic in forwarding layer
- Improve scalability
- Enable faster forwarding (2–5 seconds target latency)
- Simplify subscription control and filtering

## Architecture

### Step 1 — Data Collection
- X listener
- Farcaster listener
- Calaxy listener

### Step 2 — Normalization
Each incoming post is converted into a unified structure:

{
  source: "x | farcaster | calaxy",
  author: "username",
  content: "post text",
  timestamp: "utc",
  post_id: "unique_id",
  metadata: {}
}

### Step 3 — Processing Layer
- Deduplication check
- Keyword filtering
- Subscription validation
- Priority tagging

### Step 4 — Forwarding
- Send to Telegram channels
- Log latency
- Store analytics metrics

## Performance Goal
- Detection latency: < 2 seconds
- Forward latency: < 5 seconds
- Zero duplicate posts

## Notes
This feature is the foundation of the entire Base Ecosystem Forwarder SaaS.
