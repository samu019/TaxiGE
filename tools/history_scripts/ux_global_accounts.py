from pathlib import Path

files = [
    "templates/accounts/login.html",
    "templates/accounts/register.html",
    "templates/accounts/register_choice.html",
    "templates/accounts/register_owner_kyc.html",
    "templates/accounts/request_admin.html",
]

extra_css = r"""
<style>
/* UX GLOBAL PREMIUM TAXIGE */
html {
    scroll-behavior: smooth;
}

body {
    -webkit-font-smoothing: antialiased;
}

button,
a,
input,
select,
textarea {
    -webkit-tap-highlight-color: transparent;
}

.btn,
.choice-btn,
.nav-link,
.login-link,
.submit {
    transition: transform .18s ease, box-shadow .18s ease, opacity .18s ease;
}

.btn:hover,
.choice-btn:hover,
.nav-link:hover,
.login-link:hover,
.submit:hover {
    transform: translateY(-1px);
    opacity: .96;
}

.btn:active,
.choice-btn:active,
.nav-link:active,
.login-link:active,
.submit:active {
    transform: scale(.98);
}

input,
select,
textarea {
    min-height: 48px;
}

textarea {
    resize: vertical;
}

input[type="file"] {
    cursor: pointer;
}

.form-help,
.help-text {
    display: block;
    margin-top: 6px;
    color: #64748b;
    font-size: 13px;
    line-height: 1.4;
}

.secure-note {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    background: #ecfdf5;
    color: #065f46;
    padding: 14px;
    border-radius: 16px;
    font-size: 14px;
    font-weight: 800;
    line-height: 1.5;
    margin-top: 16px;
}

.back-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #e5e7eb;
    font-weight: 900;
    margin-bottom: 18px;
}

.progress-box {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 22px;
}

.progress-step {
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.14);
    border-radius: 18px;
    padding: 14px;
    color: #e5e7eb;
    font-size: 14px;
    line-height: 1.4;
}

.progress-step strong {
    display: block;
    color: #ffffff;
    margin-bottom: 5px;
}

.mobile-only {
    display: none;
}

@media(max-width:760px) {
    .shell {
        gap: 20px !important;
        padding-bottom: 36px !important;
    }

    .copy {
        text-align: left;
    }

    .copy h1 {
        font-size: 34px !important;
        letter-spacing: -.045em !important;
    }

    .copy p {
        font-size: 15px !important;
    }

    .panel-card,
    .kyc-card,
    .choice-card {
        border-radius: 22px !important;
        padding: 20px !important;
    }

    .badge {
        font-size: 13px;
    }

    .progress-box {
        grid-template-columns: 1fr;
    }

    .desktop-only {
        display: none !important;
    }

    .mobile-only {
        display: block;
    }

    input,
    select,
    textarea {
        font-size: 16px !important;
    }

    .btn,
    .choice-btn,
    .submit {
        min-height: 50px;
    }
}
</style>
"""

for file in files:
    p = Path(file)
    text = p.read_text(encoding="utf-8")

    if "UX GLOBAL PREMIUM TAXIGE" not in text:
        text = text.replace("</head>", extra_css + "\n</head>")

    text = text.replace(
        '<a class="brand" href="/"><span class="logo">TG</span>TaxiGE Platform</a>',
        '<a class="brand" href="/"><span class="logo">TG</span>TaxiGE Platform</a>'
    )

    p.write_text(text, encoding="utf-8")
    print("OK UX:", file)

print("OK: mejora global UI/UX aplicada")
