import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import webbrowser

class GraphSoundGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("[ OSCI - TheKarimZZZ ]")
        self.root.geometry("800x800")
        
        self.style = ttk.Style(theme="darkly")
        self.style.configure("TButton", foreground="#00ff00", background="#003300")
        self.style.configure("TLabel", foreground="#00ff00", background="#1a1a1a")
        self.style.configure("TEntry", foreground="#00ff00", background="#003300")
        self.style.configure("TFrame", background="#1a1a1a")
        self.style.configure("TLabelframe", background="#1a1a1a", foreground="#00ff00")
        self.style.configure("TLabelframe.Label", background="#1a1a1a", foreground="#00ff00")
        
        self.functions = []
        
        # Главный контейнер с заполнением всего окна
        main_container = ttk.Frame(root, bootstyle="dark")
        main_container.pack(fill='both', expand=True, padx=0, pady=0)
        
        self.notebook = ttk.Notebook(main_container, bootstyle="dark")
        self.notebook.pack(fill='both', expand=True, padx=15, pady=15)
        
        self.settings_frame = ttk.Frame(self.notebook, bootstyle="dark")
        self.notebook.add(self.settings_frame, text="НАСТРОЙКИ")
        
        self.docs_frame = ttk.Frame(self.notebook, bootstyle="dark")
        self.notebook.add(self.docs_frame, text="ДОКУМЕНТАЦИЯ")
        
        self.setup_settings_tab()
        self.setup_docs_tab()
    
    def open_github(self):
        webbrowser.open("https://github.com/TheKarimZZZ/OSCI")
    
    def setup_docs_tab(self):
        docs_container = ttk.Frame(self.docs_frame, bootstyle="dark")
        docs_container.pack(fill='both', expand=True, padx=0, pady=0)
        
        github_frame = ttk.Frame(docs_container, bootstyle="dark")
        github_frame.pack(fill='x', padx=15, pady=10)
        
        github_label = ttk.Label(
            github_frame, 
            text="🌐 GitHub: https://github.com/TheKarimZZZ/OSCI",
            bootstyle="inverse-dark",
            cursor="hand2",
            foreground="#00ffff"  
        )
        github_label.pack(anchor='center')
        github_label.bind("<Button-1>", lambda e: self.open_github())
        
        docs_text = scrolledtext.ScrolledText(
            docs_container, 
            wrap=tk.WORD,
            bg="#1a1a1a",
            fg="#00ff00",
            insertbackground="#00ff00",
            selectbackground="#003300",
            font=("Consolas", 10)
        )
        docs_text.pack(fill='both', expand=True, padx=15, pady=5)
        
        documentation = """
СОРИ ЗА КАЧЕСТВО ДОКУМЕНТАЦИЯ ОТ ДИПСИКА
=== OSCI - ГЕНЕРАТОР ЗВУКА ИЗ ГРАФИКОВ ===

🎵 ОСНОВНАЯ КОНЦЕПЦИЯ
Преобразуйте любую математическую функцию в электронный звук.
Функция автоматически масштабируется в диапазон 80-400 Гц.

🔧 ДОСТУПНЫЕ ФУНКЦИИ
• Основные: x, x^2, sqrt(x), abs(x)
• Тригонометрия (радианы): sin(x), cos(x), tan(x)
• Тригонометрия (градусы): sind(x), cosd(x), tand(x)
• Экспоненты: exp(x), log(x), log10(x)
• Константы: pi, e

🎛️ КУСОЧНЫЕ ФУНКЦИИ
Создавайте сложные графики, комбинируя несколько функций:
• Каждая функция работает на своем диапазоне X
• Конец предыдущего = начало следующего
• Используйте кнопку '+' для добавления

📊 ПАРАМЕТРЫ
• Длительность: время звучания в секундах
• Диапазон X: интервал значений переменной
• Автомасштабирование: Y → 80-400 Гц

🎨 ПРИМЕРЫ
• Линейная: 2*x + 1
• Квадратичная: x^2
• Синус: sin(2*pi*x)
• Ступенчатая: floor(x)

⚡ ЭЛЕКТРО-СИНТЕЗ
• Основной осциллятор + суб-басс
• Пилообразная волна для гармоник
• Дисторшн + реверберация
• Фильтр низких частот

💾 ВЫХОД
Файл: graph_sound_<время>sec.wav

🌐 GITHUB
Проект доступен на GitHub: https://github.com/TheKarimZZZ/OSCI
Там вы найдете:
• Исходный код
• Примеры использования
• Инструкции по установке
• Возможность сообщить о проблемах

"""
        
        docs_text.insert('1.0', documentation)
        docs_text.config(state='disabled')
    
    def setup_settings_tab(self):
        main_container = ttk.Frame(self.settings_frame, bootstyle="dark")
        main_container.pack(fill='both', expand=True, padx=0, pady=0)
        
        top_frame = ttk.Frame(main_container, bootstyle="dark")
        top_frame.pack(fill='x', padx=15, pady=10)
        
        settings_left = ttk.Frame(top_frame, bootstyle="dark")
        settings_left.pack(side='left', fill='x', expand=True)
        
        ttk.Label(settings_left, text="ДЛИТЕЛЬНОСТЬ ЗВУКА (СЕК):", bootstyle="inverse-dark").pack(side='left', padx=(0, 10))
        self.duration_var = tk.StringVar(value="4.0")
        duration_entry = ttk.Entry(
            settings_left, 
            textvariable=self.duration_var, 
            width=15,
            bootstyle="dark"
        )
        duration_entry.pack(side='left', padx=(0, 20))
        
        github_frame = ttk.Frame(top_frame, bootstyle="dark")
        github_frame.pack(side='right')
        
        github_label = ttk.Label(
            github_frame, 
            text="🌐 GitHub",
            bootstyle="inverse-dark",
            cursor="hand2",
            foreground="#00ffff" 
        )
        github_label.pack(side='right')
        github_label.bind("<Button-1>", lambda e: self.open_github())
        
        functions_container = ttk.Frame(main_container, bootstyle="dark")
        functions_container.pack(fill='both', expand=True, padx=15, pady=10)
        
        functions_frame = ttk.Labelframe(
            functions_container, 
            text="ФУНКЦИИ", 
            bootstyle="dark",
            padding=10
        )
        functions_frame.pack(fill='both', expand=True, padx=0, pady=0)
        
        header_frame = ttk.Frame(functions_frame, bootstyle="dark")
        header_frame.pack(fill='x', pady=(0, 10))
        
        ttk.Label(header_frame, text="ФУНКЦИЯ", bootstyle="inverse-dark", width=25).pack(side='left', padx=5)
        ttk.Label(header_frame, text="НАЧАЛО X", bootstyle="inverse-dark", width=20).pack(side='left', padx=5)
        ttk.Label(header_frame, text="КОНЕЦ X", bootstyle="inverse-dark", width=20).pack(side='left', padx=5)
        ttk.Label(header_frame, text="УДАЛИТЬ", bootstyle="inverse-dark", width=10).pack(side='left', padx=5)
        
        scroll_container = ttk.Frame(functions_frame, bootstyle="dark")
        scroll_container.pack(fill='both', expand=True, pady=5)
        
        self.canvas = tk.Canvas(scroll_container, bg="#1a1a1a", highlightthickness=0)
        scrollbar = ttk.Scrollbar(scroll_container, orient="vertical", command=self.canvas.yview, bootstyle="dark-round")
        self.scrollable_frame = ttk.Frame(self.canvas, bootstyle="dark")
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=self.canvas.winfo_width())
        
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        bottom_frame = ttk.Frame(functions_frame, bootstyle="dark")
        bottom_frame.pack(fill='x', pady=10)
        
        add_button = ttk.Button(
            bottom_frame, 
            text="+ ДОБАВИТЬ ФУНКЦИЮ", 
            command=self.add_function_row,
            bootstyle="success-outline",
            width=20,
        )
        add_button.pack(anchor='center')  
        
        generate_frame = ttk.Frame(main_container, bootstyle="dark")
        generate_frame.pack(fill='x', padx=15, pady=20)
        
        generate_button = ttk.Button(
            generate_frame, 
            text="🚀 СГЕНЕРИРОВАТЬ ЗВУК", 
            command=self.generate_sound,
            bootstyle="success",
            width=25
        )
        generate_button.pack(anchor='center')  
        
        self.add_function_row()
        
        self.root.update_idletasks()
    
    def on_canvas_configure(self, event):
        self.canvas.itemconfig(self.canvas_window, width=event.width)
    
    def add_function_row(self):
        row = len(self.functions)
        
        if row == 0:
            start_x = "0"
        else:
            prev_end_var = self.functions[-1]['end_var']
            start_x = prev_end_var.get()
        
        func_var = tk.StringVar(value="sin(2*pi*x)")
        start_var = tk.StringVar(value=start_x)
        end_var = tk.StringVar(value=str(float(start_x) + 2*np.pi))
        
        row_frame = ttk.Frame(self.scrollable_frame, bootstyle="dark")
        row_frame.pack(fill='x', pady=2)
        
        func_entry = ttk.Entry(
            row_frame, 
            textvariable=func_var,
            bootstyle="dark",
            width=25 
        )
        func_entry.pack(side='left')
        
        start_entry = ttk.Entry(
            row_frame, 
            textvariable=start_var, 
            bootstyle="dark",
            width=20  
        )
        start_entry.pack(side='left')
        
        end_entry = ttk.Entry(
            row_frame, 
            textvariable=end_var, 
            bootstyle="dark",
            width=20  
        )
        end_entry.pack(side='left')
        
        delete_button = ttk.Button(
            row_frame, 
            text="✕ УДАЛИТЬ", 
            command=lambda: self.delete_function_row(row_frame),
            bootstyle="danger-outline",
            width=12
        )
        delete_button.pack(side='left')
        
        self.functions.append({
            'func_var': func_var,
            'start_var': start_var,
            'end_var': end_var,
            'row_frame': row_frame
        })
        
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def delete_function_row(self, row_frame):
        if len(self.functions) <= 1:
            messagebox.showwarning("Предупреждение", "Должна остаться хотя бы одна функция")
            return
        
        for i, func_data in enumerate(self.functions):
            if func_data['row_frame'] == row_frame:
                self.functions.pop(i)
                break
        
        row_frame.destroy()
        
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def safe_eval_point(self, expr, x_val):
        def sind(degrees):
            return np.sin(np.deg2rad(degrees))
        
        def cosd(degrees):
            return np.cos(np.deg2rad(degrees))
        
        def tand(degrees):
            return np.tan(np.deg2rad(degrees))
        
        safe_dict = {
            'x': x_val,
            'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
            'asin': np.arcsin, 'acos': np.arccos, 'atan': np.arctan,
            'sinh': np.sinh, 'cosh': np.cosh, 'tanh': np.tanh,
            'sind': sind, 'cosd': cosd, 'tand': tand,
            'exp': np.exp, 'log': np.log, 'log10': np.log10,
            'sqrt': np.sqrt, 'abs': np.abs,
            'pi': np.pi, 'e': np.e,
            '__builtins__': {}
        }
        
        try:
            result = eval(expr, safe_dict)
            if np.isfinite(result):
                return result
            else:
                return np.nan
        except:
            return np.nan
    
    def generate_sound(self):
        if not self.functions:
            messagebox.showerror("Ошибка", "Добавьте хотя бы одну функцию")
            return
            
        try:
            duration = float(self.duration_var.get())
            if duration <= 0:
                duration = 4.0
        except:
            duration = 4.0
        
        sample_rate = 44100
        total_samples = int(sample_rate * duration)
        
        all_x = []
        all_y = []
        
        for func_data in self.functions:
            func_str = func_data['func_var'].get().strip()
            try:
                start_x = float(func_data['start_var'].get())
                end_x = float(func_data['end_var'].get())
            except:
                messagebox.showerror("Ошибка", "Некорректные значения диапазона X")
                return
            
            if start_x >= end_x:
                messagebox.showerror("Ошибка", "Начало диапазона должно быть меньше конца")
                return
            
            segment_ratio = (end_x - start_x) / self.get_total_x_range()
            segment_samples = int(total_samples * segment_ratio)
            
            if segment_samples == 0:
                segment_samples = 1
            
            x_segment = np.linspace(start_x, end_x, segment_samples)
            y_segment = np.zeros_like(x_segment)
            
            valid_points = 0
            for i, x_val in enumerate(x_segment):
                result = self.safe_eval_point(func_str, x_val)
                if not np.isnan(result):
                    y_segment[i] = result
                    valid_points += 1
                else:
                    if i > 0:
                        y_segment[i] = y_segment[i-1]
                    else:
                        y_segment[i] = 0
            
            all_x.extend(x_segment)
            all_y.extend(y_segment)
        
        x_values = np.array(all_x)
        y_values = np.array(all_y)
        
        y_min, y_max = np.min(y_values), np.max(y_values)
        y_range = y_max - y_min
        
        if y_range > 0:
            frequencies = 80 + (y_values - y_min) / y_range * 320
        else:
            frequencies = 240 + 80 * np.sin(2 * np.pi * x_values / self.get_total_x_range())
        
        frequencies = np.clip(frequencies, 80, 400)
        
        t = np.linspace(0, duration, len(frequencies))
        phase = 2 * np.pi * np.cumsum(frequencies) / sample_rate
        
        main_wave = 0.4 * np.sin(phase)
        sub_bass = 0.25 * np.sin(phase * 0.5)
        saw_wave = 0.15 * signal.sawtooth(phase + 0.2)
        
        audio_signal = main_wave + sub_bass + saw_wave
        
        envelope = np.ones_like(t)
        attack = int(0.1 * sample_rate)
        envelope[:attack] = np.linspace(0, 1, attack)
        release = int(0.3 * sample_rate)
        envelope[-release:] = np.linspace(1, 0, release)
        
        audio_signal = audio_signal * envelope
        
        audio_signal = np.tanh(audio_signal * 1.3)
        
        delay = int(0.02 * sample_rate)
        reverb_signal = np.zeros_like(audio_signal)
        reverb_signal[delay:] = audio_signal[:-delay] * 0.4
        audio_signal = audio_signal + reverb_signal
        
        b, a = signal.butter(2, 2000/(sample_rate/2), btype='low')
        audio_signal = signal.filtfilt(b, a, audio_signal)
        
        audio_signal = audio_signal / np.max(np.abs(audio_signal)) * 0.7
        audio_signal = (audio_signal * 32767).astype(np.int16)
        
        filename = f"OSCI_sound_{duration}sec.wav"
        wavfile.write(filename, sample_rate, audio_signal)
        
        self.show_graphs(x_values, y_values, t, frequencies, audio_signal, duration)
        
        messagebox.showinfo("УСПЕШНО", f"Файл '{filename}' сохранен!\nДиапазон частот: {np.min(frequencies):.0f}-{np.max(frequencies):.0f} Гц")
    
    def get_total_x_range(self):
        if not self.functions:
            return 10.0
        
        try:
            start = float(self.functions[0]['start_var'].get())
            end = float(self.functions[-1]['end_var'].get())
            return end - start
        except:
            return 10.0
    
    def show_graphs(self, x_values, y_values, t, frequencies, audio_signal, duration):
        plt.style.use('dark_background')
        fig = plt.figure(figsize=(12, 10), facecolor='#1a1a1a')
        
        plt.subplot(3, 1, 1)
        plt.plot(x_values, y_values, '#00ff00', linewidth=2)
        plt.title('ГРАФИК', color='#00ff00', fontweight='bold')
        plt.xlabel('X', color='#00ff00')
        plt.ylabel('Y', color='#00ff00')
        plt.grid(True, alpha=0.2, color='#00ff00')
        plt.gca().set_facecolor('#1a1a1a')
        
        plt.subplot(3, 1, 2)
        plt.plot(t, frequencies, '#00ff00', linewidth=2)
        plt.axhline(y=80, color='#ff0066', linestyle='--', alpha=0.7, label='80 Гц')
        plt.axhline(y=400, color='#ff0066', linestyle='--', alpha=0.7, label='400 Гц')
        plt.title(f'ОЗВУЧКА ({duration} СЕК)', color='#00ff00', fontweight='bold')
        plt.xlabel('ВРЕМЯ (СЕК)', color='#00ff00')
        plt.ylabel('ЧАСТОТА (ГЦ)', color='#00ff00')
        plt.legend(facecolor='#1a1a1a', edgecolor='#00ff00', labelcolor='#00ff00')
        plt.grid(True, alpha=0.2, color='#00ff00')
        plt.gca().set_facecolor('#1a1a1a')
        
        plt.subplot(3, 1, 3)
        show_samples = min(2000, len(audio_signal))
        plt.plot(t[:show_samples], audio_signal[:show_samples] / 32767, '#00ff00', linewidth=1)
        plt.title('ФОРМА', color='#00ff00', fontweight='bold')
        plt.xlabel('ВРЕМЯ (СЕК)', color='#00ff00')
        plt.ylabel('АМПЛИТУДА', color='#00ff00')
        plt.grid(True, alpha=0.2, color='#00ff00')
        plt.gca().set_facecolor('#1a1a1a')
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = GraphSoundGenerator(root)
    root.mainloop()
