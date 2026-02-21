# Payment Gateway Guide — Base Ecosystem Forwarder Bot

## Overview
This guide explains how users can pay for subscriptions and how the system validates payments.

## Supported Payment Methods
- Base (native crypto)
- USDC (Ethereum or Base network)
- TON
- USDT (Ethereum or Base network)

## User Payment Flow
1. User selects subscription plan ($10/month)
2. Choose preferred payment method
3. Send payment to the specified address
4. System verifies blockchain confirmation
5. Middleware activates subscription
6. User receives success notification

## Admin Notes
- Monitor incoming payments in real-time
- Validate subscription activation logs
- Handle payment disputes manually if necessary
- Integrates with Analytics Dashboard (feature38.md) for subscription metrics

## Security Considerations
- Verify all blockchain transactions
- Prevent duplicate or fraudulent subscriptions
- Keep payment logs tamper-proof
