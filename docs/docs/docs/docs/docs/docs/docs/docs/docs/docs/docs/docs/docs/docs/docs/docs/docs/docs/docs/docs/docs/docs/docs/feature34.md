# Feature 34 — Subscription Validation Middleware

## Description
This middleware checks whether a user or Telegram channel is eligible to receive forwarded posts based on subscription status.

## Features
- Verify trial period (7-day free trial)
- Check active paid subscription ($10/month)
- Block forwarding for expired subscriptions
- Log invalid attempts for auditing
- Integrates with payment system (Base, USDC, TON, USDT)

## Flow
1. User interacts with bot
2. Middleware checks subscription database
3. If active → forward post
4. If inactive → send reminder or block forwarding

## Notes
- Works with User Management System (feature28.md)
- Ensures premium users only get full access
- Supports scalable subscription-based SaaS
