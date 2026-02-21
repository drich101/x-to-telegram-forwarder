# Subscription Validation Guide — Base Ecosystem Forwarder Bot

## Overview
This guide explains how the subscription validation middleware works to enforce trial and paid subscriptions.

## Subscription Types
- **Trial Users:** 7-day free access
- **Paid Users:** $10/month, payable via Base, USDC, TON, or USDT

## Validation Flow
1. User interacts with bot or receives forwarded post
2. Middleware checks User Management System (feature28.md)
3. If trial or subscription active → allow forwarding
4. If expired → send reminder or block forwarding
5. Log access attempt for analytics

## Admin Notes
- View all active trial users
- View paid subscribers
- Manually activate or deactivate users
- Monitor expiry dates and payments

## Security Considerations
- Validate token/payment authenticity
- Prevent bypass of subscription checks
- Ensure logs are tamper-proof

## Notes
- Works with Unified Social Stream (feature32.md)
- Integrates with Analytics Dashboard (feature27.md)
- Critical for scalable subscription-based Web3 SaaS
