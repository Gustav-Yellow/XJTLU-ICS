#!/usr/bin/env python3
import tkinter as tk
import math
from enum import Enum, auto

# ---- Data structures ----
class Vertex:
    def __init__(self, vid, x, y):
        self.id = vid
        self.x = x * 2
        self.y = y * 2

class Edge:
    def __init__(self, u, v, w):
        self.u, self.v, self.weight = u, v, w

class StepResult:
    def __init__(self, code_line, node=None, edge=None):
        self.code_line, self.node, self.edge = code_line, node, edge

# ---- Dijkstra stepper ----
class DijkstraStepper:
    class State(Enum):
        INIT_0 = auto(); INIT_1 = auto(); INIT_2 = auto()
        WHILE_CHECK = auto(); FIND_MIN = auto(); ADD_TO_T = auto()
        FOR_PREP = auto(); FOR_CHECK = auto(); IF_CHECK = auto()
        UPDATE_COST = auto(); UPDATE_PARENT = auto()
        CLOSE_WHILE = auto(); CLOSE_FUNC = auto(); DONE = auto()

    def __init__(self, V, E, source):
        self.V, self.E, self.source = V, E, source
        self.reset()

    def reset(self):
        self.state = DijkstraStepper.State.INIT_0
        self.cost = {v: float('inf') for v in self.V}
        self.parent = {v: None for v in self.V}
        self.T = set()
        self.edge_iter = None
        self.u = None
        self.current_edge = None
        self.cost[self.source] = 0

    def next(self):
        s = self.state
        if s == self.State.INIT_0:
            self.state = self.State.INIT_1; return StepResult(0)
        if s == self.State.INIT_1:
            self.state = self.State.INIT_2; return StepResult(1)
        if s == self.State.INIT_2:
            self.state = self.State.WHILE_CHECK; return StepResult(2)
        if s == self.State.WHILE_CHECK:
            if len(self.T) < len(self.V):
                self.state = self.State.FIND_MIN; return StepResult(3)
            else:
                self.state = self.State.CLOSE_WHILE; return StepResult(11)
        if s == self.State.FIND_MIN:
            best, u = float('inf'), None
            for v in self.V:
                if v not in self.T and self.cost[v] < best:
                    best, u = self.cost[v], v
            self.u = u
            self.state = self.State.ADD_TO_T
            return StepResult(4, node=u)
        if s == self.State.ADD_TO_T:
            self.T.add(self.u)
            self.edge_iter = iter(e for e in self.E if e.u == self.u and e.v not in self.T)
            self.state = self.State.FOR_PREP; return StepResult(5, node=self.u)
        if s == self.State.FOR_PREP:
            self.state = self.State.FOR_CHECK; return StepResult(6)
        if s == self.State.FOR_CHECK:
            try:
                e = next(self.edge_iter)
            except StopIteration:
                self.state = self.State.WHILE_CHECK; return StepResult(11)
            self.current_edge = e
            self.state = self.State.IF_CHECK
            return StepResult(6, node=e.v, edge=e)
        if s == self.State.IF_CHECK:
            e, v = self.current_edge, self.current_edge.v
            if v not in self.T and self.cost[v] > self.cost[self.u] + e.weight:
                self.state = self.State.UPDATE_COST
            else:
                self.state = self.State.FOR_CHECK
            return StepResult(7, node=v, edge=e)
        if s == self.State.UPDATE_COST:
            e, v = self.current_edge, self.current_edge.v
            self.cost[v] = self.cost[self.u] + e.weight
            self.state = self.State.UPDATE_PARENT
            return StepResult(8, node=v, edge=e)
        if s == self.State.UPDATE_PARENT:
            v = self.current_edge.v
            self.parent[v] = self.u
            self.state = self.State.FOR_CHECK
            return StepResult(9, node=v, edge=self.current_edge)
        if s == self.State.CLOSE_WHILE:
            self.state = self.State.CLOSE_FUNC; return StepResult(11)
        if s == self.State.CLOSE_FUNC:
            self.state = self.State.DONE; return StepResult(12)
        return StepResult(12)

# ---- GUI ----
class DijkstraGUI:
    FOR_LINE = 6
    IF_LINE = 7
    UPDATE_COST_LINE = 8
    UPDATE_PARENT_LINE = 9
    END_IF_LINE = 10
    ADD_TO_T_LINE = 5
    WHILE_LINE = 3

    VERTEX_RADIUS = 30
    LABEL_OFFSET = VERTEX_RADIUS
    REGION_PADDING = VERTEX_RADIUS + 10
    BLINK_COUNT = 5

    def __init__(self, master):
        self.master = master; master.title('Dijkstra Visualization')

        self.u_text = None
        self.v_text = None
        self.v_labels = {}
        self.arrow_items = []
        self.potential_edges = set()
        self.last_edge = None

        main = tk.Frame(master); main.pack(fill=tk.BOTH, expand=True)
        left = tk.Frame(main); left.pack(side=tk.LEFT, padx=10, pady=10)
        center = tk.Frame(main); center.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_btn = tk.Button(left, text='Next Step', command=self.on_next, font=('Consolas',14))
        self.next_btn.pack(fill='x', pady=(0,10))
        self.reset_btn = tk.Button(left, text='Reset', command=self.on_reset, font=('Consolas',14))
        self.reset_btn.pack(fill='x')
        self.status_label = tk.Label(left, text='u = -,  v = -', font=('Consolas',16))
        self.status_label.pack(pady=(10,20))

        self.code_lines = [
            'ShortestPathTree getShortestPath(s) {',
            'Let T be a set that contains the vertices whose paths to s are known; Initially T is empty;',
            'Set cost[s] = 0 and cost[v] = infinity for all other vertices in V',
            'while (size of T < n) {',
            '    Find u not in T with the smallest cost[u]',
            '    Add u to T',
            '    for (each (u, v) in E)',
            '        if (v not in T and cost[v] > cost[u] + w(u, v)) {',
            '            cost[v] = w(u, v) + cost[u]',
            '            parent[v] = u',
            '        }',
            '    }',
            '}'
        ]


        self.listbox = tk.Listbox(
            left,
            width=100,
            height=len(self.code_lines),
            font=('Consolas',14)
        )
        for ln in self.code_lines:
            self.listbox.insert(tk.END, ln)
        self.listbox.pack()

        tf = tk.Frame(left); tf.pack(pady=20)
        tk.Label(tf, text='cost',   font=('Consolas',16), fg='blue').grid(row=0, column=0, sticky='w')
        tk.Label(tf, text='parent', font=('Consolas',16)).grid(row=2, column=0, sticky='w')
        self.cost_labels = []; self.parent_labels = []

        self.vertices = [
            Vertex('A', 100, 300),
            Vertex('B', 50, 200),
            Vertex('C', 100, 80),
            Vertex('D', 200, 200),  # D 替代原 G 的位置
            Vertex('E', 300, 300),  # E 替代原 F 的位置
            Vertex('F', 350, 180),  # ✅ 新增 F
            Vertex('G', 250, 100)  # ✅ 新增 G
        ]
        self.vertex_indices = {v: i for i, v in enumerate(self.vertices)}


        raw = [
            ('A', 'B', 1),
            ('B', 'C', 5),
            ('C', 'A', 3),
            ('A', 'D', 2),
            ('C', 'D', 9),
            ('D', 'E', 8),
            ('A', 'E', 4),

            # ✅ 新增边
            ('E', 'F', 6),
            ('F', 'G', 7),
            ('C', 'G', 4),
            ('F', 'D', 5),
            ('G', 'D', 3)
        ]
        self.edges = []
        for u_id, v_id, w in raw:
            U = next(x for x in self.vertices if x.id==u_id)
            V = next(x for x in self.vertices if x.id==v_id)
            self.edges += [Edge(U,V,w), Edge(V,U,w)]

        self.stepper = DijkstraStepper(
            self.vertices, self.edges,
            next(v for v in self.vertices if v.id=='F')
        )

        for j, v in enumerate(self.vertices):
            c = tk.Label(tf, text='∞', width=6, relief='sunken', bg='white',
                         font=('Consolas',14), fg='blue')
            c.grid(row=0, column=j+1, padx=5, pady=5)
            self.cost_labels.append(c)
            p = tk.Label(tf, text='-', width=6, relief='sunken', bg='white',
                         font=('Consolas',14))
            p.grid(row=2, column=j+1, padx=5, pady=5)
            self.parent_labels.append(p)
            tk.Label(tf, text=v.id, width=6, relief='ridge', font=('Consolas',14)).grid(row=1, column=j+1)
            tk.Label(tf, text=v.id, width=6, relief='ridge', font=('Consolas',14)).grid(row=3, column=j+1)

        self.canvas = tk.Canvas(center, width=1200, height=800, bg='white')
        self.canvas.pack()
        self.node_items, self.edge_items = {}, {}
        for e in self.edges:
            if e.u.id < e.v.id:
                ln = self.canvas.create_line(
                    e.u.x, e.u.y, e.v.x, e.v.y, fill='gray', width=2)
                self.edge_items[(e.u,e.v)] = ln
                mx,my = (e.u.x+e.v.x)/2, (e.u.y+e.v.y)/2
                self.canvas.create_text(mx+20, my-20, text=str(e.weight), font=('Consolas',14))
        for v in self.vertices:
            oid = self.canvas.create_oval(
                v.x-self.VERTEX_RADIUS, v.y-self.VERTEX_RADIUS,
                v.x+self.VERTEX_RADIUS, v.y+self.VERTEX_RADIUS,
                fill='white', outline='black', width=3)
            self.canvas.create_text(v.x, v.y, text=v.id, font=('Consolas',16))
            self.node_items[v] = oid

        self.cost_labels_canvas, self.cost_values_canvas = {}, {}
        for v in self.vertices:
            lbl = self.canvas.create_text(
                v.x+self.VERTEX_RADIUS+30, v.y+self.VERTEX_RADIUS+15,
                text='cost', font=('Consolas',16), anchor='w', fill='blue'
            )
            val = self.canvas.create_text(
                v.x+self.VERTEX_RADIUS+80, v.y+self.VERTEX_RADIUS+15,
                text='0' if v==self.stepper.source else '∞',
                font=('Consolas',16), anchor='w', fill='blue'
            )
            self.cost_labels_canvas[v] = lbl
            self.cost_values_canvas[v] = val

        self.t_frame = None
        self.blinking_items = []
        self.original_texts = []
        self.blink_count = 0

        self.update_tables()
        self.highlight_T()

    def blink_updated_values(self, vertex, update_type):
        self.blinking_items.clear()
        self.original_texts.clear()
        idx = self.vertex_indices[vertex]
        if update_type == 'cost':
            self.blinking_items += [
                (self.cost_labels[idx], 'label'),
                (self.cost_values_canvas[vertex], 'canvas'),
            ]
        else:
            self.blinking_items.append((self.parent_labels[idx], 'label'))
        for item, typ in self.blinking_items:
            if typ == 'label':
                self.original_texts.append(item.cget('text'))
            else:
                self.original_texts.append(self.canvas.itemcget(item, 'text'))
        self.blink_count = 0
        self.do_blink()

    def do_blink(self):
        if self.blink_count >= self.BLINK_COUNT * 2:
            for (item, typ), txt in zip(self.blinking_items, self.original_texts):
                if typ == 'label':
                    item.config(text=txt)
                else:
                    self.canvas.itemconfig(item, text=txt)
            self.update_tables()
            return
        for i, (item, typ) in enumerate(self.blinking_items):
            if self.blink_count % 2 == 0:
                if typ == 'label':
                    item.config(text='')
                else:
                    self.canvas.itemconfig(item, text='')
            else:
                txt = self.original_texts[i]
                if typ == 'label':
                    item.config(text=txt)
                else:
                    self.canvas.itemconfig(item, text=txt)
        self.blink_count += 1
        self.master.after(200, self.do_blink)

    def update_tables(self):
        for j, v in enumerate(self.vertices):
            c = self.stepper.cost[v]
            txt = '∞' if c == float('inf') else str(int(c) if c.is_integer() else f"{c:.1f}")
            self.cost_labels[j].config(text=txt)
            pt = '-' if self.stepper.parent[v] is None else self.stepper.parent[v].id
            self.parent_labels[j].config(text=pt)
            self.canvas.itemconfig(self.cost_values_canvas[v], text=txt)

    def convex_hull(self, pts):
        pts = sorted(set(pts))
        def cross(o,a,b): return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
        lower=[]; upper=[]
        for p in pts:
            while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0: lower.pop()
            lower.append(p)
        for p in reversed(pts):
            while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0: upper.pop()
            upper.append(p)
        return lower[:-1]+upper[:-1]

    def highlight_T(self):
        pts = [(v.x, v.y) for v in self.stepper.T]
        if not pts: return
        if len(pts) >= 3:
            hull = self.convex_hull(pts)
            cx = sum(x for x, y in hull)/len(hull)
            cy = sum(y for x, y in hull)/len(hull)
            pad = DijkstraGUI.REGION_PADDING
            padded = []
            for x, y in hull:
                dx, dy = x-cx, y-cy; d = math.hypot(dx, dy)
                nx = cx + (dx/d)*(d+pad) if d else x
                ny = cy + (dy/d)*(d+pad) if d else y
                padded.append((nx, ny))
            coords = [c for p in padded for c in p]
        else:
            xs, ys = zip(*pts); m = DijkstraGUI.VERTEX_RADIUS
            coords = [min(xs)-m, min(ys)-m, max(xs)+m, min(ys)-m,
                      max(xs)+m, max(ys)+m, min(xs)-m, max(ys)+m]
        if self.t_frame is None:
            self.t_frame = self.canvas.create_polygon(coords, outline='blue',
                                                      dash=(4,2), fill='', width=5)
            self.canvas.tag_lower(self.t_frame)
        else:
            self.canvas.coords(self.t_frame, *coords)

    def on_next(self):
        res = self.stepper.next()


        if res.code_line == DijkstraGUI.WHILE_LINE:
            if self.v_text:
                self.canvas.delete(self.v_text); self.v_text = None
            for lid in list(self.v_labels.values()):
                self.canvas.delete(lid)
            self.v_labels.clear()


        if res.code_line == DijkstraGUI.FOR_LINE:
            if self.last_edge:
                self.canvas.itemconfig(self.edge_items[self.last_edge], fill='gray', width=2)
                self.last_edge = None
            if self.v_text:
                self.canvas.delete(self.v_text); self.v_text = None
            for lid in list(self.v_labels.values()):
                self.canvas.delete(lid)
            self.v_labels.clear()
            for ln in self.edge_items.values():
                self.canvas.itemconfig(ln, fill='gray', width=2)
            self.potential_edges = {
                e for e in self.edges
                if e.u == self.stepper.u and e.v not in self.stepper.T
            }
            for e in self.potential_edges:
                key = (e.u,e.v) if (e.u,e.v) in self.edge_items else (e.v,e.u)
                self.canvas.itemconfig(self.edge_items[key], fill='yellow', width=4)
                lid = self.canvas.create_text(
                    e.v.x + self.LABEL_OFFSET, e.v.y - self.LABEL_OFFSET,
                    text='v', font=('Consolas',24), fill='red'
                )
                self.v_labels[e.v] = lid


        if res.code_line == DijkstraGUI.IF_LINE and res.edge:
            key = (res.edge.u,res.edge.v) if (res.edge.u,res.edge.v) in self.edge_items else (res.edge.v,res.edge.u)
            self.canvas.itemconfig(self.edge_items[key], fill='red', width=4)
            self.last_edge = key
            if res.node not in self.v_labels:
                self.v_text = self.canvas.create_text(
                    res.node.x + self.LABEL_OFFSET, res.node.y - self.LABEL_OFFSET,
                    text='v', font=('Consolas',24), fill='red'
                )
                self.v_labels[res.node] = self.v_text


        if res.code_line == DijkstraGUI.UPDATE_COST_LINE:
            self.update_tables()
            self.blink_updated_values(res.node, 'cost')


        if res.code_line == DijkstraGUI.UPDATE_PARENT_LINE:
            self.update_tables()
            self.blink_updated_values(res.node, 'parent')


        if res.code_line == DijkstraGUI.END_IF_LINE:
            if self.last_edge:
                self.canvas.itemconfig(self.edge_items[self.last_edge], fill='gray', width=2)
                self.last_edge = None
            if self.v_text:
                self.canvas.delete(self.v_text); self.v_text = None
            for lid in list(self.v_labels.values()):
                self.canvas.delete(lid)
            self.v_labels.clear()


        if res.code_line == DijkstraGUI.ADD_TO_T_LINE:
            self.highlight_T()
            node = res.node; p = self.stepper.parent[node]
            if p:
                dx,dy = node.x-p.x, node.y-p.y; d=math.hypot(dx,dy); r=DijkstraGUI.VERTEX_RADIUS
                sx,sy = (p.x+dx/d*r,p.y+dy/d*r) if d else (p.x,p.y)
                ex,ey = (node.x-dx/d*r,node.y-dy/d*r) if d else (node.x,node.y)
                arr = self.canvas.create_line(sx,sy,ex,ey, arrow=tk.LAST, fill='green', width=3)
                self.arrow_items.append(arr)


        if self.u_text:
            self.canvas.delete(self.u_text)
        u = self.stepper.u
        if u:
            self.u_text = self.canvas.create_text(
                u.x + self.LABEL_OFFSET, u.y - self.LABEL_OFFSET,
                text='u', font=('Consolas',24), fill='green'
            )


        self.listbox.selection_clear(0, tk.END)
        if 0 <= res.code_line < len(self.code_lines):
            self.listbox.selection_set(res.code_line)
            self.listbox.see(res.code_line)
        v_id = res.node.id if (res.node and res.node is not u) else '-'
        self.status_label.config(text=f"u = {u.id if u else '-'},  v = {v_id}")

    def on_reset(self):
        for arr in self.arrow_items:
            self.canvas.delete(arr)
        self.arrow_items.clear()
        if self.t_frame:
            self.canvas.delete(self.t_frame); self.t_frame = None
        if self.u_text:
            self.canvas.delete(self.u_text); self.u_text = None
        if self.v_text:
            self.canvas.delete(self.v_text); self.v_text = None
        for lid in self.v_labels.values():
            self.canvas.delete(lid)
        self.v_labels.clear()
        self.last_edge = None

        self.stepper.reset()
        self.potential_edges.clear()
        for ln in self.edge_items.values():
            self.canvas.itemconfig(ln, fill='gray', width=2)
        for v, oid in self.node_items.items():
            self.canvas.itemconfig(oid, fill='white', outline='black', width=3)
        for v in self.vertices:
            default = '0' if v == self.stepper.source else '∞'
            self.canvas.itemconfig(self.cost_values_canvas[v], text=default)
            self.canvas.itemconfig(self.cost_labels_canvas[v], fill='blue')
        self.next_btn.config(state='normal')
        self.listbox.selection_clear(0, tk.END)
        self.status_label.config(text='u = -,  v = -')
        self.update_tables()
        self.highlight_T()

if __name__ == '__main__':
    root = tk.Tk()
    DijkstraGUI(root)
    root.mainloop()
