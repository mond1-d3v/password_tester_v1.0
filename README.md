# 🛡️ Password Analyzer

## ✨ Features

### 🔒 **Advanced Security Analysis**
- **Length Analysis**: Evaluates password length with industry-standard recommendations
- **Character Variety**: Checks for uppercase, lowercase, numbers, and special characters
- **Pattern Detection**: Identifies common patterns and keyboard sequences
- **Dictionary Attack Protection**: Detects common words in multiple languages
- **Entropy Calculation**: Measures password randomness and unpredictability
- **Personal Information Detection**: Warns about birth years, names, and dates

### 🌍 **Multilingual Support**
- **6 Languages Supported**: English 🇬🇧, French 🇫🇷, Spanish 🇪🇸, Italian 🇮🇹, German 🇩🇪, Russian 🇷🇺
- **Real-time Translation**: Interface adapts instantly to selected language
- **Multilingual Dictionary**: Detects weak passwords in all supported languages
- **Flag-based Language Selection**: Intuitive country flags for language switching

### 🎨 **Modern Interface**
- **Dark Theme**: Professional cybersecurity-focused design
- **Real-time Analysis**: Instant feedback as you type
- **Progress Visualization**: Color-coded strength indicators
- **Detailed Reports**: Comprehensive security assessment with recommendations
- **Fullscreen Mode**: Immersive analysis experience (Press Escape to toggle)

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- tkinter (usually included with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mond1-d3v/password_tester_v1.0
   cd password_tester_v1.0
   ```

2. **Run the application**
   ```bash
   python GUI.py
   ```

### Alternative Installation
Download the latest release from the [Releases](https://github.com/username/password-analyzer/releases) page.

## 📁 Project Structure

```
password-analyzer/
├── GUI.py                 # Main application interface
├── password_tests.py      # Password analysis logic  
├── translations.py        # Multilingual support
└── README.md              # Project documentation
```

## 🔧 Usage

1. **Launch the Application**
   ```bash
   python GUI.py
   ```

2. **Select Your Language**
   - Click on any flag icon (🇬🇧🇫🇷🇪🇸🇮🇹🇩🇪🇷🇺) in the top-right corner
   - Interface will instantly adapt to your chosen language

3. **Analyze Your Password**
   - Type your password in the input field
   - View real-time analysis results
   - Check security metrics on the right panel
   - Review detailed recommendations

4. **Interpret Results**
   - **Score**: 0-100 overall security rating
   - **Color Codes**: 
     - 🔴 Red: Very Weak/Weak (0-49)
     - 🟡 Yellow: Moderate (50-69)
     - 🟢 Green: Strong/Very Strong (70-100)

## 🛠️ Technical Details

### Security Tests Performed

| Test | Description | Max Score |
|------|-------------|-----------|
| **Length** | Password length evaluation | 20 points |
| **Character Variety** | Mix of character types | 25 points |
| **Common Patterns** | Detection of weak patterns | 15 points |
| **Dictionary Words** | Multilingual dictionary check | 10 points |
| **Repetition** | Character/pattern repetition | 10 points |
| **Entropy** | Randomness calculation | 15 points |
| **Keyboard Patterns** | Sequential key detection | 5 points |
| **Personal Info** | Birth years, names, dates | 5 points |

### Language Support

| Language | Code | Dictionary Words | Flag | Status |
|----------|------|------------------|------|--------|
| English | `en` | 30+ words | 🇬🇧 | ✅ Complete |
| French | `fr` | 26+ words | 🇫🇷 | ✅ Complete |
| Spanish | `es` | 26+ words | 🇪🇸 | ✅ Complete |
| Italian | `it` | 26+ words | 🇮🇹 | ✅ Complete |
| German | `de` | 26+ words | 🇩🇪 | ✅ Complete |
| Russian | `ru` | 26+ words | 🇷🇺 | ✅ Complete |

## 🎯 Key Features

### Real-time Analysis
- Instant feedback as you type
- No need to click "analyze" buttons
- Live security metrics updates

### Multilingual Detection
- Detects weak passwords in any supported language
- Warns if using words from different languages
- Prioritizes selected interface language

### Professional Interface
- Modern dark theme design
- Cybersecurity-focused aesthetics
- Intuitive user experience
- Professional reporting format

## 🔐 Security Recommendations

The tool provides intelligent recommendations based on analysis:

- **Length**: Suggests minimum 12 characters
- **Complexity**: Recommends character variety
- **Uniqueness**: Warns against common patterns
- **Randomness**: Suggests increasing entropy
- **Personal Info**: Advises avoiding personal data
