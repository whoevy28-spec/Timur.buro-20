import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import requests
import re
import threading
import time

class RobloxCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roblox Game Checker 2025 DEBUG")
        self.root.geometry("900x780")

        self.min_online_var = tk.IntVar(value=10)
        self.check_public_var = tk.BooleanVar(value=True)
        self.cookie_var = tk.StringVar(value="")

        self.setup_ui()

    def setup_ui(self):
        settings = ttk.LabelFrame(self.root, text=" Настройки фильтра ")
        settings.pack(fill="x", padx=10, pady=5)

        ttk.Label(settings, text="Минимальный онлайн:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(settings, textvariable=self.min_online_var, width=10).grid(row=0, column=1, padx=5, pady=5)
        ttk.Checkbutton(
            settings,
            text="Только открытые игры (Public)",
            variable=self.check_public_var
        ).grid(row=0, column=2, padx=20)

        cookie_frame = ttk.LabelFrame(self.root, text=" .ROBLOSECURITY Cookie ")
        cookie_frame.pack(fill="x", padx=10, pady=5)
        ttk.Label(cookie_frame, text="Вставьте .ROBLOSECURITY сюда:").pack(anchor="w", padx=5)
        ttk.Entry(cookie_frame, textvariable=self.cookie_var, show="*").pack(fill="x", padx=5, pady=5)

        ttk.Label(self.root, text="Ссылки на игры:").pack(anchor="w", padx=10, pady=(10, 0))
        self.input_area = scrolledtext.ScrolledText(self.root, height=12)
        self.input_area.pack(fill="both", padx=10, pady=5, expand=True)

        self.start_btn = ttk.Button(
            self.root, text="▶ НАЧАТЬ ПРОВЕРКУ",
            command=self.start_checking_thread
        )
        self.start_btn.pack(fill="x", padx=10, pady=8)

        ttk.Label(self.root, text="Результаты:").pack(anchor="w", padx=10)
        self.output_area = scrolledtext.ScrolledText(
            self.root, height=15, state='disabled', bg="#f8f9fa"
        )
        self.output_area.pack(fill="both", padx=10, pady=5, expand=True)

        self.status_label = ttk.Label(
            self.root, text="Готов", relief="sunken", anchor="w"
        )
        self.status_label.pack(side="bottom", fill="x")

    def log(self, text):
        self.output_area.configure(state='normal')
        self.output_area.insert(tk.END, text + "\n")
        self.output_area.see(tk.END)
        self.output_area.configure(state='disabled')

    def get_headers(self, with_cookie=True):
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json",
            "Referer": "https://www.roblox.com/"
        }
        if with_cookie:
            cookie = self.cookie_var.get().strip()
            if cookie:
                if not cookie.startswith(".ROBLOSECURITY="):
                    cookie = f".ROBLOSECURITY={cookie}"
                headers["Cookie"] = cookie
        return headers

    def get_universe_id(self, place_id, headers):
        try:
            url = f"https://apis.roblox.com/universes/v1/places/{place_id}/universe"
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                uid = r.json().get("universeId")
                if uid:
                    return str(uid)
            elif r.status_code == 429:
                return "429"
        except:
            pass
        return None

    def start_checking_thread(self):
        thread = threading.Thread(target=self.run_checker, daemon=True)
        thread.start()

    def run_checker(self):
        self.start_btn.config(state="disabled")
        self.output_area.configure(state='normal')
        self.output_area.delete('1.0', tk.END)
        self.output_area.configure(state='disabled')

        raw_text = self.input_area.get("1.0", tk.END).strip()
        links = list(set([
            line.strip() for line in raw_text.split('\n')
            if 'roblox.com/games/' in line
        ]))

        if not links:
            messagebox.showwarning("Ошибка", "Вставьте ссылки!")
            self.start_btn.config(state="normal")
            return

        headers = self.get_headers()
        has_cookie = "Cookie" in headers

        if has_cookie:
            self.log("[+] Куки обнаружен")
        else:
            self.log("[!] Куки нет — медленный режим")

        place_ids = []
        id_to_link = {}
        for link in links:
            m = re.search(r'games/(\d+)', link)
            if m:
                pid = m.group(1)
                place_ids.append(pid)
                id_to_link[pid] = link

        self.log(f"[*] Найдено игр: {len(place_ids)}\n")

        # ======= ЭТАП 1: Universe IDs =======
        self.log("[*] Шаг 1: Получаю Universe IDs...")
        universe_map = {}

        for i, pid in enumerate(place_ids):
            self.status_label.config(text=f"Universe ID: {i+1}/{len(place_ids)}")
            uid = self.get_universe_id(pid, headers)

            if uid == "429":
                self.log(f"[!] 429 на игре #{i+1}. Жду 30 сек...")
                time.sleep(30)
                uid = self.get_universe_id(pid, headers)

            if uid and uid != "429":
                universe_map[uid] = pid

            time.sleep(0.3 if has_cookie else 2.0)

        self.log(f"[+] Universe IDs: {len(universe_map)}/{len(place_ids)}\n")

        if not universe_map:
            self.log("[!] Не удалось получить ни одного Universe ID.")
            self.start_btn.config(state="normal")
            return

        # ======= ЭТАП 2: Проверка игр =======
        self.log(f"[*] Шаг 2: Проверяю {len(universe_map)} игр...")
        valid_count = 0
        u_ids = list(universe_map.keys())
        chunks = [u_ids[i:i+50] for i in range(0, len(u_ids), 50)]

        for chunk_i, chunk in enumerate(chunks):
            self.status_label.config(text=f"Пачка {chunk_i+1}/{len(chunks)}")
            self.log(f"\n[*] Пачка {chunk_i+1}: {len(chunk)} игр")
            self.log(f"    Universe IDs: {chunk[:3]}...")  # Показываем первые 3 для отладки

            try:
                url = f"https://games.roblox.com/v1/games?universeIds={','.join(chunk)}"
                self.log(f"    URL: {url[:80]}...")

                r = requests.get(url, headers=headers, timeout=15)
                self.log(f"    Статус ответа: {r.status_code}")
                self.log(f"    Тело ответа: {r.text[:300]}")  # Полный ответ для дебага

                if r.status_code == 429:
                    self.log("[!] 429! Жду 20 сек...")
                    time.sleep(20)
                    r = requests.get(url, headers=headers, timeout=15)
                    self.log(f"    Повтор статус: {r.status_code}")
                    self.log(f"    Повтор тело: {r.text[:300]}")

                if r.status_code != 200:
                    self.log(f"[-] Ошибка: {r.status_code}")
                    continue

                json_data = r.json()
                self.log(f"    JSON ключи: {list(json_data.keys())}")

                games = json_data.get('data', [])
                self.log(f"    Игр в ответе: {len(games)}")

                for game in games:
                    try:
                        u_id = str(game.get('universeId', ''))
                        place_id = universe_map.get(u_id)
                        if not place_id:
                            self.log(f"    [!] universeId {u_id} не найден в universe_map")
                            continue

                        name = game.get('name', 'Без названия')
                        online = game.get('playing', 0)
                        is_playable = game.get('isPlayable', False)

                        self.log(f"    Игра: {name} | Онлайн: {online} | Открыта: {is_playable}")

                        passed = True
                        reasons = []

                        if online < self.min_online_var.get():
                            passed = False
                            reasons.append(f"онлайн {online}")

                        if self.check_public_var.get() and not is_playable:
                            passed = False
                            reasons.append("закрыта")

                        if passed:
                            self.log(f"\n[+] ПОДХОДИТ: {name} | Онлайн: {online}")
                            self.log(f"    https://www.roblox.com/games/{place_id}/")
                            valid_count += 1
                        else:
                            self.log(f"[-] Скип: {name} ({', '.join(reasons)})")

                    except Exception as e:
                        self.log(f"[-] Ошибка обработки: {e}")

                time.sleep(0.5)

            except Exception as e:
                self.log(f"[-] Критическая ошибка: {e}")

        self.log(f"\n{'='*50}")
        self.log(f"[*] ГОТОВО! Найдено: {valid_count} из {len(place_ids)}")
        self.log(f"{'='*50}")
        self.status_label.config(text=f"Готово! Найдено: {valid_count}")
        self.start_btn.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    app = RobloxCheckerApp(root)
    root.mainloop()