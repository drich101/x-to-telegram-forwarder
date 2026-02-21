# Rate-Limit Guide — Tweet Forwarder Bot

## Overview
Instructions for handling X (Twitter) and Telegram API rate limits to prevent forwarding failures.

## Steps
1. Monitor API usage per account
2. Configure thresholds for automatic retries
3. Delay or queue forwarding when limits are near
4. Test limits with multiple accounts
5. Adjust bot configuration based on API response

## Notes
- Ensures ultra-fast forwarding (2–5 seconds) without violating API limits
- Supports multi-account and multi-channel forwarding
- Complements logging, monitoring, and retry mechanisms
