# Flask Diet Planner Chatbot

A simple Flask web application that uses the Groq API to create an intelligent diet planning chatbot.

## Features

- **Real-time Chat Interface**: Interactive chat UI with message history
- **AI-Powered Diet Planning**: Leverages Groq API for intelligent nutritional advice
- **Conversation History**: Maintains context across multiple messages
- **System Prompt Integration**: Pre-configured as a diet planner expert
- **Responsive Design**: Works on desktop and mobile devices
- **Reset Functionality**: Clear conversation and start fresh

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r flask_requirements.txt
```

### 2. Configure Environment Variables

Create or update your `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

## Project Structure

```
GenAI-Diet-Planner/
├── app.py                    # Flask application main file
├── templates/
│   └── index.html           # Chat UI template
├── flask_requirements.txt    # Python dependencies
└── .env                      # Environment variables (not in repo)
```

## API Endpoints

### POST `/api/chat`
Send a message to the diet planner chatbot.

**Request:**
```json
{
  "message": "I want to lose weight, what should I eat?"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Here's a personalized diet plan for weight loss...",
  "conversation_length": 2
}
```

### POST `/api/reset`
Reset the conversation history.

**Response:**
```json
{
  "success": true,
  "message": "Conversation reset"
}
```

### GET `/api/history`
Get the entire conversation history.

**Response:**
```json
{
  "history": [
    {
      "role": "user",
      "content": "What's a healthy breakfast?"
    },
    {
      "role": "assistant",
      "content": "A healthy breakfast should include..."
    }
  ]
}
```

## Usage

1. Open `http://localhost:5000` in your browser
2. Type your diet-related questions or requests
3. Press Enter or click Send
4. The chatbot will respond with personalized advice
5. Click Reset to start a new conversation

## System Prompt

The chatbot is configured with a specialized system prompt that makes it an expert diet planner. It can:

- Understand dietary goals (weight loss, muscle gain, wellness)
- Identify dietary restrictions and preferences
- Consider lifestyle and activity levels
- Provide personalized meal suggestions
- Create weekly meal plans
- Offer nutritional information

## Technology Stack

- **Backend**: Python Flask
- **API**: Groq API for LLM completions
- **Frontend**: HTML5 + CSS3 + Vanilla JavaScript
- **Model**: Mixtral-8x7b or OpenAI GPT-OSS-120b

## Example Conversations

**User**: "I'm vegetarian and want to lose 5 kg in 2 months"
**Bot**: [Provides personalized vegetarian meal plan with caloric targets]

**User**: "What are good protein sources for vegans?"
**Bot**: [Lists vegan protein options with nutritional info]

**User**: "Create a weekly meal plan for me"
**Bot**: [Generates detailed 7-day meal plan]

## Troubleshooting

**Issue**: API Key not found
**Solution**: Ensure `.env` file exists with valid `GROQ_API_KEY`

**Issue**: Flask not starting
**Solution**: Install all dependencies: `pip install -r flask_requirements.txt`

**Issue**: Chat not responding
**Solution**: Check API key validity and Groq API service status

## Future Enhancements

- User authentication and persistent profiles
- Save favorite meal plans
- Integration with nutrition APIs
- Mobile app version
- Voice input/output
- Multi-language support

---

Happy dieting! 🥗
