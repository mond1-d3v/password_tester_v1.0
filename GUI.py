import tkinter as tk
from tkinter import ttk, messagebox
from password_tests import PasswordAnalyzer
from translations import TRANSLATIONS, FLAGS

class PasswordTester:
    def __init__(self, root):
        self.root = root
        self.analyzer = PasswordAnalyzer()
        self.current_language = 'en'
        self.setup_window()
        self.setup_styles()
        self.create_widgets()
        
    def get_text(self, key):
        """Get translated text for current language"""
        return TRANSLATIONS.get(self.current_language, {}).get(key, key)
        
    def change_language(self, lang):
        """Change the interface language"""
        self.current_language = lang
        self.analyzer.set_language(lang)
        self.update_interface_language()
        if self.password_var.get():
            self.analyze_password(self.password_var.get())
        
    def setup_window(self):
        self.root.title("CyberSec Password Strength Analyzer")
        self.root.configure(bg="#0f0f0f")
        self.root.state('zoomed')
        self.root.bind('<Escape>', self.toggle_fullscreen)
        
    def setup_styles(self):
        """Configure modern ttk styles"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Modern.Horizontal.TProgressbar",
                            background='#00ff88',
                            troughcolor='#2d2d2d',
                            borderwidth=0,
                            lightcolor='#00ff88',
                            darkcolor='#00ff88')
        
    def toggle_fullscreen(self, event=None):
        """Allow user to exit fullscreen with Escape key"""
        current_state = self.root.state()
        if current_state == 'zoomed':
            self.root.state('normal')
            self.root.geometry("1200x800")
            self.root.update_idletasks()
            x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
            y = (self.root.winfo_screenheight() // 2) - (800 // 2)
            self.root.geometry(f"1200x800+{x}+{y}")
        else:
            self.root.state('zoomed')
        
    def create_widgets(self):
        main_container = tk.Frame(self.root, bg="#0f0f0f")
        main_container.pack(fill="both", expand=True)
        header_frame = tk.Frame(main_container, bg="#1a1a1a", height=180)
        header_frame.pack(fill="x", padx=0, pady=0)
        header_frame.pack_propagate(False)
        header_content = tk.Frame(header_frame, bg="#1a1a1a")
        header_content.pack(expand=True, fill="both", padx=40, pady=30)
        title_section = tk.Frame(header_content, bg="#1a1a1a")
        title_section.pack(side="left", fill="both", expand=True)
        logo_label = tk.Label(title_section, text="🛡️", font=("Segoe UI Emoji", 28), 
                             fg="#00ff88", bg="#1a1a1a")
        logo_label.pack(side="left", padx=(0, 15), pady=(20, 0), anchor="n")
        title_frame = tk.Frame(title_section, bg="#1a1a1a")
        title_frame.pack(side="left", fill="both", expand=True, pady=(15, 0))
        self.title_label = tk.Label(title_frame, text=self.get_text('title'), 
                              font=("Segoe UI", 22, "bold"), fg="#ffffff", bg="#1a1a1a")
        self.title_label.pack(anchor="w", pady=(0, 5))
        self.subtitle_label = tk.Label(title_frame, text=self.get_text('subtitle'), 
                                 font=("Segoe UI", 11), fg="#00ff88", bg="#1a1a1a",
                                 wraplength=500, justify="left")
        self.subtitle_label.pack(anchor="w", pady=(0, 10))
        right_section = tk.Frame(header_content, bg="#1a1a1a")
        right_section.pack(side="right", fill="y", pady=(15, 0))
        lang_frame = tk.Frame(right_section, bg="#1a1a1a")
        lang_frame.pack(anchor="n")
        tk.Label(lang_frame, text="Language:", font=("Segoe UI", 9), 
                fg="#888888", bg="#1a1a1a").pack(pady=(0, 5))
        lang_buttons_frame = tk.Frame(lang_frame, bg="#1a1a1a")
        lang_buttons_frame.pack()
        for lang, flag in FLAGS.items():
            btn = tk.Button(lang_buttons_frame, text=flag, font=("Segoe UI Emoji", 14),
                           bg="#2d2d2d" if lang == self.current_language else "#1a1a1a",
                           fg="#ffffff", relief="flat", bd=0, cursor="hand2",
                           command=lambda l=lang: self.change_language(l), width=3, height=1)
            btn.pack(side="left", padx=1)
            setattr(self, f"lang_btn_{lang}", btn)
        status_frame = tk.Frame(right_section, bg="#1a1a1a")
        status_frame.pack(anchor="n", pady=(15, 0))
        status_content = tk.Frame(status_frame, bg="#1a1a1a")
        status_content.pack()
        status_indicator = tk.Frame(status_content, bg="#00ff88", width=8, height=8)
        status_indicator.pack(side="left", padx=(0, 6), pady=5)
        self.status_label = tk.Label(status_content, text=self.get_text('system_active'), 
                               font=("Segoe UI", 9, "bold"), fg="#00ff88", bg="#1a1a1a")
        self.status_label.pack(side="left", pady=5)
        content_frame = tk.Frame(main_container, bg="#0f0f0f")
        content_frame.pack(fill="both", expand=True, padx=40, pady=30)
        left_panel = tk.Frame(content_frame, bg="#0f0f0f")
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 20))
        right_panel = tk.Frame(content_frame, bg="#0f0f0f", width=400)
        right_panel.pack(side="right", fill="y", padx=(20, 0))
        right_panel.pack_propagate(False)
        self.create_input_section(left_panel)
        self.create_results_section(left_panel)
        self.create_metrics_panel(right_panel)
        
    def create_input_section(self, parent):
        input_card = tk.Frame(parent, bg="#1a1a1a", relief="flat", bd=0)
        input_card.pack(fill="x", pady=(0, 30))
        card_header = tk.Frame(input_card, bg="#1a1a1a", height=60)
        card_header.pack(fill="x", padx=30, pady=(30, 0))
        card_header.pack_propagate(False)
        tk.Label(card_header, text="🔐", font=("Segoe UI Emoji", 24), 
                fg="#00ff88", bg="#1a1a1a").pack(side="left", pady=15)
        header_text = tk.Frame(card_header, bg="#1a1a1a")
        header_text.pack(side="left", fill="y", padx=(15, 0))
        self.input_title_label = tk.Label(header_text, text=self.get_text('password_analysis'), 
                font=("Segoe UI", 18, "bold"), fg="#ffffff", bg="#1a1a1a")
        self.input_title_label.pack(anchor="w", pady=(8, 0))
        self.input_desc_label = tk.Label(header_text, text=self.get_text('password_analysis_desc'), 
                font=("Segoe UI", 11), fg="#888888", bg="#1a1a1a")
        self.input_desc_label.pack(anchor="w")
        input_section = tk.Frame(input_card, bg="#1a1a1a")
        input_section.pack(fill="x", padx=30, pady=(20, 30))
        self.password_label = tk.Label(input_section, text=self.get_text('password_label'), 
                font=("Segoe UI", 10, "bold"), fg="#888888", bg="#1a1a1a")
        self.password_label.pack(anchor="w", pady=(0, 8))
        input_frame = tk.Frame(input_section, bg="#2d2d2d", relief="flat", bd=1)
        input_frame.pack(fill="x", ipady=12)
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(input_frame, textvariable=self.password_var,
                                      font=("Segoe UI", 14), show="*", relief="flat", bd=0,
                                      bg="#2d2d2d", fg="#ffffff", insertbackground="#00ff88")
        self.password_entry.pack(fill="x", padx=15)
        self.password_entry.bind("<KeyRelease>", self.on_password_change)
        controls_frame = tk.Frame(input_section, bg="#1a1a1a")
        controls_frame.pack(fill="x", pady=(15, 0))
        self.show_password = tk.BooleanVar()
        show_frame = tk.Frame(controls_frame, bg="#1a1a1a")
        show_frame.pack(side="left")
        show_btn = tk.Checkbutton(show_frame, text="", variable=self.show_password,
                                 command=self.toggle_password_visibility,
                                 bg="#1a1a1a", activebackground="#1a1a1a", 
                                 selectcolor="#00ff88", fg="#00ff88", relief="flat", bd=0)
        show_btn.pack(side="left")
        self.show_password_label = tk.Label(show_frame, text=self.get_text('show_password'), 
                font=("Segoe UI", 10), fg="#888888", bg="#1a1a1a")
        self.show_password_label.pack(side="left", padx=(5, 0))
        self.clear_btn = tk.Button(controls_frame, text=self.get_text('clear'), 
                             font=("Segoe UI", 10, "bold"), fg="#888888", bg="#1a1a1a",
                             relief="flat", bd=0, cursor="hand2",
                             command=self.clear_password)
        self.clear_btn.pack(side="right")

    def create_results_section(self, parent):
        results_card = tk.Frame(parent, bg="#1a1a1a", relief="flat", bd=0)
        results_card.pack(fill="both", expand=True)
        card_header = tk.Frame(results_card, bg="#1a1a1a", height=60)
        card_header.pack(fill="x", padx=30, pady=(30, 0))
        card_header.pack_propagate(False)
        tk.Label(card_header, text="📊", font=("Segoe UI Emoji", 24), 
                fg="#00ff88", bg="#1a1a1a").pack(side="left", pady=15)
        header_text = tk.Frame(card_header, bg="#1a1a1a")
        header_text.pack(side="left", fill="y", padx=(15, 0))
        self.results_title_label = tk.Label(header_text, text=self.get_text('security_analysis'), 
                font=("Segoe UI", 18, "bold"), fg="#ffffff", bg="#1a1a1a")
        self.results_title_label.pack(anchor="w", pady=(8, 0))
        self.results_desc_label = tk.Label(header_text, text=self.get_text('security_analysis_desc'), 
                font=("Segoe UI", 11), fg="#888888", bg="#1a1a1a")
        self.results_desc_label.pack(anchor="w")
        score_section = tk.Frame(results_card, bg="#1a1a1a")
        score_section.pack(fill="x", padx=30, pady=(20, 0))
        self.score_label = tk.Label(score_section, text="0", 
                                   font=("Segoe UI", 48, "bold"), fg="#ffffff", bg="#1a1a1a")
        self.score_label.pack(side="left")
        score_text = tk.Frame(score_section, bg="#1a1a1a")
        score_text.pack(side="left", fill="y", padx=(15, 0))
        tk.Label(score_text, text="/100", 
                font=("Segoe UI", 24), fg="#888888", bg="#1a1a1a").pack(anchor="w", pady=(8, 0))
        self.strength_label = tk.Label(score_text, text="", 
                                      font=("Segoe UI", 12, "bold"), bg="#1a1a1a")
        self.strength_label.pack(anchor="w")
        progress_section = tk.Frame(results_card, bg="#1a1a1a")
        progress_section.pack(fill="x", padx=30, pady=(20, 30))
        self.progress = ttk.Progressbar(progress_section, length=500, mode='determinate',
                                       style="Modern.Horizontal.TProgressbar")
        self.progress.pack(fill="x")
        results_section = tk.Frame(results_card, bg="#1a1a1a")
        results_section.pack(fill="both", expand=True, padx=30, pady=(0, 30))
        scrollbar_frame = tk.Frame(results_section, bg="#2d2d2d", width=8)
        scrollbar_frame.pack(side="right", fill="y", padx=(10, 0))
        self.results_text = tk.Text(results_section, font=("Consolas", 12),
                                   bg="#1a1a1a", fg="#ffffff", relief="flat", bd=0,
                                   wrap="word", selectbackground="#00ff88",
                                   insertbackground="#00ff88")
        self.results_text.pack(side="left", fill="both", expand=True)
        
    def create_metrics_panel(self, parent):
        metrics_card = tk.Frame(parent, bg="#1a1a1a", relief="flat", bd=0)
        metrics_card.pack(fill="both", expand=True)
        card_header = tk.Frame(metrics_card, bg="#1a1a1a", height=60)
        card_header.pack(fill="x", padx=20, pady=(30, 0))
        card_header.pack_propagate(False)
        tk.Label(card_header, text="⚡", font=("Segoe UI Emoji", 20), 
                fg="#00ff88", bg="#1a1a1a").pack(pady=15)
        self.metrics_title_label = tk.Label(card_header, text=self.get_text('security_metrics'), 
                font=("Segoe UI", 16, "bold"), fg="#ffffff", bg="#1a1a1a")
        self.metrics_title_label.pack(pady=(0, 5))
        self.metrics_frame = tk.Frame(metrics_card, bg="#1a1a1a")
        self.metrics_frame.pack(fill="both", expand=True, padx=20, pady=20)
        self.create_metric_item(self.get_text('length'), "0", self.get_text('chars'), "#888888")
        self.create_metric_item(self.get_text('entropy'), "0.0", self.get_text('bits'), "#888888")
        self.create_metric_item(self.get_text('character_types'), "0", "/4", "#888888")
        self.create_metric_item(self.get_text('security_level'), self.get_text('none'), "", "#888888")
        
    def create_metric_item(self, label, value, unit, color):
        metric_frame = tk.Frame(self.metrics_frame, bg="#0f0f0f", relief="flat", bd=0)
        metric_frame.pack(fill="x", pady=(0, 15), ipady=15)
        tk.Label(metric_frame, text=label, 
                font=("Segoe UI", 10), fg="#888888", bg="#0f0f0f").pack(anchor="w", padx=15, pady=(10, 0))
        value_frame = tk.Frame(metric_frame, bg="#0f0f0f")
        value_frame.pack(anchor="w", padx=15, pady=(5, 10))
        value_label = tk.Label(value_frame, text=value, 
                              font=("Segoe UI", 18, "bold"), fg=color, bg="#0f0f0f")
        value_label.pack(side="left")
        if unit:
            tk.Label(value_frame, text=f" {unit}", 
                    font=("Segoe UI", 12), fg="#666666", bg="#0f0f0f").pack(side="left", pady=(3, 0))
    
    def update_interface_language(self):
        """Update all interface elements with new language"""
        self.title_label.config(text=self.get_text('title'))
        self.subtitle_label.config(text=self.get_text('subtitle'))
        self.status_label.config(text=self.get_text('system_active'))
        self.input_title_label.config(text=self.get_text('password_analysis'))
        self.input_desc_label.config(text=self.get_text('password_analysis_desc'))
        self.password_label.config(text=self.get_text('password_label'))
        self.show_password_label.config(text=self.get_text('show_password'))
        self.clear_btn.config(text=self.get_text('clear'))
        self.results_title_label.config(text=self.get_text('security_analysis'))
        self.results_desc_label.config(text=self.get_text('security_analysis_desc'))
        self.metrics_title_label.config(text=self.get_text('security_metrics'))
        for lang in FLAGS.keys():
            btn = getattr(self, f"lang_btn_{lang}")
            btn.config(bg="#2d2d2d" if lang == self.current_language else "#1a1a1a")
        self.update_metrics_panel(None)
    
    def clear_password(self):
        self.password_var.set("")
        self.clear_results()

    def toggle_password_visibility(self):
        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")
            
    def on_password_change(self, event=None):
        password = self.password_var.get()
        if password:
            self.analyze_password(password)
        else:
            self.clear_results()
            
    def clear_results(self):
        self.score_label.config(text="0", fg="#ffffff")
        self.strength_label.config(text="", fg="#ffffff")
        self.progress['value'] = 0
        self.results_text.delete(1.0, tk.END)
        self.update_metrics_panel(None)
        
    def analyze_password(self, password):
        if not password:
            return 
        analysis = self.analyzer.perform_security_tests(password)
        self.display_results(analysis)
        self.update_metrics_panel(analysis)
        
    def update_metrics_panel(self, analysis):
        for widget in self.metrics_frame.winfo_children():
            widget.destroy()
        if analysis:
            password = analysis['password']
            tests = analysis['tests']
            length = len(password)
            length_color = "#00ff88" if length >= 12 else "#ffaa00" if length >= 8 else "#ff4444"
            self.create_metric_item(self.get_text('length'), str(length), self.get_text('chars'), length_color)
            entropy = float(tests['entropy']['message'].split(':')[1].split()[0]) if 'bits' in tests['entropy']['message'] else 0
            entropy_color = "#00ff88" if entropy >= 70 else "#ffaa00" if entropy >= 50 else "#ff4444"
            self.create_metric_item(self.get_text('entropy'), f"{entropy:.1f}", self.get_text('bits'), entropy_color)
            char_types = 4 if tests['character_variety']['score'] == 25 else 3 if tests['character_variety']['score'] >= 18 else 2 if tests['character_variety']['score'] >= 10 else 1
            char_color = "#00ff88" if char_types == 4 else "#ffaa00" if char_types >= 3 else "#ff4444"
            self.create_metric_item(self.get_text('character_types'), str(char_types), "/4", char_color)
            level, color = self.analyzer.get_security_level(analysis['total_score'])
            level_text = self.get_text(level.lower().replace(' ', '_'))
            self.create_metric_item(self.get_text('security_level'), level_text, "", color)
        else:
            self.create_metric_item(self.get_text('length'), "0", self.get_text('chars'), "#888888")
            self.create_metric_item(self.get_text('entropy'), "0.0", self.get_text('bits'), "#888888")
            self.create_metric_item(self.get_text('character_types'), "0", "/4", "#888888")
            self.create_metric_item(self.get_text('security_level'), self.get_text('none'), "", "#888888")
        
    def display_results(self, analysis):
        score = analysis['total_score']
        self.score_label.config(text=str(score))
        self.progress['value'] = score
        strength, color = self.analyzer.get_security_level(score)
        strength_text = self.get_text(strength.lower().replace(' ', '_'))
        score_color = color
        self.strength_label.config(text=strength_text, fg=color)
        self.score_label.config(fg=score_color)
        self.results_text.delete(1.0, tk.END)
        result_text = f"╭─ SECURITY ASSESSMENT REPORT ─────────────────────────╮\n"
        result_text += f"│                                                      │\n"
        result_text += f"│  Password Length: {len(analysis['password']):>2} characters                        │\n"
        result_text += f"│  Overall Score:   {score:>3}/100 ({strength_text})              │\n"
        result_text += f"│                                                      │\n"
        result_text += f"╰──────────────────────────────────────────────────────╯\n\n"
        result_text += f"🔍 DETAILED ANALYSIS\n"
        result_text += "─" * 50 + "\n\n"
        for test_name, result in analysis['tests'].items():
            test_display = self.get_text(test_name)
            status_icon = "✅" if result['status'] in ['PASS', 'EXCELLENT', 'GOOD'] else "⚠️" if result['status'] in ['WEAK', 'WARN', 'FAIR'] else "❌" 
            result_text += f"{status_icon} {test_display}\n"
            result_text += f"   Status: {result['status']} | Score: {result['score']}/20\n"
            result_text += f"   {result['message']}\n\n"
        result_text += f"💡 {self.get_text('recommendations')}\n"
        result_text += "─" * 50 + "\n"
        for rec in analysis['recommendations']:
            result_text += f"{rec}\n"
        self.results_text.insert(1.0, result_text)

def main():
    root = tk.Tk()
    app = PasswordTester(root)
    root.mainloop()

if __name__ == "__main__":
    main()
