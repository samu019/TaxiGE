from pathlib import Path
import re

p = Path("templates/accounts/register.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# Reemplazar medidor simple por medidor visual
text = text.replace(
    '<div id="password-meter" class="password-meter">Seguridad: pendiente</div>',
    '''
<div class="password-strength-box">
    <div class="strength-top">
        <span>🔐 Seguridad de la contraseña</span>
        <strong id="password-strength-label">Pendiente</strong>
    </div>
    <div class="strength-bar">
        <div id="password-strength-fill"></div>
    </div>
    <ul class="password-rules">
        <li id="rule-length">Mínimo 8 caracteres</li>
        <li id="rule-upper">Una letra mayúscula</li>
        <li id="rule-lower">Una letra minúscula</li>
        <li id="rule-number">Un número</li>
    </ul>
</div>
'''
)

css = r'''
.password-strength-box{
    margin-top:10px;
    padding:14px;
    border-radius:16px;
    background:#f8fafc;
    border:1px solid #cbd5e1;
}
.strength-top{
    display:flex;
    justify-content:space-between;
    gap:10px;
    align-items:center;
    font-size:13px;
    font-weight:900;
    color:#0f172a;
}
#password-strength-label{
    color:#64748b;
}
.strength-bar{
    margin-top:10px;
    width:100%;
    height:9px;
    border-radius:999px;
    background:#e2e8f0;
    overflow:hidden;
}
#password-strength-fill{
    width:0%;
    height:100%;
    border-radius:999px;
    background:#94a3b8;
    transition:width .25s ease, background .25s ease;
}
.password-rules{
    margin:12px 0 0;
    padding-left:18px;
    display:grid;
    gap:5px;
    font-size:13px;
    color:#64748b;
    font-weight:700;
}
.password-rules li.ok{
    color:#059669;
}
.password-rules li.ok::marker{
    content:"✓ ";
}
'''

if ".password-strength-box" not in text:
    text = text.replace("</style>", css + "\n</style>", 1)

# Reemplazar script antiguo del medidor
text = re.sub(
    r"const passwordField = document\.getElementById\('id_password'\);.*?evaluate\(\);\s*\}\s*\}\);",
    r"""const passwordField = document.getElementById('id_password');
    const label = document.getElementById('password-strength-label');
    const fill = document.getElementById('password-strength-fill');
    const rules = {
        length: document.getElementById('rule-length'),
        upper: document.getElementById('rule-upper'),
        lower: document.getElementById('rule-lower'),
        number: document.getElementById('rule-number')
    };

    if (passwordField && label && fill) {
        function setRule(el, ok) {
            if (!el) return;
            el.classList.toggle('ok', ok);
        }

        function evaluate() {
            const v = passwordField.value;
            const checks = {
                length: v.length >= 8,
                upper: /[A-Z]/.test(v),
                lower: /[a-z]/.test(v),
                number: /[0-9]/.test(v)
            };

            setRule(rules.length, checks.length);
            setRule(rules.upper, checks.upper);
            setRule(rules.lower, checks.lower);
            setRule(rules.number, checks.number);

            const score = Object.values(checks).filter(Boolean).length;

            if (!v) {
                label.textContent = 'Pendiente';
                label.style.color = '#64748b';
                fill.style.width = '0%';
                fill.style.background = '#94a3b8';
            } else if (score <= 1) {
                label.textContent = 'Débil';
                label.style.color = '#dc2626';
                fill.style.width = '25%';
                fill.style.background = '#dc2626';
            } else if (score <= 3) {
                label.textContent = 'Media';
                label.style.color = '#d97706';
                fill.style.width = '65%';
                fill.style.background = '#f59e0b';
            } else {
                label.textContent = 'Fuerte';
                label.style.color = '#059669';
                fill.style.width = '100%';
                fill.style.background = '#22c55e';
            }
        }

        passwordField.addEventListener('input', evaluate);
        evaluate();
    }
});""",
    text,
    flags=re.DOTALL
)

p.write_text(text, encoding="utf-8")
print("Medidor visual de contraseña actualizado.")
