# -*- coding: utf-8 -*-
"""
build_graph.py — 知识图谱生成器（llm-wiki-agent 格式）

功能（确定性，无 LLM 调用、无第三方依赖）：
  1. 扫描 wiki/ 下所有 markdown 页面
  2. 解析 [[wikilink]] 生成 EXTRACTED 边
  3. 用连通分量做简单社区划分并着色
  4. 输出 graph/graph.json（节点/边数据）和 graph/graph.html（vis.js 交互图）
  5. 顺带报告断链（指向不存在页面的 wikilink）

用法：
  python tools/build_graph.py
"""

import json
import re
from pathlib import Path

WIKI_DIR = Path(__file__).resolve().parent.parent / "wiki"
GRAPH_DIR = Path(__file__).resolve().parent.parent / "graph"

WIKILINK_RE = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
TITLE_RE = re.compile(r'^title:\s*["\']?(.+?)["\']?\s*$', re.M)
TYPE_RE = re.compile(r"^type:\s*(\S+)", re.M)

# 社区配色（浅色主题）
PALETTE = [
    "#4e79a7", "#f28e2b", "#59a14f", "#e15759", "#b07aa1",
    "#76b7b2", "#edc948", "#9c755f", "#bab0ac", "#d37295",
]


def parse_page(path: Path):
    """解析单个 wiki 页面：返回 (元数据, wikilink 列表)。"""
    text = path.read_text(encoding="utf-8-sig")
    frontmatter = FRONTMATTER_RE.match(text)
    meta = {"title": path.stem, "type": "page"}
    if frontmatter:
        m = TITLE_RE.search(frontmatter.group(1))
        if m:
            meta["title"] = m.group(1).strip()
        m = TYPE_RE.search(frontmatter.group(1))
        if m:
            meta["type"] = m.group(1).strip()
    links = [l.strip() for l in WIKILINK_RE.findall(text)]
    return meta, links


def build():
    pages = {}
    for p in sorted(WIKI_DIR.rglob("*.md")):
        rel = p.relative_to(WIKI_DIR)
        meta, links = parse_page(p)
        meta["path"] = "wiki/" + rel.as_posix()
        meta["links"] = links
        pages[p.stem] = meta

    # 解析边 + 断链检测
    edges = []
    broken = []
    for stem, meta in pages.items():
        for target in meta["links"]:
            if target in pages:
                edges.append({"from": stem, "to": target, "type": "EXTRACTED"})
            else:
                broken.append((stem, target))

    # 连通分量 → 社区着色
    adj = {s: set() for s in pages}
    for e in edges:
        adj[e["from"]].add(e["to"])
        adj[e["to"]].add(e["from"])
    visited, community = set(), {}
    cid = 0
    for start in pages:
        if start in visited:
            continue
        queue, comp = [start], []
        visited.add(start)
        while queue:
            node = queue.pop()
            comp.append(node)
            for nxt in adj[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        for node in comp:
            community[node] = cid
        cid += 1

    nodes = []
    for stem, meta in pages.items():
        nodes.append({
            "id": stem,
            "label": meta["title"],
            "type": meta["type"],
            "path": meta["path"],
            "community": community[stem],
            "degree": len(adj[stem]),
        })

    GRAPH_DIR.mkdir(exist_ok=True)
    graph = {
        "directed": True,
        "multigraph": False,
        "generated_by": "tools/build_graph.py",
        "node_count": len(nodes),
        "edge_count": len(edges),
        "nodes": nodes,
        "edges": edges,
    }
    (GRAPH_DIR / "graph.json").write_text(
        json.dumps(graph, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    html = render_html(nodes, edges)
    (GRAPH_DIR / "graph.html").write_text(html, encoding="utf-8")

    return nodes, edges, broken


def render_html(nodes, edges):
    node_json = json.dumps(
        [
            {
                "id": n["id"],
                "label": n["label"],
                "title": f"{n['label']}（{n['type']}，度数 {n['degree']}）\n{n['path']}",
                "color": PALETTE[n["community"] % len(PALETTE)],
                "value": n["degree"] + 1,
                "shape": {"source": "square", "entity": "diamond",
                          "concept": "dot", "synthesis": "triangle",
                          "overview": "star", "page": "dot"}.get(n["type"], "dot"),
            }
            for n in nodes
        ],
        ensure_ascii=False,
    )
    edge_json = json.dumps(
        [{"from": e["from"], "to": e["to"], "arrows": "to"} for e in edges],
        ensure_ascii=False,
    )
    legend = "".join(
        f'<span style="margin-right:14px"><span style="display:inline-block;'
        f'width:10px;height:10px;background:{PALETTE[n["community"] % len(PALETTE)]};'
        f'border-radius:50%;margin-right:4px"></span>{n["label"]}</span>'
        for n in sorted(nodes, key=lambda x: -x["degree"])[:8]
    )
    return f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>知识图谱 — yagwen-data-analysis</title>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
<style>
  body {{ margin:0; font-family: "Microsoft YaHei", sans-serif; background:#fafafa; }}
  #header {{ padding:14px 20px; background:#fff; border-bottom:1px solid #e0e0e0; }}
  #header h1 {{ font-size:18px; margin:0 0 6px; }}
  #legend {{ font-size:13px; color:#555; }}
  #graph {{ width:100%; height:calc(100vh - 84px); }}
</style>
</head>
<body>
<div id="header">
  <h1>个人知识库 · 知识图谱（{len(nodes)} 个页面 / {len(edges)} 条链接）</h1>
  <div id="legend">连接最多的页面：{legend}</div>
</div>
<div id="graph"></div>
<script>
  var nodes = new vis.DataSet({node_json});
  var edges = new vis.DataSet({edge_json});
  var container = document.getElementById("graph");
  var data = {{ nodes: nodes, edges: edges }};
  var options = {{
    layout: {{ improvedLayout: true }},
    physics: {{ stabilization: true, barnesHut: {{ gravitationalConstant: -8000, springLength: 120 }} }},
    interaction: {{ hover: true, tooltipDelay: 150 }},
    edges: {{ color: "#9aa0a6", arrows: {{ to: {{ scaleFactor: 0.5 }} }}, smooth: false }}
  }};
  var network = new vis.Network(container, data, options);
</script>
</body>
</html>
"""


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    nodes, edges, broken = build()
    print(f"节点: {len(nodes)}  边: {len(edges)}  社区: {len(set(n['community'] for n in nodes))}")
    if broken:
        print(f"断链 {len(broken)} 条：")
        for src, tgt in broken:
            print(f"  [[{tgt}]]  (出现在 {src})")
    else:
        print("断链：无，所有 wikilink 均可解析")
    print("输出：graph/graph.json, graph/graph.html")
