# 🌈 LumiiShift

An AI-powered mood tracking application built with Streamlit that provides empathetic responses to your emotions.

## ✨ Features

- **100+ Mood Options**: Comprehensive mood mapping with color-coded responses
- **AI-Powered Responses**: Empathetic AI responses using Together.ai's Mistral model
- **Interactive UI**: Beautiful, responsive interface with animated mood buttons
- **Color Psychology**: Each mood has an associated color for visual emotional representation
- **Special Effects**: Balloons and snow effects for certain moods

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Together.ai API key ([Get one here](https://together.ai))

### Installation

1. **Clone or download the project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key** (choose one method):
   
   **Option A: Environment file (recommended)**
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```
   
   **Option B: Enter manually**
   - The app will prompt you for your API key when you run it

4. **Run the application**:
   ```bash
   streamlit run lumiishift_app.py
   ```

## 🛠️ Development with Kiro

This project is optimized for development with Kiro IDE. Available features:

### Kiro Hooks
- **Test LumiiShift App**: Quickly start the development server
- **Code Quality Check**: Automated code quality and formatting checks

### Steering Rules
- Follows PEP 8 coding standards
- Implements security best practices
- Focuses on accessibility and performance

## 📁 Project Structure

```
├── lumiishift_app.py      # Main application (improved version)
├── Scripts/lumii.py       # Original application
├── mood_data.py           # Mood mapping data
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── .kiro/               # Kiro IDE configuration
    ├── steering/        # Development guidelines
    └── hooks/           # Automated workflows
```

## 🎨 Mood Categories

The app includes diverse mood categories:
- **Basic emotions**: happy, sad, angry, calm
- **Complex feelings**: nostalgic, conflicted, hopeful
- **Energy states**: energetic, tired, restless
- **Social emotions**: lonely, romantic, shy
- **And many more!**

## 🔧 Configuration

### Environment Variables

Create a `.env` file with:
```
TOGETHER_API_KEY=your_together_ai_api_key_here
```

### Customization

- **Mood Data**: Edit `mood_data.py` to add/modify moods
- **Styling**: Modify CSS in `lumiishift_app.py`
- **AI Behavior**: Adjust system prompts in the `get_lumiishift_response` function

## 🤝 Contributing

1. Follow the coding standards in `.kiro/steering/`
2. Test your changes thoroughly
3. Ensure accessibility compliance
4. Add appropriate error handling

## 📝 License

This project is open source. Feel free to use and modify as needed.

## 🆘 Troubleshooting

**API Key Issues**:
- Ensure your Together.ai API key is valid
- Check your account has sufficient credits

**Installation Problems**:
- Make sure you're using Python 3.8+
- Try creating a virtual environment

**Performance Issues**:
- Check your internet connection
- Consider caching API responses for development

---

Built with ❤️ using Streamlit and Together.ai
