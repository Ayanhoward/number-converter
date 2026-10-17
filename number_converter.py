import tkinter as tk
from tkinter import messagebox, ttk

class NumberConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Computer Architecture: Number System Converter")
        self.root.geometry("500x550")
        self.root.config(bg="#f4f6f9")

        # Title Label
        title_label = tk.Label(
            root, text="Number System & Data Representation", 
            font=("Arial", 14, "bold"), bg="#f4f6f9", fg="#2c3e50"
        )
        title_label.pack(pady=15)

        # Main Frame
        frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
        frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Input Base Selection & Entry
        tk.Label(frame, text="Select Input Base:", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=0, column=0, sticky="w", padx=15, pady=10)
        
        self.base_var = tk.StringVar(value="Decimal")
        bases = ["Decimal", "Binary", "Hexadecimal", "Octal"]
        self.base_menu = ttk.Combobox(frame, textvariable=self.base_var, values=bases, state="readonly", width=15)
        self.base_menu.grid(row=0, column=1, padx=15, pady=10, sticky="ew")
        self.base_menu.bind("<<ComboboxChanged>>", self.clear_fields)

        # Input Value
        tk.Label(frame, text="Enter Value:", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=1, column=0, sticky="w", padx=15, pady=10)
        self.entry_val = tk.Entry(frame, font=("Arial", 11), width=18)
        self.entry_val.grid(row=1, column=1, padx=15, pady=10, sticky="ew")

        # Bit Width Selection (Architecture specific)
        tk.Label(frame, text="Bit Width (Word Size):", font=("Arial", 10, "bold"), bg="#ffffff").grid(row=2, column=0, sticky="w", padx=15, pady=10)
        self.bit_var = tk.StringVar(value="8-bit")
        bit_widths = ["8-bit", "16-bit", "32-bit"]
        self.bit_menu = ttk.Combobox(frame, textvariable=self.bit_var, values=bit_widths, state="readonly", width=15)
        self.bit_menu.grid(row=2, column=1, padx=15, pady=10, sticky="ew")

        # Convert Button
        convert_btn = tk.Button(
            frame, text="Convert", font=("Arial", 11, "bold"), 
            bg="#2980b9", fg="white", command=self.convert
        )
        convert_btn.grid(row=3, column=0, columnspan=2, pady=15, ipadx=20)

        # Results Display Frame
        res_frame = tk.LabelFrame(root, text=" Converted Outputs ", font=("Arial", 10, "bold"), bg="#f4f6f9", fg="#2c3e50")
        res_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.lbl_dec = tk.Label(res_frame, text="Decimal (Base 10): --", font=("Arial", 10), bg="#f4f6f9", anchor="w")
        self.lbl_dec.pack(fill=tk.X, padx=15, pady=5)

        self.lbl_bin = tk.Label(res_frame, text="Binary (Base 2): --", font=("Arial", 10), bg="#f4f6f9", anchor="w")
        self.lbl_bin.pack(fill=tk.X, padx=15, pady=5)

        self.lbl_hex = tk.Label(res_frame, text="Hexadecimal (Base 16): --", font=("Arial", 10), bg="#f4f6f9", anchor="w")
        self.lbl_hex.pack(fill=tk.X, padx=15, pady=5)

        self.lbl_oct = tk.Label(res_frame, text="Octal (Base 8): --", font=("Arial", 10), bg="#f4f6f9", anchor="w")
        self.lbl_oct.pack(fill=tk.X, padx=15, pady=5)

        self.lbl_twos = tk.Label(res_frame, text="2's Complement (Signed): --", font=("Arial", 10, "bold"), bg="#f4f6f9", fg="#c0392b", anchor="w")
        self.lbl_twos.pack(fill=tk.X, padx=15, pady=5)

    def clear_fields(self, event=None):
        self.entry_val.delete(0, tk.END)
        self.lbl_dec.config(text="Decimal (Base 10): --")
        self.lbl_bin.config(text="Binary (Base 2): --")
        self.lbl_hex.config(text="Hexadecimal (Base 16): --")
        self.lbl_oct.config(text="Octal (Base 8): --")
        self.lbl_twos.config(text="2's Complement (Signed): --")

    def convert(self):
        raw_input = self.entry_val.get().strip()
        base_type = self.base_var.get()
        bit_str = self.bit_var.get()
        bits = int(bit_str.split("-")[0])

        if not raw_input:
            messagebox.showerror("Error", "Input field cannot be empty!")
            return

        try:
            # Parse input based on selected base
            if base_type == "Decimal":
                dec_val = int(raw_input, 10)
            elif base_type == "Binary":
                dec_val = int(raw_input, 2)
            elif base_type == "Hexadecimal":
                dec_val = int(raw_input, 16)
            elif base_type == "Octal":
                dec_val = int(raw_input, 8)
            else:
                return

            # Range check for chosen word size
            max_val = (2 ** (bits - 1)) - 1
            min_val = -(2 ** (bits - 1))
            
            # Formulate standard outputs
            bin_val = bin(dec_val & 0xFFFFFFFF)[2:] # Raw bit pattern representation
            hex_val = hex(dec_val).upper()
            oct_val = oct(dec_val)

            # Handle 2's Complement for signed interpretation within chosen bit width
            if dec_val < 0 or dec_val > (2**bits - 1):
                # Check if it fits in signed range
                if dec_val < min_val or dec_val > max_val:
                    twos_comp_str = f"Out of range for {bits}-bit signed integer!"
                else:
                    # Compute two's complement bit string
                    if dec_val < 0:
                        twos_val = (1 << bits) + dec_val
                    else:
                        twos_val = dec_val
                    twos_comp_str = f"{twos_val:0{bits}b}"
            else:
                if dec_val >= (2**(bits-1)):
                    # Unsigned mapped to signed view
                    twos_comp_str = f"{dec_val:0{bits}b} (Unsigned overflow for signed view)"
                else:
                    twos_comp_str = f"{dec_val:0{bits}b}"

            # Update GUI labels
            self.lbl_dec.config(text=f"Decimal (Base 10): {dec_val}")
            self.lbl_bin.config(text=f"Binary (Base 2): {bin_val}")
            self.lbl_hex.config(text=f"Hexadecimal (Base 16): {hex_val}")
            self.lbl_oct.config(text=f"Octal (Base 8): {oct_val}")
            self.lbl_twos.config(text=f"2's Complement ({bits}-bit): {twos_comp_str}")

        except ValueError:
            messagebox.showerror("Invalid Input", f"The value '{raw_input}' is not valid for base {base_type}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberConverterApp(root)
    root.mainloop()