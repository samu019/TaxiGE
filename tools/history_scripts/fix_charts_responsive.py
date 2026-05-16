from pathlib import Path

p = Path("templates/dashboard/panel_home.html")
text = p.read_text(encoding="utf-8-sig").replace("\ufeff", "")

# Altura profesional de gráficos
text = text.replace(
""".chart-card {
    background: rgba(2,6,23,.45);
    border: 1px solid rgba(148,163,184,.20);
    border-radius: 22px;
    padding: 18px;
    min-height: 310px;
}""",
""".chart-card {
    background: rgba(2,6,23,.45);
    border: 1px solid rgba(148,163,184,.20);
    border-radius: 22px;
    padding: 18px;
    height: 280px;
    min-height: 280px;
    overflow: hidden;
}

.chart-card canvas {
    width: 100% !important;
    height: 220px !important;
    max-height: 220px !important;
}"""
)

# Responsive móvil
text = text.replace(
"""@media (max-width: 760px) {
    .filter-bar,
    .metric-grid,
    .compact-grid,
    .chart-grid {
        grid-template-columns: 1fr;
    }""",
"""@media (max-width: 760px) {
    .filter-bar,
    .metric-grid,
    .compact-grid,
    .chart-grid {
        grid-template-columns: 1fr;
    }

    .chart-card {
        height: 230px;
        min-height: 230px;
        padding: 14px;
    }

    .chart-card canvas {
        height: 170px !important;
        max-height: 170px !important;
    }"""
)

# Móvil muy pequeño
if "@media (max-width: 420px)" not in text:
    text = text.replace(
        "</style>",
"""@media (max-width: 420px) {
    .chart-card {
        height: 210px;
        min-height: 210px;
    }

    .chart-card canvas {
        height: 150px !important;
        max-height: 150px !important;
    }
}
</style>"""
    )

p.write_text(text, encoding="utf-8")
print("OK: gráficos ajustados y responsive móvil aplicado")
