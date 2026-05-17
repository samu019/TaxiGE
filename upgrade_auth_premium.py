from pathlib import Path

# =========================
# REGISTER.HTML
# =========================
p = Path("templates/accounts/register.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

# CSS adicional
extra_css = """
.password-tools{
    display:flex;
    justify-content:flex-end;
    margin-top:6px;
}
.toggle-password{
    border:0;
    background:none;
    color:#2563eb;
    font-weight:800;
    cursor:pointer;
    font-size:13px;
}
.password-meter{
    margin-top:8px;
    padding:10px 12px;
    border-radius:12px;
    background:#f8fafc;
    border:1px solid #cbd5e1;
    font-size:13px;
    font-weight:800;
}
.password-meter.weak{color:#dc2626;}
.password-meter.medium{color:#d97706;}
.password-meter.strong{color:#059669;}
.terms-box{
    margin-top:18px;
    padding:14px 16px;
    border-radius:16px;
    background:#f8fafc;
    border:1px solid #cbd5e1;
}
.terms-box label{
    display:flex;
    align-items:flex-start;
    gap:10px;
    font-weight:700;
    color:#0f172a;
    line-height:1.6;
}
.terms-box input{
    margin-top:4px;
}
"""

if ".password-tools" not in text:
    text = text.replace("</style>", extra_css + "\n</style>", 1)

# Añadir botones de mostrar contraseña
text = text.replace(
    "{{ form.password }}\n                            {{ form.password.errors }}",
    """{{ form.password }}
                            <div class="password-tools">
                                <button type="button" class="toggle-password" data-target="{{ form.password.id_for_label }}">👁️ Mostrar contraseña</button>
                            </div>
                            <div id="password-meter" class="password-meter">Seguridad: pendiente</div>
                            {{ form.password.errors }}"""
)

text = text.replace(
    "{{ form.password_confirm }}\n                            {{ form.password_confirm.errors }}",
    """{{ form.password_confirm }}
                            <div class="password-tools">
                                <button type="button" class="toggle-password" data-target="{{ form.password_confirm.id_for_label }}">👁️ Mostrar contraseña</button>
                            </div>
                            {{ form.password_confirm.errors }}"""
)

# Añadir términos antes del botón
text = text.replace(
    '<button type="submit" class="submit-btn">🚀 Crear cuenta normal</button>',
    """
                    <div class="terms-box">
                        <label>
                            <input type="checkbox" id="accept-terms" required>
                            <span>He leído y acepto los términos y condiciones de TaxiGE.</span>
                        </label>
                    </div>

                    <button type="submit" class="submit-btn">🚀 Crear cuenta normal</button>
"""
)

# JavaScript
script = """
<script>
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.toggle-password').forEach(function(btn){
        btn.addEventListener('click', function(){
            const field = document.getElementById(btn.dataset.target);
            if (!field) return;
            if (field.type === 'password') {
                field.type = 'text';
                btn.textContent = '🙈 Ocultar contraseña';
            } else {
                field.type = 'password';
                btn.textContent = '👁️ Mostrar contraseña';
            }
        });
    });

    const passwordField = document.getElementById('id_password');
    const meter = document.getElementById('password-meter');

    if (passwordField && meter) {
        function evaluate() {
            const v = passwordField.value;
            let score = 0;
            if (v.length >= 8) score++;
            if (/[A-Z]/.test(v)) score++;
            if (/[a-z]/.test(v)) score++;
            if (/[0-9]/.test(v)) score++;
            if (/[^A-Za-z0-9]/.test(v)) score++;

            meter.className = 'password-meter';

            if (!v) {
                meter.textContent = 'Seguridad: pendiente';
            } else if (score <= 2) {
                meter.classList.add('weak');
                meter.textContent = 'Seguridad: Débil';
            } else if (score <= 4) {
                meter.classList.add('medium');
                meter.textContent = 'Seguridad: Media';
            } else {
                meter.classList.add('strong');
                meter.textContent = 'Seguridad: Fuerte';
            }
        }

        passwordField.addEventListener('input', evaluate);
        evaluate();
    }
});
</script>
"""

if "</body>" in text and "password-meter" in text and "DOMContentLoaded" not in text:
    text = text.replace("</body>", script + "\n</body>", 1)

p.write_text(text, encoding="utf-8")

# =========================
# LOGIN.HTML
# =========================
p = Path("templates/accounts/login.html")
text = p.read_text(encoding="utf-8", errors="replace").replace("\ufeff", "")

if ".password-tools" not in text:
    text = text.replace("</style>", extra_css + "\n</style>", 1)

text = text.replace(
    "{{ form.password }}</div>",
    """{{ form.password }}
                    <div class="password-tools">
                        <button type="button" class="toggle-password" data-target="{{ form.password.id_for_label }}">👁️ Mostrar contraseña</button>
                    </div>
                </div>"""
)

if "</body>" in text and "DOMContentLoaded" not in text:
    login_script = """
<script>
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.toggle-password').forEach(function(btn){
        btn.addEventListener('click', function(){
            const field = document.getElementById(btn.dataset.target);
            if (!field) return;
            if (field.type === 'password') {
                field.type = 'text';
                btn.textContent = '🙈 Ocultar contraseña';
            } else {
                field.type = 'password';
                btn.textContent = '👁️ Mostrar contraseña';
            }
        });
    });
});
</script>
"""
    text = text.replace("</body>", login_script + "\n</body>", 1)

p.write_text(text, encoding="utf-8")

print("Registro y login premium actualizados.")
