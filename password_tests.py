import re
import math

class PasswordAnalyzer:
    """Class containing all password testing and analysis methods"""
    
    def __init__(self):
        self.dictionary_words = {
            'en': ['password', 'admin', 'user', 'login', 'welcome', 'hello', 'computer', 'security', 'system', 'server', 'network', 'internet', 'manager', 'service', 'access', 'account', 'database', 'windows', 'microsoft', 'google', 'facebook', 'twitter', 'linkedin', 'instagram', 'youtube', 'amazon', 'apple', 'samsung', 'netflix', 'spotify'],
            'fr': ['motdepasse', 'administrateur', 'utilisateur', 'connexion', 'bienvenue', 'bonjour', 'ordinateur', 'sécurité', 'système', 'serveur', 'réseau', 'internet', 'gestionnaire', 'service', 'accès', 'compte', 'france', 'paris', 'lyon', 'marseille', 'toulouse', 'nice', 'nantes', 'bordeaux', 'lille', 'rennes'],
            'es': ['contraseña', 'administrador', 'usuario', 'iniciosesion', 'bienvenido', 'hola', 'computadora', 'seguridad', 'sistema', 'servidor', 'red', 'internet', 'gerente', 'servicio', 'acceso', 'cuenta', 'españa', 'madrid', 'barcelona', 'valencia', 'sevilla', 'zaragoza', 'málaga', 'murcia', 'palmas', 'bilbao'],
            'it': ['password', 'amministratore', 'utente', 'accesso', 'benvenuto', 'ciao', 'computer', 'sicurezza', 'sistema', 'server', 'rete', 'internet', 'manager', 'servizio', 'accesso', 'account', 'italia', 'roma', 'milano', 'napoli', 'torino', 'palermo', 'genova', 'bologna', 'firenze', 'bari'],
            'de': ['passwort', 'administrator', 'benutzer', 'anmeldung', 'willkommen', 'hallo', 'computer', 'sicherheit', 'system', 'server', 'netzwerk', 'internet', 'manager', 'service', 'zugang', 'konto', 'deutschland', 'berlin', 'hamburg', 'münchen', 'köln', 'frankfurt', 'stuttgart', 'düsseldorf', 'dortmund', 'essen'],
            'ru': ['пароль', 'администратор', 'пользователь', 'вход', 'добропожаловать', 'привет', 'компьютер', 'безопасность', 'система', 'сервер', 'сеть', 'интернет', 'менеджер', 'сервис', 'доступ', 'аккаунт', 'россия', 'москва', 'петербург', 'новосибирск', 'екатеринбург', 'казань', 'челябинск', 'омск', 'самара', 'ростов']
        }
        self.current_language = 'en'
    
    def set_language(self, language):
        """Set the primary language for testing"""
        self.current_language = language
    
    def detect_language(self, password):
        """Detect the language of words in the password"""
        lower_pass = password.lower()
        detected_languages = []
        for lang, words in self.dictionary_words.items():
            if lang == self.current_language:
                continue
            for word in words:
                if word in lower_pass:
                    detected_languages.append(lang)
                    break
        return detected_languages
    
    def perform_security_tests(self, password):
        """Perform all security tests on the password"""
        tests = {
            'length': self.test_length(password),
            'character_variety': self.test_character_variety(password),
            'common_patterns': self.test_common_patterns(password),
            'dictionary_words': self.test_dictionary_words(password),
            'repetition': self.test_repetition(password),
            'entropy': self.calculate_entropy(password),
            'keyboard_patterns': self.test_keyboard_patterns(password),
            'personal_info': self.test_personal_info_patterns(password)
        }
        total_score = sum(test['score'] for test in tests.values())
        return {
            'password': password,
            'total_score': min(100, total_score),
            'tests': tests,
            'recommendations': self.generate_recommendations(tests)
        }
        
    def test_length(self, password):
        """Test password length"""
        length = len(password)
        if length < 8:
            return {'score': 0, 'status': 'FAIL', 'message': f'Too short ({length} chars). Minimum 8 required.'}
        elif length < 12:
            return {'score': 10, 'status': 'WEAK', 'message': f'Acceptable length ({length} chars). 12+ recommended.'}
        elif length < 16:
            return {'score': 15, 'status': 'GOOD', 'message': f'Good length ({length} chars).'}
        else:
            return {'score': 20, 'status': 'EXCELLENT', 'message': f'Excellent length ({length} chars).'}
            
    def test_character_variety(self, password):
        """Test character variety in password"""
        score = 0
        has_lower = bool(re.search(r'[a-z]', password))
        has_upper = bool(re.search(r'[A-Z]', password))
        has_digits = bool(re.search(r'[0-9]', password))
        has_symbols = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        variety_count = sum([has_lower, has_upper, has_digits, has_symbols])
        if variety_count == 4:
            score = 25
            status = 'EXCELLENT'
            message = 'Uses all character types (lowercase, uppercase, digits, symbols).'
        elif variety_count == 3:
            score = 18
            status = 'GOOD'
            message = 'Uses 3 character types. Add symbols for better security.'
        elif variety_count == 2:
            score = 10
            status = 'WEAK'
            message = 'Uses only 2 character types. Add more variety.'
        else:
            score = 0
            status = 'FAIL'
            message = 'Uses only 1 character type. Very weak.'
        return {'score': score, 'status': status, 'message': message}
        
    def test_common_patterns(self, password):
        """Test for common password patterns"""
        common_patterns = [
            r'123456', r'password', r'qwerty', r'abc123', r'admin',
            r'letmein', r'welcome', r'monkey', r'dragon', r'master',
            r'iloveyou', r'princess', r'football', r'baseball', r'sunshine',
            r'passw0rd', r'12345678', r'superman', r'trustno1', r'starwars'
        ]
        for pattern in common_patterns:
            if re.search(pattern, password.lower()):
                return {'score': 0, 'status': 'FAIL', 'message': f'Contains common pattern: {pattern}'}   
        return {'score': 15, 'status': 'PASS', 'message': 'No common patterns detected.'}
        
    def test_dictionary_words(self, password):
        """Test for dictionary words with multilingual support"""
        lower_pass = password.lower()
        primary_words = self.dictionary_words.get(self.current_language, [])
        for word in primary_words:
            if word in lower_pass:
                return {'score': 0, 'status': 'FAIL', 'message': f'Contains dictionary word: {word}'}
        detected_languages = self.detect_language(password)
        if detected_languages:
            for lang in detected_languages:
                words = self.dictionary_words.get(lang, [])
                for word in words:
                    if word in lower_pass:
                        lang_names = {'en': 'English', 'fr': 'French', 'es': 'Spanish', 'it': 'Italian', 'de': 'German', 'ru': 'Russian'}
                        lang_name = lang_names.get(lang, lang)
                        return {'score': 0, 'status': 'FAIL', 'message': f'Contains {lang_name} dictionary word: {word}'}
        return {'score': 10, 'status': 'PASS', 'message': 'No common dictionary words found.'}
        
    def test_repetition(self, password):
        """Test for character repetition"""
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                return {'score': 0, 'status': 'FAIL', 'message': f'Contains repeated characters: {password[i]*3}'}
        if len(password) >= 6:
            for length in range(2, len(password) // 2 + 1):
                for start in range(len(password) - 2 * length + 1):
                    pattern = password[start:start + length]
                    if password[start + length:start + 2 * length] == pattern:
                        return {'score': 2, 'status': 'WEAK', 'message': f'Contains repeated pattern: {pattern}'}  
        return {'score': 10, 'status': 'PASS', 'message': 'No excessive character repetition.'}
        
    def calculate_entropy(self, password):
        """Calculate password entropy"""
        charset_size = 0
        if re.search(r'[a-z]', password):
            charset_size += 26
        if re.search(r'[A-Z]', password):
            charset_size += 26
        if re.search(r'[0-9]', password):
            charset_size += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            charset_size += 32
        if charset_size == 0:
            return {'score': 0, 'status': 'FAIL', 'message': 'Cannot calculate entropy.'}
        entropy = len(password) * math.log2(charset_size)
        if entropy < 30:
            return {'score': 0, 'status': 'WEAK', 'message': f'Low entropy: {entropy:.1f} bits'}
        elif entropy < 50:
            return {'score': 8, 'status': 'FAIR', 'message': f'Fair entropy: {entropy:.1f} bits'}
        elif entropy < 70:
            return {'score': 12, 'status': 'GOOD', 'message': f'Good entropy: {entropy:.1f} bits'}
        else:
            return {'score': 15, 'status': 'EXCELLENT', 'message': f'Excellent entropy: {entropy:.1f} bits'}
            
    def test_keyboard_patterns(self, password):
        """Test for keyboard patterns"""
        keyboard_patterns = [
            'qwerty', 'qwertyuiop', 'asdf', 'asdfghjkl', 'zxcv', 'zxcvbnm',
            '1234', '12345678', 'qaz', 'wsx', 'edc', 'rfv', 'tgb', 'yhn',
            'qwe', 'asd', 'zxc', 'poi', 'lkj', 'mnb'
        ]
        lower_pass = password.lower()
        for pattern in keyboard_patterns:
            if pattern in lower_pass or pattern[::-1] in lower_pass:
                return {'score': 0, 'status': 'FAIL', 'message': f'Contains keyboard pattern: {pattern}'}     
        return {'score': 5, 'status': 'PASS', 'message': 'No keyboard patterns detected.'}

    def test_personal_info_patterns(self, password):
        """Test for personal information patterns"""
        if re.search(r'19\d{2}|20\d{2}', password):
            return {'score': 0, 'status': 'WARN', 'message': 'May contain birth year or date.'}
        if re.search(r'(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)', password.lower()):
            return {'score': 2, 'status': 'WARN', 'message': 'May contain month name.'}
        common_names = ['john', 'mike', 'david', 'chris', 'alex', 'sarah', 'emma', 'lisa']
        for name in common_names:
            if name in password.lower():
                return {'score': 1, 'status': 'WARN', 'message': f'May contain common name: {name}'}
        if re.search(r'0123|1234|2345|3456|4567|5678|6789', password):
            return {'score': 0, 'status': 'FAIL', 'message': 'Contains sequential numbers.'}
        return {'score': 5, 'status': 'PASS', 'message': 'No obvious personal information detected.'}
        
    def generate_recommendations(self, tests):
        """Generate security recommendations based on test results"""
        recommendations = []
        messages = {
            'en': {
                'length': "• Increase password length to at least 12 characters",
                'variety': "• Use a mix of uppercase, lowercase, numbers, and symbols",
                'patterns': "• Avoid common patterns and dictionary words",
                'entropy': "• Increase randomness and unpredictability",
                'keyboard': "• Avoid keyboard patterns like 'qwerty' or '123456'",
                'repetition': "• Avoid repeating characters or patterns",
                'personal': "• Avoid personal information like birth years or names",
                'good1': "• Your password meets security standards",
                'good2': "• Consider using a password manager for unique passwords",
                'good3': "• Change passwords regularly for sensitive accounts"
            },
            'fr': {
                'length': "• Augmentez la longueur du mot de passe à au moins 12 caractères",
                'variety': "• Utilisez un mélange de majuscules, minuscules, chiffres et symboles",
                'patterns': "• Évitez les motifs communs et les mots du dictionnaire",
                'entropy': "• Augmentez le caractère aléatoire et l'imprévisibilité",
                'keyboard': "• Évitez les motifs de clavier comme 'qwerty' ou '123456'",
                'repetition': "• Évitez la répétition de caractères ou de motifs",
                'personal': "• Évitez les informations personnelles comme les années de naissance",
                'good1': "• Votre mot de passe respecte les normes de sécurité",
                'good2': "• Envisagez d'utiliser un gestionnaire de mots de passe",
                'good3': "• Changez régulièrement les mots de passe des comptes sensibles"
            },
            'es': {
                'length': "• Aumente la longitud de la contraseña a al menos 12 caracteres",
                'variety': "• Use una mezcla de mayúsculas, minúsculas, números y símbolos",
                'patterns': "• Evite patrones comunes y palabras del diccionario",
                'entropy': "• Aumente la aleatoriedad e impredecibilidad",
                'keyboard': "• Evite patrones de teclado como 'qwerty' o '123456'",
                'repetition': "• Evite repetir caracteres o patrones",
                'personal': "• Evite información personal como años de nacimiento",
                'good1': "• Su contraseña cumple con los estándares de seguridad",
                'good2': "• Considere usar un administrador de contraseñas",
                'good3': "• Cambie las contraseñas regularmente para cuentas sensibles"
            },
            'it': {
                'length': "• Aumentare la lunghezza della password ad almeno 12 caratteri",
                'variety': "• Usare un mix di maiuscole, minuscole, numeri e simboli",
                'patterns': "• Evitare pattern comuni e parole del dizionario",
                'entropy': "• Aumentare casualità e imprevedibilità",
                'keyboard': "• Evitare pattern di tastiera come 'qwerty' o '123456'",
                'repetition': "• Evitare ripetizioni di caratteri o pattern",
                'personal': "• Evitare informazioni personali come anni di nascita",
                'good1': "• La tua password soddisfa gli standard di sicurezza",
                'good2': "• Considera l'uso di un gestore di password",
                'good3': "• Cambia regolarmente le password per account sensibili"
            },
            'de': {
                'length': "• Erhöhen Sie die Passwortlänge auf mindestens 12 Zeichen",
                'variety': "• Verwenden Sie eine Mischung aus Groß-, Kleinbuchstaben, Zahlen und Symbolen",
                'patterns': "• Vermeiden Sie häufige Muster und Wörterbuch-Wörter",
                'entropy': "• Erhöhen Sie Zufälligkeit und Unvorhersagbarkeit",
                'keyboard': "• Vermeiden Sie Tastaturmuster wie 'qwerty' oder '123456'",
                'repetition': "• Vermeiden Sie wiederholende Zeichen oder Muster",
                'personal': "• Vermeiden Sie persönliche Informationen wie Geburtsjahre",
                'good1': "• Ihr Passwort erfüllt die Sicherheitsstandards",
                'good2': "• Erwägen Sie die Verwendung eines Passwort-Managers",
                'good3': "• Ändern Sie Passwörter regelmäßig für sensible Konten"
            },
            'ru': {
                'length': "• Увеличьте длину пароля до минимум 12 символов",
                'variety': "• Используйте смесь заглавных, строчных букв, цифр и символов",
                'patterns': "• Избегайте общих шаблонов и словарных слов",
                'entropy': "• Увеличьте случайность и непредсказуемость",
                'keyboard': "• Избегайте клавиатурных шаблонов как 'qwerty' или '123456'",
                'repetition': "• Избегайте повторения символов или шаблонов",
                'personal': "• Избегайте личной информации как годы рождения",
                'good1': "• Ваш пароль соответствует стандартам безопасности",
                'good2': "• Рассмотрите использование менеджера паролей",
                'good3': "• Регулярно меняйте пароли для важных аккаунтов"
            }
        }
        lang_messages = messages.get(self.current_language, messages['en'])
        if tests['length']['score'] < 15:
            recommendations.append(lang_messages['length'])
        if tests['character_variety']['score'] < 20:
            recommendations.append(lang_messages['variety'])
        if tests['common_patterns']['score'] == 0:
            recommendations.append(lang_messages['patterns'])           
        if tests['entropy']['score'] < 10:
            recommendations.append(lang_messages['entropy'])            
        if tests['keyboard_patterns']['score'] == 0:
            recommendations.append(lang_messages['keyboard'])            
        if tests['repetition']['score'] < 5:
            recommendations.append(lang_messages['repetition'])            
        if tests['personal_info']['score'] < 3:
            recommendations.append(lang_messages['personal'])           
        if not recommendations:
            recommendations.append(lang_messages['good1'])
            recommendations.append(lang_messages['good2'])
            recommendations.append(lang_messages['good3'])
        return recommendations
        
    def get_security_level(self, score):
        """Get security level based on score"""
        if score >= 85:
            return "VERY STRONG", "#00ff88"
        elif score >= 70:
            return "STRONG", "#88ff44"
        elif score >= 50:
            return "MODERATE", "#ffaa00"
        elif score >= 30:
            return "WEAK", "#ff8800"
        else:
            return "VERY WEAK", "#ff4444"
