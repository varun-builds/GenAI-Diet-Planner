# 🥗 GenAI-Diet-Planner

A modern web application that uses Generative AI to create personalized, intelligent diet recommendations based on user preferences, dietary restrictions, and health goals.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **AI-Powered Recommendations**: Leverages generative AI models to suggest personalized diet plans
- **Personalization**: Customizes recommendations based on:
  - Dietary preferences (vegetarian, vegan, keto, gluten-free, etc.)
  - Health goals (weight loss, muscle gain, general wellness)
  - Caloric requirements
  - Allergies and food restrictions
  - Cuisine preferences
- **Meal Planning**: Generate weekly meal plans with recipes
- **Nutritional Analysis**: View macros and micronutrients for suggested meals
- **Interactive UI**: User-friendly interface for easy navigation
- **Real-time Suggestions**: Get instant diet recommendations
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## 🛠️ Tech Stack

### Frontend
- **React** or **Vue.js** (choose based on your preference)
- **TypeScript** for type safety
- **Tailwind CSS** for styling
- **Axios** for API calls

### Backend
- **Node.js** with **Express** or **Python** with **Flask/FastAPI**
- **RESTful API** for client-server communication
- **JWT** for authentication

### AI/ML
- **OpenAI API**, **Google Generative AI**, or **Anthropic Claude** for AI completions
- **Prompt Engineering** for diet recommendation logic

### Database
- **MongoDB** or **PostgreSQL** for storing user profiles and preferences
- User data persistence and history tracking

### Deployment
- **Docker** for containerization
- **AWS**, **Heroku**, or **Vercel** for hosting

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- API keys for your chosen AI service (OpenAI, Google, Anthropic, etc.)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/GenAI-Diet-Planner.git
   cd GenAI-Diet-Planner
   ```

2. **Install dependencies**
   ```bash
   # Frontend
   cd frontend
   npm install

   # Backend
   cd ../backend
   npm install
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the backend directory:
   ```env
   AI_API_KEY=your_api_key_here
   AI_PROVIDER=openai  # or google, anthropic
   DATABASE_URL=your_database_url
   PORT=5000
   JWT_SECRET=your_secret_key
   ```

4. **Start the application**
   
   ```bash
   # Terminal 1 - Backend
   cd backend
   npm start

   # Terminal 2 - Frontend
   cd frontend
   npm start
   ```

   The app will open at `http://localhost:3000`

## 📖 Usage

1. **Sign Up/Login**: Create an account or log in
2. **Complete Profile**: Enter your dietary preferences, restrictions, and health goals
3. **Get Recommendations**: Click "Generate Diet Plan" to receive AI-powered suggestions
4. **View Details**: Explore nutritional information, recipes, and meal plans
5. **Save Preferences**: Bookmark favorite meal plans for future reference

## 📁 Project Structure

```
GenAI-Diet-Planner/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
│   └── package.json
├── backend/
│   ├── routes/
│   ├── controllers/
│   ├── models/
│   ├── middleware/
│   ├── services/
│   ├── config/
│   └── server.js
├── .gitignore
├── README.md
└── docker-compose.yml
```

## ⚙️ Configuration

### AI Model Configuration

Update the AI provider settings in `backend/config/ai.config.ts`:

```typescript
export const aiConfig = {
  provider: process.env.AI_PROVIDER,
  apiKey: process.env.AI_API_KEY,
  model: 'gpt-4', // or appropriate model for your provider
  temperature: 0.7,
  maxTokens: 2000
};
```

### Database Configuration

Configure your database connection in `backend/config/database.ts`

## 🔌 API Integration

### Endpoints

- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `POST /api/diet/recommendations` - Get diet recommendations
- `GET /api/diet/plans/:id` - Fetch specific meal plan
- `POST /api/user/preferences` - Save user preferences
- `GET /api/user/profile` - Get user profile

### Example Request

```bash
curl -X POST http://localhost:5000/api/diet/recommendations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer your_token" \
  -d '{
    "age": 30,
    "goal": "weight_loss",
    "restrictions": ["gluten-free"],
    "cuisinePreference": ["Indian", "Mediterranean"],
    "caloryTarget": 2000
  }'
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Support

For support, email support@dietplanner.com or open an issue on GitHub.

---

**Happy dieting with AI! 🤖✨**
