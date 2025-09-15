# LumiiShift Development Guidelines

## Project Overview
LumiiShift is a Streamlit-based mood tracking application that uses AI to provide empathetic responses to user emotions. The app features 100+ different moods with color-coded responses and integrates with Together.ai's API.

## Code Standards
- Use clear, descriptive variable names
- Add comments for complex logic
- Follow PEP 8 for Python code formatting
- Keep functions focused and single-purpose
- Handle API errors gracefully with user-friendly messages

## Development Workflow
- Test API integrations thoroughly
- Validate UI responsiveness across different screen sizes
- Ensure accessibility compliance for color choices
- Test with various mood combinations

## Security Best Practices
- Never commit API keys to version control
- Use environment variables for sensitive data
- Validate all user inputs
- Implement proper error handling for API calls

## Performance Considerations
- Cache API responses when appropriate
- Optimize image loading and display
- Minimize unnecessary re-renders in Streamlit
- Consider rate limiting for API calls
