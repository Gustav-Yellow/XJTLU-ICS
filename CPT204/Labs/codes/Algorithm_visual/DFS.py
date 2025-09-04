import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


nodes = [0, 1, 2, 3, 4]
edges = [(0, 1), (1, 4), (0, 3), (0, 2), (1, 2), (2, 3)]
pos = {
    0: (0, 1),
    1: (1, 1),
    4: (1, 0),
    3: (0, 0),
    2: (0.5, 0.5),
}

code_lines = [
    "Tree dfs (vertex v) {",
    "    // Mark the current vertex as visited",
    "    visit v;",
    "    // Loop through each neighbor of v",
    "    for each neighbor w of v",
    "       // If this neighbor is not visited",
    "    if (w has not been visited) {",
    "       // Set v as the parent of w in the search tree",
    "    set v as the parent for w;",
    "    // Recursively visit w, which changes in each recursive step",
    "    dfs (w);",
    "    }",
    "}"
]

adj = {v: [] for v in nodes}
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
for v in adj:
    adj[v].sort()

events = []
visited = set()

def dfs(v, parent=None):
    events.append(("call", v, parent))
    events.append(("visit", v, parent))
    visited.add(v)
    for w in adj[v]:
        events.append(("for", v, w))
        events.append(("if", v, w))
        if w not in visited:
            events.append(("descent", v, w))
            events.append(("setparent", v, w))
            events.append(("recurse", v, w))
            dfs(w, parent=v)
            events.append(("backtrack", v, w))
        else:
            events.append(("skip", v, w))
    events.append(("return", v, parent))

dfs(0)

step_index = 0
fig, (ax_graph, ax_code) = plt.subplots(1, 2, figsize=(10, 6))
fig.tight_layout()

root = tk.Tk()
root.title('DFS Visualization – Directional Neighbors + Offset for 4')
root.geometry('800x800')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
current_label = ttk.Label(root, text="", font=(None, 14, 'bold'))
current_label.pack(pady=5)
button_frame = ttk.Frame(root)
button_frame.pack(pady=5)
narrative_frame = None
narrative_text = None

def get_active_nodes(events_subset):
    active = set()
    for t, v, _ in events_subset:
        if t == 'call':
            active.add(v)
        elif t == 'return' and v in active:
            active.remove(v)
    return active

def update_plot():
    global narrative_frame, narrative_text
    ax_graph.clear()
    ax_code.clear()
    ax_code.axis('off')

    etype, v, w = events[step_index]

    cur_vis = [e[1] for e in events[:step_index+1] if e[0] == 'visit']
    edges_tree = [(c, p) for (t, c, p) in events[:step_index+1] if t == 'descent']
    active_nodes = get_active_nodes(events[:step_index+1])


    for u, v0 in edges:
        ax_graph.plot([pos[u][0], pos[v0][0]], [pos[u][1], pos[v0][1]], c='black', linewidth=1)
    for c, p in edges_tree:
        ax_graph.plot([pos[c][0], pos[p][0]], [pos[c][1], pos[p][1]], c='red', linewidth=2)


    for n in nodes:
        x0, y0 = pos[n]
        color = 'red' if n in cur_vis else 'white'
        ax_graph.scatter(x0, y0, s=600, c=color, edgecolors='black', zorder=2)
        label = str(n)
        if etype == 'if' and n == w:
            label += ' (w)'
        ax_graph.text(x0, y0, label, fontsize=14, fontweight='bold', va='center', ha='center')


    for node in active_nodes:
        x0, y0 = pos[node]
        neighbors = adj[node]
        spacing = 0.1
        if node == 4:
            base_x = x0 - spacing * (len(neighbors) - 1) / 2 + 0.05  # 向右偏移
        else:
            base_x = x0 - spacing * (len(neighbors) - 1) / 2

        if node in [0, 1, 2]:
            base_y = y0 - 0.15
            va = 'top'
        else:
            base_y = y0 + 0.18
            va = 'bottom'

        if_seen = [w_ for (t_, a_, w_) in events[:step_index+1] if t_ == 'if' and a_ == node]
        for i, nei in enumerate(neighbors):
            color = 'green' if nei in if_seen else 'red'
            ax_graph.text(base_x + i * spacing, base_y, str(nei),
                          fontsize=12, ha='center', va=va, color=color, fontweight='bold')

    ax_graph.axis('off')


    box_padding = 0.02
    line_height = 0.08
    box_height = len(code_lines) * line_height + 2 * box_padding
    box_width = 1.0 - 2 * box_padding
    box_x = box_padding
    box_y = 1 - box_height

    ax_code.add_patch(Rectangle((box_x, box_y), box_width, box_height, fill=False, edgecolor='black'))
    highlight_map = {
        'call': 1, 'visit': 3, 'for': 5, 'if': 7, 'descent': 7,
        'setparent': 9, 'recurse': 11, 'skip': 7, 'backtrack': 5, 'return': 12
    }
    idx = highlight_map.get(etype)
    if idx:
        y = box_y + box_height - idx * line_height
        ax_code.add_patch(Rectangle((box_x+0.005, y), box_width-0.01, line_height, facecolor='yellow', alpha=0.5))

    for i, line in enumerate(code_lines, start=1):
        y0 = box_y + box_height - i*line_height + (line_height-0.02)
        ax_code.text(box_x+0.01, y0, line, va='top', family='monospace')

    canvas.draw()
    current_label.config(text=f"Current v = {v}" + (f", w = {w}" if w is not None else ""))


    narrative = []
    stack = []
    indent = lambda: '  ' * len(stack)
    seen_for = set()
    for t, a, b in events[:step_index+1]:
        if t == 'call':
            narrative.append(indent() + f"⇘ enter dfs({a})")
            stack.append(a)
        elif t == 'visit':
            narrative.append(indent() + f"✓ visit {a}")
        elif t == 'for':
            if a not in seen_for:
                neigh = adj[a]
                narrative.append(indent() + f"↻ dfs({a}) has neighbors: {', '.join(map(str, neigh))}")
                seen_for.add(a)
        elif t == 'descent':
            narrative.append(indent() + f"→ neighbor {b} not visited")
        elif t == 'setparent':
            narrative.append(indent() + f"⇨ set parent[{b}] = {a}")
        elif t == 'recurse':
            narrative.append(indent() + f"→ dfs({b})")
        elif t == 'skip':
            narrative.append(indent() + f"↷ neighbor {b} already visited, skip")
        elif t == 'backtrack':
            narrative.append(indent() + f"↩ backtrack to dfs({a})")
        elif t == 'return':
            narrative.append(indent() + f"⇗ return from dfs({a})")
            if stack:
                stack.pop()
            narrative.append("")

    if narrative_frame is None:
        narrative_frame = tk.Frame(root)
        narrative_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        scrollbar = tk.Scrollbar(narrative_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        narrative_text = tk.Text(narrative_frame, height=15, font=('Courier', 16), yscrollcommand=scrollbar.set)
        narrative_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=narrative_text.yview)

    narrative_text.config(state=tk.NORMAL)
    narrative_text.delete('1.0', tk.END)
    narrative_text.insert(tk.END, "\n".join(narrative))
    narrative_text.config(state=tk.DISABLED)
    narrative_text.see(tk.END)

def on_next():
    global step_index
    if step_index < len(events) - 1:
        step_index += 1
        update_plot()

def on_reset():
    global step_index
    step_index = 0
    update_plot()

ttk.Button(button_frame, text='Next', command=on_next).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text='Reset', command=on_reset).pack(side=tk.LEFT, padx=5)

update_plot()
root.mainloop()
