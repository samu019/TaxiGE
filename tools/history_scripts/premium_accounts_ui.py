from pathlib import Path

base_css = r"""
<style>
:root{
    --dark:#020617;
    --dark2:#0f172a;
    --gold:#f59e0b;
    --gold2:#facc15;
    --muted:#64748b;
    --soft:#f8fafc;
    --border:#e5e7eb;
    --danger:#991b1b;
}
*{box-sizing:border-box}
body{
    margin:0;
    font-family:Arial,sans-serif;
    background:
        radial-gradient(circle at 12% 8%, rgba(245,158,11,.24), transparent 28%),
        radial-gradient(circle at 82% 12%, rgba(59,130,246,.14), transparent 28%),
        linear-gradient(135deg,#020617,#111827);
    color:#111827;
    min-height:100vh;
}
a{text-decoration:none}
.nav{
    width:min(1180px,calc(100% - 32px));
    margin:0 auto;
    padding:22px 0;
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:14px;
}
.brand{
    display:flex;
    align-items:center;
    gap:12px;
    color:white;
    font-size:22px;
    font-weight:900;
}
.logo{
    width:46px;
    height:46px;
    border-radius:16px;
    background:linear-gradient(135deg,var(--gold),var(--gold2));
    color:#111827;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:900;
    box-shadow:0 14px 34px rgba(245,158,11,.30);
}
.nav-link{
    color:white;
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.16);
    padding:12px 16px;
    border-radius:999px;
    font-weight:900;
}
.shell{
    width:min(1180px,calc(100% - 32px));
    margin:0 auto;
    min-height:calc(100vh - 94px);
    display:grid;
    grid-template-columns:.9fr 1.1fr;
    gap:38px;
    align-items:center;
    padding:28px 0 70px;
}
.copy{color:white}
.badge{
    display:inline-block;
    padding:9px 13px;
    border-radius:999px;
    background:rgba(245,158,11,.16);
    border:1px solid rgba(245,158,11,.35);
    color:#fde68a;
    font-weight:900;
    margin-bottom:18px;
}
.copy h1{
    font-size:clamp(36px,5vw,62px);
    line-height:.97;
    letter-spacing:-.06em;
    margin:0 0 18px;
}
.copy p{
    color:#cbd5e1;
    line-height:1.7;
    font-size:18px;
    max-width:620px;
}
.panel-card{
    background:rgba(255,255,255,.96);
    border:1px solid rgba(255,255,255,.75);
    border-radius:30px;
    padding:30px;
    box-shadow:0 30px 90px rgba(0,0,0,.34);
}
.panel-card h2{
    font-size:30px;
    margin:0 0 8px;
    letter-spacing:-.04em;
}
.subtitle{
    color:var(--muted);
    margin-bottom:22px;
    line-height:1.6;
}
.grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:16px;
}
.full{grid-column:span 2}
label{
    display:block;
    font-size:14px;
    font-weight:900;
    margin-bottom:7px;
}
input,select,textarea{
    width:100%;
    padding:14px;
    border:1px solid #d1d5db;
    border-radius:15px;
    background:#f8fafc;
    font-size:15px;
    transition:.16s ease;
}
input:focus,select:focus,textarea:focus{
    outline:4px solid rgba(245,158,11,.20);
    border-color:var(--gold);
    background:white;
}
input[type=file]{
    background:white;
    padding:11px;
}
.error{
    color:var(--danger);
    margin-top:6px;
    font-size:13px;
    font-weight:800;
}
.notice{
    background:#fef3c7;
    color:#92400e;
    border-radius:17px;
    padding:14px;
    font-weight:800;
    line-height:1.5;
    margin-bottom:18px;
}
.btn{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    width:100%;
    border:0;
    border-radius:16px;
    padding:15px 18px;
    font-weight:900;
    cursor:pointer;
    font-size:15px;
    text-align:center;
}
.btn-primary{
    background:linear-gradient(135deg,var(--gold),var(--gold2));
    color:#111827;
    box-shadow:0 18px 34px rgba(245,158,11,.24);
}
.btn-dark{
    background:#111827;
    color:white;
}
.bottom-link{
    text-align:center;
    margin-top:16px;
    color:var(--muted);
}
.bottom-link a{
    color:#111827;
    font-weight:900;
}
.steps{
    display:grid;
    gap:12px;
    margin-top:26px;
    max-width:560px;
}
.step{
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.14);
    border-radius:18px;
    padding:16px;
    color:#e5e7eb;
}
.step strong{color:white}
.section-title{
    margin:24px 0 14px;
    padding:13px 15px;
    border-radius:17px;
    background:#f8fafc;
    color:#334155;
    font-weight:900;
}
.choice-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:22px;
}
.choice-card{
    background:rgba(255,255,255,.09);
    border:1px solid rgba(255,255,255,.16);
    border-radius:28px;
    padding:30px;
    color:white;
    box-shadow:0 24px 70px rgba(0,0,0,.28);
    backdrop-filter:blur(14px);
}
.choice-card h2{font-size:30px;margin:0 0 12px}
.choice-card p{color:#cbd5e1;line-height:1.7}
.choice-card ul{color:#e5e7eb;line-height:1.9;padding-left:20px}
.choice-btn{
    display:block;
    text-align:center;
    margin-top:22px;
    padding:15px;
    border-radius:16px;
    font-weight:900;
}
.choice-btn-user{background:white;color:#111827}
.choice-btn-owner{background:linear-gradient(135deg,var(--gold),var(--gold2));color:#111827}
.kyc-container{
    width:min(1120px,calc(100% - 32px));
    margin:0 auto 60px;
    padding-top:20px;
}
.kyc-card{
    background:white;
    border-radius:30px;
    padding:30px;
    box-shadow:0 30px 90px rgba(15,23,42,.20);
}
@media(max-width:900px){
    .shell{grid-template-columns:1fr;padding-top:14px}
    .choice-grid{grid-template-columns:1fr}
}
@media(max-width:640px){
    .nav{align-items:flex-start;flex-direction:column}
    .brand{font-size:19px}
    .logo{width:42px;height:42px}
    .nav-link{width:100%;text-align:center}
    .panel-card,.kyc-card{padding:22px;border-radius:24px}
    .grid{grid-template-columns:1fr}
    .full{grid-column:span 1}
    .copy h1{font-size:38px}
    .copy p{font-size:16px}
}
</style>
"""

# LOGIN
Path("templates/accounts/login.html").write_text(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Iniciar sesión - TaxiGE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{base_css}
</head>
<body>
<nav class="nav">
    <a class="brand" href="/"><span class="logo">TG</span>TaxiGE Platform</a>
    <a class="nav-link" href="/accounts/register/">Crear cuenta</a>
</nav>
<div class="shell">
    <section class="copy">
        <div class="badge">Acceso seguro</div>
        <h1>Entra a tu panel privado de gestión.</h1>
        <p>Los propietarios aprobados acceden al panel. El superusuario accede al panel principal de administración.</p>
        <div class="steps">
            <div class="step"><strong>Propietario:</strong> gestión de taxis, conductores, pagos y daños.</div>
            <div class="step"><strong>Superusuario:</strong> auditoría y aprobación de solicitudes KYC.</div>
        </div>
    </section>
    <section class="panel-card">
        <h2>Iniciar sesión</h2>
        <div class="subtitle">Introduce tus credenciales para continuar.</div>
        {{% if form.errors %}}<div class="notice">Usuario o contraseña incorrectos.</div>{{% endif %}}
        <form method="post">
            {{% csrf_token %}}
            <div class="grid">
                <div class="full"><label>Usuario</label>{{{{ form.username }}}}</div>
                <div class="full"><label>Contraseña</label>{{{{ form.password }}}}</div>
            </div>
            <button class="btn btn-dark" type="submit" style="margin-top:20px;">Entrar</button>
        </form>
        <div class="bottom-link">¿No tienes cuenta? <a href="/accounts/register/">Registrarte</a></div>
    </section>
</div>
</body>
</html>""", encoding="utf-8")

# REGISTER CHOICE
Path("templates/accounts/register_choice.html").write_text(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Elegir tipo de cuenta - TaxiGE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{base_css}
</head>
<body>
<nav class="nav">
    <a class="brand" href="/"><span class="logo">TG</span>TaxiGE Platform</a>
    <a class="nav-link" href="/accounts/login/">Iniciar sesión</a>
</nav>
<div style="width:min(1100px,calc(100% - 32px));margin:0 auto;padding:44px 0 70px;">
    <div style="text-align:center;color:white;margin-bottom:34px;">
        <div class="badge">Registro inteligente</div>
        <h1 style="font-size:clamp(36px,5vw,62px);line-height:.98;letter-spacing:-.06em;margin:0 0 14px;">Elige tu tipo de cuenta</h1>
        <p style="color:#cbd5e1;font-size:18px;">TaxiGE separa usuarios normales y propietarios para proteger la plataforma.</p>
    </div>
    <div class="choice-grid">
        <div class="choice-card">
            <div class="badge">Cuenta pública</div>
            <h2>Usuario normal</h2>
            <p>Para ver opciones públicas y futuras funciones de cliente.</p>
            <ul>
                <li>Registro inmediato</li>
                <li>Sin acceso a editar taxis</li>
                <li>No entra al panel de propietarios</li>
            </ul>
            <a class="choice-btn choice-btn-user" href="/accounts/register/user/">Crear cuenta normal</a>
        </div>
        <div class="choice-card">
            <div class="badge">KYC obligatorio</div>
            <h2>Propietario de taxi</h2>
            <p>Para dueños o empresas que necesitan gestionar taxis, conductores, pagos y daños.</p>
            <ul>
                <li>Datos personales</li>
                <li>Documentos KYC</li>
                <li>Documentos del taxi</li>
                <li>Aprobación manual</li>
            </ul>
            <a class="choice-btn choice-btn-owner" href="/accounts/register/owner/">Solicitar cuenta de propietario</a>
        </div>
    </div>
</div>
</body>
</html>""", encoding="utf-8")

# USER REGISTER
Path("templates/accounts/register.html").write_text(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Crear cuenta normal - TaxiGE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{base_css}
</head>
<body>
<nav class="nav">
    <a class="brand" href="/"><span class="logo">TG</span>TaxiGE</a>
    <a class="nav-link" href="/accounts/login/">Iniciar sesión</a>
</nav>
<div class="shell">
    <section class="copy">
        <div class="badge">Usuario normal</div>
        <h1>Crea tu cuenta pública en TaxiGE.</h1>
        <p>Esta cuenta no permite editar taxis. Para administrar taxis debes solicitar cuenta de propietario con KYC.</p>
        <div class="steps">
            <div class="step"><strong>Acceso público:</strong> pensado para usuarios normales.</div>
            <div class="step"><strong>Seguridad:</strong> sin permisos administrativos.</div>
        </div>
    </section>
    <section class="panel-card">
        <h2>Crear cuenta</h2>
        <div class="subtitle">Completa tus datos principales.</div>
        <form method="post">
            {{% csrf_token %}}
            <div class="grid">
                {{% for field in form %}}
                <div class="{{% if field.name == 'email' or field.name == 'password' or field.name == 'password_confirm' %}}full{{% endif %}}">
                    <label>{{{{ field.label }}}}</label>
                    {{{{ field }}}}
                    {{% for error in field.errors %}}<div class="error">{{{{ error }}}}</div>{{% endfor %}}
                </div>
                {{% endfor %}}
            </div>
            {{% for error in form.non_field_errors %}}<div class="error">{{{{ error }}}}</div>{{% endfor %}}
            <button class="btn btn-primary" type="submit" style="margin-top:20px;">Crear cuenta normal</button>
        </form>
        <div class="bottom-link">¿Eres propietario? <a href="/accounts/register/owner/">Solicitar cuenta KYC</a></div>
    </section>
</div>
</body>
</html>""", encoding="utf-8")

# OWNER KYC
Path("templates/accounts/register_owner_kyc.html").write_text(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Registro propietario KYC - TaxiGE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{base_css}
</head>
<body>
<nav class="nav">
    <a class="brand" href="/"><span class="logo">TG</span>TaxiGE Platform</a>
    <a class="nav-link" href="/accounts/login/">Iniciar sesión</a>
</nav>
<div style="width:min(1120px,calc(100% - 32px));margin:0 auto;padding:34px 0 20px;color:white;">
    <div class="badge">KYC obligatorio</div>
    <h1 style="font-size:clamp(34px,5vw,58px);line-height:.98;letter-spacing:-.06em;margin:0 0 12px;">Solicitud de propietario de taxi</h1>
    <p style="color:#cbd5e1;font-size:18px;line-height:1.7;max-width:780px;">Completa tus datos personales, documentos KYC y documentos del taxi. Tu cuenta quedará pendiente hasta revisión.</p>
</div>
<div class="kyc-container">
    <div class="kyc-card">
        <div class="notice">Enviar esta solicitud no activa el panel automáticamente. TaxiGE revisará tu identidad y documentos.</div>
        <form method="post" enctype="multipart/form-data">
            {{% csrf_token %}}
            {{% for error in form.non_field_errors %}}<div class="error">{{{{ error }}}}</div>{{% endfor %}}

            <div class="section-title">1. Datos de cuenta</div>
            <div class="grid">
                <div><label>{{{{ form.username.label }}}}</label>{{{{ form.username }}}}{{% for e in form.username.errors %}}<div class="error">{{{{ e }}}}</div>{{% endfor %}}</div>
                <div><label>{{{{ form.email.label }}}}</label>{{{{ form.email }}}}{{% for e in form.email.errors %}}<div class="error">{{{{ e }}}}</div>{{% endfor %}}</div>
                <div><label>{{{{ form.password.label }}}}</label>{{{{ form.password }}}}{{% for e in form.password.errors %}}<div class="error">{{{{ e }}}}</div>{{% endfor %}}</div>
                <div><label>{{{{ form.password_confirm.label }}}}</label>{{{{ form.password_confirm }}}}{{% for e in form.password_confirm.errors %}}<div class="error">{{{{ e }}}}</div>{{% endfor %}}</div>
                <div><label>{{{{ form.first_name.label }}}}</label>{{{{ form.first_name }}}}</div>
                <div><label>{{{{ form.last_name.label }}}}</label>{{{{ form.last_name }}}}</div>
                <div><label>{{{{ form.user_phone.label }}}}</label>{{{{ form.user_phone }}}}</div>
            </div>

            <div class="section-title">2. Identificación del propietario</div>
            <div class="grid">
                <div><label>{{{{ form.owner_full_name.label }}}}</label>{{{{ form.owner_full_name }}}}</div>
                <div><label>{{{{ form.phone.label }}}}</label>{{{{ form.phone }}}}</div>
                <div><label>{{{{ form.city.label }}}}</label>{{{{ form.city }}}}</div>
                <div><label>{{{{ form.address.label }}}}</label>{{{{ form.address }}}}</div>
                <div><label>{{{{ form.identity_number.label }}}}</label>{{{{ form.identity_number }}}}</div>
                <div><label>{{{{ form.identity_document.label }}}}</label>{{{{ form.identity_document }}}}</div>
                <div><label>{{{{ form.selfie_photo.label }}}}</label>{{{{ form.selfie_photo }}}}</div>
            </div>

            <div class="section-title">3. Empresa o flota</div>
            <div class="grid">
                <div><label>{{{{ form.company_name.label }}}}</label>{{{{ form.company_name }}}}</div>
                <div><label>{{{{ form.taxi_count.label }}}}</label>{{{{ form.taxi_count }}}}</div>
            </div>

            <div class="section-title">4. Taxi principal de verificación</div>
            <div class="grid">
                <div><label>{{{{ form.main_taxi_brand.label }}}}</label>{{{{ form.main_taxi_brand }}}}</div>
                <div><label>{{{{ form.main_taxi_model.label }}}}</label>{{{{ form.main_taxi_model }}}}</div>
                <div><label>{{{{ form.main_taxi_plate.label }}}}</label>{{{{ form.main_taxi_plate }}}}</div>
                <div><label>{{{{ form.main_taxi_color.label }}}}</label>{{{{ form.main_taxi_color }}}}</div>
                <div><label>{{{{ form.taxi_registration_document.label }}}}</label>{{{{ form.taxi_registration_document }}}}</div>
                <div><label>{{{{ form.taxi_license_document.label }}}}</label>{{{{ form.taxi_license_document }}}}</div>
                <div><label>{{{{ form.ownership_proof_document.label }}}}</label>{{{{ form.ownership_proof_document }}}}</div>
            </div>

            <div class="section-title">5. Mensaje adicional</div>
            <div><label>{{{{ form.message.label }}}}</label>{{{{ form.message }}}}</div>

            <button class="btn btn-primary" type="submit" style="margin-top:24px;">Enviar solicitud KYC</button>
        </form>
    </div>
</div>
</body>
</html>""", encoding="utf-8")

# REQUEST ADMIN SIMPLE
Path("templates/accounts/request_admin.html").write_text(f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Solicitar acceso - TaxiGE</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{base_css}
</head>
<body>
<nav class="nav">
    <a class="brand" href="/"><span class="logo">TG</span>TaxiGE Platform</a>
    <a class="nav-link" href="/accounts/logout/">Salir</a>
</nav>
<div class="shell">
    <section class="copy">
        <div class="badge">Solicitud pendiente</div>
        <h1>Solicita acceso como propietario.</h1>
        <p>Tu cuenta normal está creada. Envía los datos básicos para que TaxiGE revise tu solicitud.</p>
    </section>
    <section class="panel-card">
        <h2>Solicitud de propietario</h2>
        <div class="subtitle">Completa la información de tu empresa o flota.</div>
        {{% if existing_request %}}<div class="notice">Ya tienes una solicitud pendiente. Debes esperar revisión.</div>{{% else %}}
        <form method="post" enctype="multipart/form-data">
            {{% csrf_token %}}
            <div class="grid">
                {{% for field in form %}}
                <div class="{{% if field.name == 'message' %}}full{{% endif %}}">
                    <label>{{{{ field.label }}}}</label>
                    {{{{ field }}}}
                    {{% for error in field.errors %}}<div class="error">{{{{ error }}}}</div>{{% endfor %}}
                </div>
                {{% endfor %}}
            </div>
            <button class="btn btn-primary" type="submit" style="margin-top:20px;">Enviar solicitud</button>
        </form>
        {{% endif %}}
    </section>
</div>
</body>
</html>""", encoding="utf-8")

print("OK: UI premium aplicada a cuentas y KYC")
