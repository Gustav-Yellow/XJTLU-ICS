import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from collections import deque

# 1. Define the graph structure and layout
nodes = [0, 1, 2, 3, 4]
edges = [(0, 1), (1, 4), (0, 3), (0, 2), (1, 2), (2, 3)]
pos = {
    0: (0, 1),
    1: (1, 1),
    4: (1, 0),
    3: (0, 0),
    2: (0.5, 0.5),
}

# 2. Pseudocode lines to display
code_lines = [
    "bfs (vertex v) {",
    "    create an empty queue for storing vertices to be visited;",
    "    add v into the queue;",
    "    mark v visited;",
    "    while the queue is not empty {",
    "        dequeue a vertex, say u, from the queue;",
    "        for each neighbor w of u",
    "            if w has not been visited {",
    "                add w into the queue;",
    "                set u as the parent for w;",
    "                mark w visited;",
    "            }",
    "    }",
    "}",
]

# 3. BFS tracing events
events = []
visited = set()
parent = {}
adj = {v: [] for v in nodes}
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

def bfs_capture(start):
    queue = deque()
    events.append(("init_queue", start, None))
    queue.append(start)
    events.append(("enqueue_start", start, None))
    visited.add(start)
    events.append(("mark_start", start, None))
    while queue:
        events.append(("check_empty", None, None))
        u = queue.popleft()
        events.append(("dequeue", u, None))
        for w in sorted(adj[u]):
            events.append(("for", u, w))
            events.append(("check_if", u, w))  # ✅ highlight if line
            if w not in visited:
                queue.append(w)
                events.append(("enqueue", w, u))
                parent[w] = u
                events.append(("setparent", u, w))
                visited.add(w)
                events.append(("mark_child", w, None))
            else:
                events.append(("skip", u, w))
    events.append(("end", None, None))

bfs_capture(0)

# GUI state
step_index = 0
narrative_frame = None
narrative_text = None

# Set up figure
fig, (ax_graph, ax_code) = plt.subplots(1, 2, figsize=(10, 6))
fig.tight_layout()

# Dimensions for pseudocode box
total_lines = len(code_lines)
line_height = 0.08
box_padding = 0.02
box_height = total_lines * line_height + 2 * box_padding
box_width = 1.0 - 2 * box_padding
box_x = box_padding
box_y = 1 - box_height

# Highlight map (now includes check_if)
highlight_map = {
    'init_queue': 1,
    'enqueue_start': 2,
    'mark_start': 3,
    'check_empty': 4,
    'dequeue': 5,
    'for': 6,
    'check_if': 7,     # ✅ if line
    'skip': 6,
    'enqueue': 8,
    'setparent': 9,
    'mark_child': 10,
    'end': 12
}

# Update function
def update_plot():
    global narrative_frame, narrative_text
    ax_graph.clear()
    ax_code.clear()
    ax_code.axis('off')

    etype, u, w = events[step_index]

    # Draw graph
    cur_visited = {e[1] for e in events[:step_index+1] if e[0] in ('mark_start','mark_child')}
    tree_edges = [(e[1], e[2]) for e in events[:step_index+1] if e[0] == 'setparent']
    for n in nodes:
        x0, y0 = pos[n]
        color = 'red' if n in cur_visited else 'white'
        label_color = 'white' if n in cur_visited else 'black'
        ax_graph.scatter(x0, y0, s=600, c=color, edgecolors='black', zorder=2)
        ax_graph.text(x0, y0, str(n), fontsize=14, fontweight='bold',
                     color=label_color, va='center', ha='center')
    for a, b in edges:
        ax_graph.plot([pos[a][0], pos[b][0]], [pos[a][1], pos[b][1]], c='black')
    for par, child in tree_edges:
        ax_graph.plot([pos[par][0], pos[child][0]], [pos[par][1], pos[child][1]], c='red', linewidth=2)
    ax_graph.axis('off')

    # Draw pseudocode
    ax_code.add_patch(Rectangle((box_x, box_y), box_width, box_height,
                                fill=False, edgecolor='black'))
    line_idx = highlight_map.get(etype)
    if line_idx is not None:
        hl_y = box_y + box_height - (line_idx + 1) * line_height
        ax_code.add_patch(Rectangle((box_x+0.005, hl_y), box_width-0.01,
                                    line_height, facecolor='yellow', alpha=0.5))
    for i, txt in enumerate(code_lines, start=0):
        y0 = box_y + box_height - (i + 1)*line_height + (line_height-0.02)
        ax_code.text(box_x+0.01, y0, txt, va='top', family='monospace')

    canvas.draw()

    # Update current event label
    if w is None:
        current_label.config(text=f"Event: {etype}, v/u = {u}")
    else:
        current_label.config(text=f"Event: {etype}, u = {u}, w = {w}")

    # Reconstruct queue state
    dq = deque()
    for e in events[:step_index+1]:
        t, a, b = e
        if t == 'init_queue':
            dq = deque()
        elif t in ('enqueue_start', 'enqueue'):
            dq.append(a)
        elif t == 'dequeue' and dq:
            dq.popleft()
    queue_label.config(text=f"Queue: {list(dq)}")

    # Build narrative
    narrative = []
    i = 0
    while i <= step_index:
        t, a, b = events[i]
        if t == 'init_queue':
            narrative.append("Create empty queue")
        elif t == 'enqueue_start':
            narrative.append(f"Enqueue start vertex {a}")
        elif t == 'dequeue':
            narrative.append(f"Dequeue {a}")
        elif t == 'for':
            narrative.append(f"  for each neighbor {b} of {a}")
        elif t == 'check_if':
            pass  # no text for condition, only for highlight
        elif t == 'skip':
            narrative.append(f"    → {b} already visited, skip")
        elif t == 'enqueue':
            narrative.append(f"    → enqueue {a}")
        elif t == 'setparent':
            narrative.append(f"    → set parent[{b}] = {a}")
        elif t == 'mark_child':
            narrative.append(f"    → mark {a} visited")
        elif t == 'mark_start':
            narrative.append(f"    → mark {a} visited")
        i += 1

    if narrative_frame is None:
        narrative_frame = tk.Frame(root)
        narrative_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        scrollbar = tk.Scrollbar(narrative_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        narrative_text = tk.Text(narrative_frame, height=15, font=('Courier',12),
                                 yscrollcommand=scrollbar.set)
        narrative_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=narrative_text.yview)

    narrative_text.config(state=tk.NORMAL)
    narrative_text.delete('1.0', tk.END)
    narrative_text.insert(tk.END, "\n".join(narrative))
    narrative_text.config(state=tk.DISABLED)
    narrative_text.see(tk.END)

# Build GUI
root = tk.Tk()
root.title("BFS Visualization – Trace & Parent")
root.geometry("800x800")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

current_label = ttk.Label(root, text="", font=(None,14,'bold'))
current_label.pack(pady=5)

queue_label = ttk.Label(root, text="Queue: []", font=(None,14,'bold'))
queue_label.pack(pady=5)

button_frame = ttk.Frame(root)
button_frame.pack(pady=5)

def on_next():
    global step_index
    if step_index < len(events)-1:
        step_index += 1
        update_plot()

def on_reset():
    global step_index
    step_index = 0
    update_plot()

ttk.Button(button_frame, text='Next', command=on_next).pack(side=tk.LEFT, padx=5)
ttk.Button(button_frame, text='Reset', command=on_reset).pack(side=tk.LEFT, padx=5)

# Initial draw and start GUI
update_plot()
root.mainloop()
