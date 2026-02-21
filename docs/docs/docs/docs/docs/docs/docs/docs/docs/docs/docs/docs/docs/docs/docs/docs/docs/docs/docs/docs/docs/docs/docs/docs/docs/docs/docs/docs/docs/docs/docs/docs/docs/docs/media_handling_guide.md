# Media Handling Guide — Base Ecosystem Forwarder Bot

## Overview
This guide explains how the bot handles images, videos, GIFs, and attachments from X, Farcaster, and Calaxy to ensure correct delivery.

## Features
- **Media Detection:** Identify images, videos, and attachments in posts
- **Processing:** Convert, resize, or compress media if required
- **Forwarding:** Attach media properly to Telegram messages
- **Error Handling:** Retry failed media forwards (feature37.md)
- **Logging:** Record media delivery events for analytics

## Admin Notes
- Monitor logs for failed media deliveries
- Configure conversion/resizing settings if necessary
- Works with Unified Social Stream (feature43.md) and Multi-Channel Forwarding (feature35.md)

## Notes
- Critical for professional multi-platform content forwarding
- Ensures minimal delay while preserving media quality
