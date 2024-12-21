import socket as sk
import tkinter as tk
from tkinter import messagebox
import subprocess

#start to code
root = tk.Tk()
root.title("Gathering Information Network")
root.geometry("1000x700")
root.config(bg="gray")

label = tk.Label(root, text="Input the IPv4", font=("Arial",16) )
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.insert(0, "")
entry.pack(pady=5)

def ping_ip():
    ip = entry.get().strip()
    if not ip:
        messagebox.showerror("ERROR", "Not Found Your IPv4 that You Input")
        return

    try:
        sk.inet_aton(ip)
    except sk.error:
        messagebox.showerror("ERROR", "Invalid IPv4!")
        return 

    try:
        response = subprocess.run(['ping', '-c', '4', ip], capture_output=True, text=True)
        if response.returncode==0:
            result.delete(1.0, tk.END)
            result.insert(tk.END, f"Scanning {ip} .........\n")
            result.insert(tk.END, response.stdout)
    except Exception:
        messagebox.showerror("ERROR", "Can Not Scan!Please Retry")

def adjust_timeout(val):
    timeout_label.config(text=f"Timeout: {val} seconds")

timeout_scale = tk.Scale(root, from_=1, to=10, orient='horizontal', command=adjust_timeout)
timeout_scale.pack(pady=5)

timeout_label = tk.Label(root, text="Timeout: 1 seconds")
timeout_label.pack(pady=5)

button = tk.Button(root, text="Ping", command=ping_ip)
button.pack(pady=5)

result = tk.Text(root, height=20, width=100, bg="lightgray")
result.pack(pady=5)

root.mainloop()
