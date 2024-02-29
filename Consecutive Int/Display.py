import tkinter as tk
from tkinter import ttk

def gcd_euclidean(m, n):
    it = 0
    iterations = []
    while n:
        it += 1
        iterations.append((m, n))
        m, n = n, m % n
    time_e = it * 0.001  
    return m, iterations, time_e

def gcd_consecutive(m, n):
    it = 0
    iterations = []
    i = min(m, n)
    while i > 0:
        it += 1
        iterations.append((m, n, i))
        if m % i == 0 and n % i == 0:
            break
        i -= 1
    time_c = it * 0.001 
    return i, iterations, time_c

#Euclidean algorithm
result_e, iterations_e, time_e = gcd_euclidean(31415, 14142)

#Consecutive Integer algorithm
result_c, iterations_c, time_c = gcd_consecutive(31415, 14142)

#Tkinter GUI
root = tk.Tk()
root.title("GCD Algorithms")

# Create a frame for the table layout
table_frame = ttk.Frame(root)
table_frame.pack()

# Euclidean Algorithm table
euclidean_tree = ttk.Treeview(table_frame, columns=("GCD", "Iterations"))
euclidean_tree.heading("#0", text="Euclidean Algorithm")
euclidean_tree.heading("#1", text="GCD")
euclidean_tree.heading("#2", text="Iterations")

euclidean_tree.insert("", "end", text="Euclidean", values=(result_e, len(iterations_e)))
for i, iteration in enumerate(iterations_e, start=1):
    euclidean_tree.insert("", "end", text=f"Iteration {i}", values=iteration)

euclidean_tree.column("#1", width=50)  # Adjust column width
euclidean_tree.column("#2", width=150)  # Adjust column width


euclidean_tree.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add scrollbar for Euclidean table
euclidean_scroll = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=euclidean_tree.yview)
euclidean_tree.configure(yscrollcommand=euclidean_scroll.set)
euclidean_scroll.pack(side=tk.LEFT, fill=tk.Y)


# Consecutive Integer Algorithm table
consecutive_tree = ttk.Treeview(table_frame, columns=("GCD", "Iterations"))
consecutive_tree.heading("#0", text="Consecutive Integer Algorithm")
consecutive_tree.heading("#1", text="GCD")
consecutive_tree.heading("#2", text="Iterations")

consecutive_tree.column("#1", width=50)  # Adjust column width
consecutive_tree.column("#2", width=150)  # Adjust column width

# Add scrollbar for Euclidean table
consecutive_scroll = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=consecutive_tree.yview)
consecutive_tree.configure(yscrollcommand=consecutive_scroll.set)
consecutive_scroll.pack(side=tk.RIGHT, fill=tk.Y)


consecutive_tree.insert("", "end", text="Consecutive", values=(result_c, len(iterations_c)))
for i, iteration in enumerate(iterations_c, start=1):
    consecutive_tree.insert("", "end", text=f"Iteration {i}", values=iteration)

consecutive_tree.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Total Time Taken
total_time_label = tk.Label(root, text=f"Total Time Taken by Euclidean Algorithm: {time_e:.3f} seconds\nTotal Time Taken by CI Algorithm: {time_c:.3f} seconds")
total_time_label.pack()

root.mainloop()
