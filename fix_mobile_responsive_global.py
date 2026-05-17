from pathlib import Path

p = Path("templates/dashboard/panel_base.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

css = r'''
<style>
/* TAXIGE GLOBAL MOBILE RESPONSIVE FIX */
@media (max-width: 768px) {
    body {
        overflow-x: hidden !important;
    }

    .panel-layout,
    .dashboard-layout,
    .main-layout,
    .content-layout {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
    }

    aside,
    .sidebar {
        max-width: 100% !important;
    }

    main,
    .main-content,
    .panel-content,
    .content {
        width: 100% !important;
        max-width: 100% !important;
        padding: 14px !important;
        overflow-x: hidden !important;
    }

    h1 {
        font-size: 26px !important;
        line-height: 1.15 !important;
    }

    h2 {
        font-size: 21px !important;
    }

    .stats-grid,
    .cards-grid,
    .dashboard-grid,
    .subscription-grid,
    .subscription-layout,
    .form-grid,
    .payment-info-grid,
    .premium-bank-grid {
        grid-template-columns: 1fr !important;
        width: 100% !important;
    }

    .stat-card,
    .content-card,
    .subscription-card,
    .subscription-panel,
    .premium-info-card,
    .form-field,
    .box,
    .card {
        width: 100% !important;
        max-width: 100% !important;
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
    }

    table {
        min-width: 720px;
    }

    .table-responsive,
    .subscription-table-wrap {
        width: 100% !important;
        overflow-x: auto !important;
        -webkit-overflow-scrolling: touch !important;
    }

    input,
    textarea,
    select,
    button,
    .btn,
    .subscription-btn,
    .submit-btn {
        max-width: 100% !important;
    }

    a {
        overflow-wrap: anywhere !important;
        word-break: break-word !important;
    }
}

/* SHARED ACCESS LINK FIX */
.share-link-box,
.shared-link-box,
.access-link-box,
.invite-link-box,
.copy-link-box {
    width: 100% !important;
    max-width: 100% !important;
    padding: 16px !important;
    border-radius: 18px !important;
    background: rgba(15,23,42,.92) !important;
    border: 1px solid rgba(96,165,250,.28) !important;
    overflow: hidden !important;
}

.share-link-box input,
.shared-link-box input,
.access-link-box input,
.invite-link-box input,
.copy-link-box input,
input[type="url"],
input[readonly] {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: auto !important;
    white-space: nowrap !important;
    text-overflow: ellipsis !important;
}

.share-link-box a,
.shared-link-box a,
.access-link-box a,
.invite-link-box a,
.copy-link-box a {
    display: block !important;
    width: 100% !important;
    overflow-wrap: anywhere !important;
    word-break: break-all !important;
    color: #60a5fa !important;
    font-weight: 800 !important;
}

@media (max-width: 768px) {
    .share-actions,
    .shared-actions,
    .copy-actions,
    .invite-actions {
        display: grid !important;
        grid-template-columns: 1fr !important;
        gap: 10px !important;
    }

    .share-actions button,
    .shared-actions button,
    .copy-actions button,
    .invite-actions button {
        width: 100% !important;
    }
}
</style>
'''

if "TAXIGE GLOBAL MOBILE RESPONSIVE FIX" not in text:
    if "</head>" in text:
        text = text.replace("</head>", css + "\n</head>", 1)
    else:
        text = css + "\n" + text

p.write_text(text, encoding="utf-8")
print("Responsive móvil global y enlaces compartidos ajustados.")
