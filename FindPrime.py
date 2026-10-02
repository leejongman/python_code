import time
import tkinter as tk
from tkinter import ttk

def is_prime(number: int) -> bool:
    """Return True if number is a prime number, otherwise False."""
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for divisor in range(3,number, 2):
        if number % divisor == 0:
            return False
    return True

def main():
    root = tk.Tk()
    root.title("Find Prime Numbers")
    root.geometry("480x480")
    root.minsize(200, 200)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(2, weight=1)

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(4, weight=1)

    ttk.Label(main_frame, text="Find Prime Numbers", font=("Malgun Gothic", 18, "bold")).grid(
        row=0, column=0, sticky="w", pady=(0, 16)
    )
    ttk.Label(main_frame, text="End of the range to search").grid(row=1, column=0, sticky="w")

    input_frame = ttk.Frame(main_frame)
    input_frame.grid(row=2, column=0, sticky="ew", pady=(6, 16))
    input_frame.columnconfigure(0, weight=1)

    end_entry = ttk.Entry(input_frame)
    end_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8))
    find_button = ttk.Button(input_frame, text="Find Primes")
    find_button.grid(row=0, column=1)

    action_frame = ttk.Frame(main_frame)
    action_frame.grid(row=3, column=0, sticky="e", pady=(0, 10))
    clear_button = ttk.Button(action_frame, text="Clear")
    clear_button.grid(row=0, column=0, padx=(0, 8))
    exit_button = ttk.Button(action_frame, text="Exit", command=root.destroy)
    exit_button.grid(row=0, column=1)

    result_frame = ttk.Frame(main_frame)
    result_frame.grid(row=4, column=0, sticky="nsew")
    result_frame.columnconfigure(0, weight=1)
    result_frame.rowconfigure(0, weight=1)

    result_text = tk.Text(result_frame, wrap="word", height=14, state="disabled")
    result_text.grid(row=0, column=0, sticky="nsew")
    scrollbar = ttk.Scrollbar(result_frame, orient="vertical", command=result_text.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    result_text.configure(yscrollcommand=scrollbar.set)

    status_label = ttk.Label(main_frame, text="Please enter a positive integer.")
    status_label.grid(row=5, column=0, sticky="w", pady=(10, 0))

    def clear_form():
        end_entry.delete(0, tk.END)
        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.configure(state="disabled")
        status_label.configure(text="Please enter a positive integer.")
        end_entry.focus_set()

    def find_primes(event=None):
        try:
            end_number = int(end_entry.get().strip())
            if end_number < 0:
                raise ValueError
        except ValueError:
            status_label.configure(text="Please enter a positive integer.")
            end_entry.focus_set()
            return

        start = time.perf_counter()
        prime_numbers = [
            number for number in range(2, end_number + 1) if is_prime(number)
        ]
        elapsed = time.perf_counter() - start

        prime_lines = ",\n".join(
            "  " + ", ".join(map(str, prime_numbers[index:index + 10]))
            for index in range(0, len(prime_numbers), 10)
        )
        prime_list = f"[\n{prime_lines}\n]" if prime_lines else "[]"
        result = f"1부터 {end_number}까지의 소수:\n{prime_list}"

        result_text.configure(state="normal")
        result_text.delete("1.0", tk.END)
        result_text.insert("1.0", result)
        result_text.configure(state="disabled")
        status_label.configure(
            text=f"소수 {len(prime_numbers)}개 · 계산 시간 {elapsed:.4f}초"
        )

    find_button.configure(command=find_primes)
    clear_button.configure(command=clear_form)
    end_entry.bind("<Return>", find_primes)
    end_entry.focus_set()
    root.mainloop()

if __name__ == "__main__":
    main()
