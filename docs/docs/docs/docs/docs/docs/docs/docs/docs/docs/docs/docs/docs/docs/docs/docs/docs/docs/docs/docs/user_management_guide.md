# User Management Guide — Tweet Forwarder Bot

## Overview
This guide explains how the User Management System tracks trial users, paid subscribers, and subscription renewals.

## Tracked Data
- Telegram User ID
- Trial start date
- Trial expiry date (7 days)
- Subscription status (Active / Expired)
- Payment token used (Base, USDC, TON, USDT)
- Subscription expiry date

## Trial Flow
1. User interacts with bot for the first time
2. 7-day free trial starts automatically
3. User receives reminder 1 day before trial ends
4. If no payment is received, access is restricted

## Subscription Flow
1. User sends $10 equivalent in supported token
2. Payment is verified (on-chain or admin confirmation)
3. Subscription is activated for 30 days
4. Renewal required after expiry

## Admin Controls
- View active trial users
- View active paid users
- Manually activate/deactivate accounts
- Monitor subscription expiry

## Notes
- Integrates with feature23 (Free Trial + Subscription System)
- Works with Analytics Dashboard (feature27.md)
- Essential for scalable crypto SaaS model
