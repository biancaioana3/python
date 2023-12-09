import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from threading import Timer


class NewsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("News App")
        self.root.geometry("600x400")

        self.categories = ["Astronomy", "Biology", "Medicine"]

        self.label_category = tk.Label(root, text="Select Category:")
        self.label_category.pack(pady=10)

        self.category_combobox = ttk.Combobox(root, values=self.categories)
        self.category_combobox.pack(pady=10)
        self.category_combobox.set(self.categories[0])

        self.title_label = tk.Label(root, text="Title:")
        self.title_label.pack(pady=5)

        self.title_text = tk.Text(root, height=1, width=50)
        self.title_text.pack(pady=5)

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack(pady=5)

        self.description_text = tk.Text(root, height=5, width=50)
        self.description_text.pack(pady=5)

        self.image_label = tk.Label(root, text="Image:")
        self.image_label.pack(pady=5)

        self.image_text = tk.Text(root, height=1, width=50)
        self.image_text.pack(pady=5)

        self.get_news_button = tk.Button(root, text="Get News", command=self.get_news)
        self.get_news_button.pack(pady=10)

        # Update news every 15 minutes
        self.update_interval = 15 * 60
        self.update_news()

    def get_news(self):
        category = self.category_combobox.get().lower()
        url = f"https://news.ycombinator.com/rss/{category}.rss"

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            items = soup.find_all("item")

            if items:
                item = items[0]  # Display the first item
                title = item.title.text
                description = item.description.text
                image_url = None

                # Check if the feed contains an image
                if "img" in description:
                    image_url = BeautifulSoup(description, "html.parser").find("img")["src"]

                self.title_text.delete(1.0, tk.END)
                self.title_text.insert(tk.END, title)

                self.description_text.delete(1.0, tk.END)
                self.description_text.insert(tk.END, description)

                self.image_text.delete(1.0, tk.END)
                self.image_text.insert(tk.END, image_url if image_url else "No image available")

        except Exception as e:
            print(f"Error fetching news: {e}")

        # Schedule the next update
        Timer(self.update_interval, self.update_news).start()

    def update_news(self):
        # Trigger a news update
        self.get_news()


if __name__ == "__main__":
    root = tk.Tk()
    app = NewsApp(root)
    root.mainloop()
