from flask import Flask, request, jsonify, render_template
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

# System prompt for diet planner
SYSTEM_PROMPT = """You are an expert AI Diet Planner assistant. Your role is to help users create personalized, healthy, and delicious diet plans.

Your responsibilities include:
1. Understanding user's dietary goals (weight loss, muscle gain, general wellness, etc.)
2. Identifying dietary restrictions and preferences (vegetarian, vegan, gluten-free, allergies, etc.)
3. Considering their lifestyle and activity level
4. Providing personalized meal suggestions with nutritional information
5. Creating weekly meal plans with recipes
6. Offering healthy alternatives and tips
7. Tracking progress and adjusting plans as needed

When responding:
- Be empathetic and encouraging
- Provide specific, actionable meal recommendations
- Include macronutrient breakdowns when relevant
- Ask clarifying questions if needed
- Suggest balanced meals with proteins, carbs, and healthy fats
- Consider cultural preferences and local food availability

Always prioritize health and safety in your recommendations."""

# Store conversation history
conversation_history = []

@app.route('/')
def index():
    """Render the chatbot UI"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat requests"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Add user message to history
        conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Create API request with full conversation history
        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT}
            ] + conversation_history,
            temperature=0.7,
            top_p=0.9,
            max_tokens=1024,
            stream=False
        )
        
        # Extract assistant response
        assistant_message = completion.choices[0].message.content
        
        # Add assistant message to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return jsonify({
            'success': True,
            'message': assistant_message,
            'conversation_length': len(conversation_history)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reset', methods=['POST'])
def reset():
    """Reset conversation history"""
    global conversation_history
    conversation_history = []
    return jsonify({'success': True, 'message': 'Conversation reset'})

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    return jsonify({'history': conversation_history})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
