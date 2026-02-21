# Configuration Guide — Tweet Forwarder Bot

## Environment Variables (.env)

| Variable                  | Description                                      | Example                          |
|----------------------------|-------------------------------------------------|----------------------------------|
| TELEGRAM_BOT_TOKEN         | Telegram bot token for bot authentication      | your_telegram_bot_token_here     |
| TWITTER_BEARER_TOKEN       | X (Twitter) API Bearer Token                    | your_bearer_token_here           |
| CHAT_ID                     | Telegram chat ID to forward tweets             | your_telegram_chat_id_here       |
| WEB3_RPC_URL               | RPC endpoint for Base/Web3 integration         | https://your-base-node-url       |
| CONTRACT_ADDRESS           | Smart contract address (for future Web3 use)   | 0xYourContractAddress            |

## Notes

- Never commit your real `.env` file. Use `.env.example` as placeholder.  
-
