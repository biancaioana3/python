import tkinter as tk
from tkinter import ttk, scrolledtext
import requests

class HTTPRequestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HTTP Request Client")

        self.create_widgets()

    def create_widgets(self):
        # Frames
        request_frame = ttk.Frame(self.root, padding="10")
        request_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        response_frame = ttk.Frame(self.root, padding="10")
        response_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Request Widgets
        ttk.Label(request_frame, text="Method:").grid(row=0, column=0, sticky=tk.W)
        self.method_var = tk.StringVar()
        method_combobox = ttk.Combobox(request_frame, textvariable=self.method_var, values=["GET", "POST", "PUT", "DELETE"])
        method_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(request_frame, text="URL:").grid(row=1, column=0, sticky=tk.W)
        self.url_entry = ttk.Entry(request_frame)
        self.url_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Label(request_frame, text="Headers:").grid(row=2, column=0, sticky=tk.W)
        self.headers_entry = ttk.Entry(request_frame)
        self.headers_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))

        ttk.Label(request_frame, text="Payload:").grid(row=3, column=0, sticky=tk.W)
        self.payload_entry = ttk.Entry(request_frame)
        self.payload_entry.grid(row=3, column=1, sticky=(tk.W, tk.E))

        ttk.Button(request_frame, text="Send Request", command=self.send_request).grid(row=4, column=0, columnspan=2, pady=(10, 0))

        # Response Widgets
        ttk.Label(response_frame, text="Response:").grid(row=0, column=0, sticky=tk.W)
        self.response_text = scrolledtext.ScrolledText(response_frame, wrap=tk.WORD, width=40, height=10)
        self.response_text.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(5, 0))

    def send_request(self):
        method = self.method_var.get()
        url = self.url_entry.get()
        headers = self.headers_entry.get()
        payload = self.payload_entry.get()

        try:
            response = requests.request(method, url, headers=headers, data=payload)
            response_text = f"Status Code: {response.status_code}\n\n{response.text}"
        except requests.RequestException as e:
            response_text = f"Error: {e}"

        self.response_text.delete(1.0, tk.END)  # Clear previous response
        self.response_text.insert(tk.END, response_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = HTTPRequestApp(root)
    root.mainloop()
