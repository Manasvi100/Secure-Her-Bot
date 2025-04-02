from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Replace with your actual bot token from BotFather
TOKEN = "7900801627:AAFDB-YybXS-DzPxdYhAEzGhA-D1qOxiZtY"

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔹 Register", callback_data="register")],
        [InlineKeyboardButton("🚨 Report Harassment", callback_data="report")],
        [InlineKeyboardButton("📂 My Reports", callback_data="my_reports")],
        [InlineKeyboardButton("🔒 Store Evidence", callback_data="store_evidence")],
        [InlineKeyboardButton("🆘 Community Help", callback_data="community_help")],
        [InlineKeyboardButton("📍 Location History", callback_data="location_history")],
        [InlineKeyboardButton("🛣️ Safe Route", callback_data="safe_route")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 *Welcome to HerSafe Bot!* \n\n"
        "I'm here to assist you with safety features. Choose an option below:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# Function to handle button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "register": "📌 Send your details using: `/register <name> <phone>`",
        "report": "🚨 Report an incident using: `/report <category> <description> <location>`",
        "my_reports": "📂 Fetching your previous reports...",
        "store_evidence": "🔒 Upload evidence using: `/evidence <file> <password>`",
        "community_help": "🆘 Requesting community assistance...",
        "location_history": "📍 Fetching high-risk locations...",
        "safe_route": "🛣️ Enter your start and destination using: `/safe_route <start> <destination>`"
    }

    # Send the corresponding message for the clicked button
    if query.data in messages:
        await query.message.reply_text(messages[query.data])

# Main function to start the bot
def main():
    app = Application.builder().token(TOKEN).build()
    
    # Add command and callback handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
