"""The whole design system in one place.

Design tokens (colours, fonts, radii) are CSS variables at the top of CSS.
Change --accent and the entire site follows.

Specificity note: Streamlit ships its own styles for p / h1 / a / ul. Every rule below is
prefixed with `.stApp .yp` (my wrapper class) so it wins, and the resets use :where() so they
carry no extra specificity and my own classes can still override them.
"""

CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600&family=Geist+Mono:wght@400;500&display=swap');

:root{
  --bg:#0d0e12; --bg-2:#111319; --surface:#151820; --surface-2:#1b1f28;
  --line:#252934; --line-2:#333947;
  --text:#eceef3; --muted:#9298a6; --dim:#6b7180;
  --accent:#7c8cff; --accent-btn:#5a67ee; --accent-btn-hover:#6e7bff;
  --accent-soft:rgba(124,140,255,.11); --accent-line:rgba(124,140,255,.34);
  --font:'Geist',ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
  --mono:'Geist Mono',ui-monospace,'SF Mono',Menlo,Consolas,monospace;
  --ease:cubic-bezier(.2,.7,.2,1);
}

/* ---------- 1. Make Streamlit disappear --------------------------------------------- */
html,body,.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"],section.main,.main{
  background:var(--bg)!important; scroll-behavior:smooth; overflow-x:hidden;
}
header[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],
[data-testid="stStatusWidget"],[data-testid="stSidebar"],[data-testid="collapsedControl"],
[data-testid="stSidebarCollapsedControl"],#MainMenu,footer{display:none!important}
.block-container,[data-testid="stMainBlockContainer"]{padding:0!important;max-width:100%!important}
[data-testid="stVerticalBlock"]{gap:0!important}
[data-testid="stElementContainer"],.element-container{margin:0!important;width:100%!important}
[data-testid="stMarkdownContainer"]{width:100%}
iframe[height="0"]{position:absolute;width:0;height:0;border:0}
div:has(> iframe[height="0"]){height:0!important;min-height:0!important;margin:0!important;overflow:hidden}

/* ---------- 2. Base + resets ---------------------------------------------------------- */
.stApp .yp{font-family:var(--font);color:var(--text);line-height:1.6;font-size:16px;
  -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;overflow-x:clip}
.stApp .yp *,.stApp .yp *::before,.stApp .yp *::after{box-sizing:border-box}
.stApp .yp :where(h1,h2,h3,h4,p,ul,ol,li,figure,small,span,strong,b,article,section,nav){
  font-family:var(--font);margin:0;padding:0;color:inherit;letter-spacing:inherit}
.stApp .yp :where(ul,ol){list-style:none}
.stApp .yp :where(a){color:inherit;text-decoration:none;border:0}
.stApp .yp :where(img,svg){max-width:100%;display:block}
.stApp .yp a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:8px}
.stApp .yp ::selection{background:rgba(124,140,255,.35)}

.stApp .yp .wrap{max-width:1160px;margin:0 auto;padding:0 clamp(20px,5vw,48px)}
.stApp .yp .sec{position:relative;padding:clamp(72px,10vw,132px) 0;scroll-margin-top:60px}
.stApp .yp .sec-head{max-width:860px;margin-bottom:clamp(32px,5vw,56px)}
.stApp .yp .sec-title{font-size:clamp(2rem,4.6vw,3.35rem);line-height:1.05;letter-spacing:-.035em;font-weight:600}
.stApp .yp .sec-sub{margin-top:14px;color:var(--muted);font-size:1.05rem;max-width:56ch}
.stApp .yp .eyebrow{font-family:var(--mono);font-size:.74rem;letter-spacing:.14em;color:var(--accent);
  text-transform:uppercase;margin-bottom:18px}

/* buttons */
.stApp .yp .btn-row{display:flex;flex-wrap:wrap;gap:12px}
.stApp .yp .btn{display:inline-flex;align-items:center;justify-content:center;gap:.55rem;padding:.85rem 1.4rem;
  border-radius:10px;font-weight:500;font-size:.95rem;line-height:1;cursor:pointer;
  border:1px solid transparent;transition:transform .25s var(--ease),background .25s,border-color .25s,box-shadow .25s}
.stApp .yp .btn-primary{background:var(--accent-btn);color:#fff}
.stApp .yp .btn-primary:hover{background:var(--accent-btn-hover);transform:translateY(-2px);
  box-shadow:0 10px 30px -10px rgba(110,123,255,.75)}
.stApp .yp .btn-ghost{border-color:var(--line-2);background:rgba(255,255,255,.02);color:var(--text)}
.stApp .yp .btn-ghost:hover{border-color:var(--accent-line);background:var(--accent-soft);transform:translateY(-2px)}
.stApp .yp .btn-off{border:1px dashed var(--line-2);color:var(--dim);cursor:not-allowed}
.stApp .yp .btn .arr{display:inline-block;transition:transform .25s var(--ease)}
.stApp .yp .btn:hover .arr,.stApp .yp .link-arrow:hover .arr{transform:translateX(4px)}

/* chips */
.stApp .yp .chips{display:flex;flex-wrap:wrap;gap:8px}
.stApp .yp .chip{display:inline-flex;align-items:center;gap:.5rem;padding:.34rem .72rem;border:1px solid var(--line);
  border-radius:8px;background:var(--surface);color:var(--muted);font-size:.84rem;line-height:1.3;
  transition:border-color .25s,color .25s}
.stApp .yp .chip:hover{border-color:var(--line-2);color:var(--text)}
.stApp .yp .chip.used::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--accent);flex:none}
.stApp .yp .chip.tech{font-family:var(--mono);font-size:.76rem;color:var(--accent);border-color:var(--accent-line);
  background:var(--accent-soft)}
.stApp .yp .chip.big{font-size:.95rem;padding:.5rem .95rem;color:var(--text)}

/* ---------- 3. Navigation ------------------------------------------------------------- */
.stApp .yp .nav{position:fixed;top:0;left:0;right:0;z-index:900;background:rgba(13,14,18,.72);
  -webkit-backdrop-filter:blur(14px) saturate(1.2);backdrop-filter:blur(14px) saturate(1.2);
  border-bottom:1px solid rgba(255,255,255,.06)}
.stApp .yp .nav-in{max-width:1160px;margin:0 auto;padding:0 clamp(16px,5vw,48px);height:60px;display:flex;
  align-items:center;justify-content:space-between;gap:12px}
.stApp .yp .brand{font-weight:600;letter-spacing:-.02em;white-space:nowrap}
.stApp .yp .brand .short{display:none}
.stApp .yp .nav-links{display:flex;gap:2px;overflow-x:auto;scrollbar-width:none}
.stApp .yp .nav-links::-webkit-scrollbar{display:none}
.stApp .yp .nav-links a{padding:.45rem .8rem;border-radius:8px;font-size:.9rem;color:var(--muted);white-space:nowrap;
  transition:color .2s,background .2s}
.stApp .yp .nav-links a:hover{color:var(--text);background:rgba(255,255,255,.05)}
.stApp .yp .nav-links a.active{color:var(--accent)}

/* ---------- 4. Hero ------------------------------------------------------------------- */
.stApp .yp .hero{position:relative;min-height:100vh;min-height:100svh;display:flex;align-items:center;
  padding:110px 0 96px;overflow:hidden;scroll-margin-top:0}
.stApp .yp .hero-bg{position:absolute;inset:0;pointer-events:none}
.stApp .yp .grid-wrap{position:absolute;inset:0;overflow:hidden;
  -webkit-mask-image:radial-gradient(ellipse 75% 65% at 65% 40%,#000 15%,transparent 72%);
  mask-image:radial-gradient(ellipse 75% 65% at 65% 40%,#000 15%,transparent 72%)}
.stApp .yp .grid-bg{position:absolute;inset:-56px 0 0 0;opacity:.5;
  background-image:linear-gradient(var(--line) 1px,transparent 1px),linear-gradient(90deg,var(--line) 1px,transparent 1px);
  background-size:56px 56px;animation:gridmove 14s linear infinite}
.stApp .yp .glow{position:absolute;border-radius:50%;filter:blur(90px);will-change:transform}
.stApp .yp .glow.g1{width:520px;height:520px;right:-6%;top:-8%;background:rgba(124,140,255,.30);
  animation:drift 16s ease-in-out infinite alternate}
.stApp .yp .glow.g2{width:420px;height:420px;left:-10%;bottom:-16%;background:rgba(124,140,255,.14);
  animation:drift 20s ease-in-out infinite alternate-reverse}
.stApp .yp .dot{position:absolute;width:3px;height:3px;border-radius:50%;background:var(--accent);opacity:.45;
  animation:floaty 9s ease-in-out infinite}

.stApp .yp .hero-grid{position:relative;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);
  gap:clamp(32px,6vw,88px);align-items:center;width:100%}
.stApp .yp .hero-title{font-size:clamp(3.4rem,9vw,7rem);line-height:.94;letter-spacing:-.05em;font-weight:600}
.stApp .yp .hero-title span{display:block}
.stApp .yp .hero-role{margin-top:18px;font-size:clamp(1.35rem,2.6vw,1.9rem);letter-spacing:-.02em;font-weight:500;
  color:var(--accent)}
.stApp .yp .hero-desc{margin-top:22px;max-width:46ch;color:var(--muted);font-size:clamp(1.02rem,1.5vw,1.2rem)}
.stApp .yp .hero .btn-row{margin-top:32px}
.stApp .yp .social{display:flex;gap:6px;margin-top:22px}
.stApp .yp .social a{width:42px;height:42px;display:grid;place-items:center;border-radius:10px;color:var(--muted);
  border:1px solid var(--line);transition:color .2s,border-color .2s,transform .25s var(--ease),background .2s}
.stApp .yp .social a:hover{color:var(--text);border-color:var(--accent-line);background:var(--accent-soft);transform:translateY(-2px)}
.stApp .yp .chain{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;margin-top:36px;
  font-family:var(--mono);font-size:.74rem;color:var(--dim)}
.stApp .yp .chain i{font-style:normal;color:var(--accent-line)}

.stApp .yp .portrait{position:relative;margin:0;justify-self:end;width:min(100%,430px)}
.stApp .yp .portrait-frame{position:relative;aspect-ratio:4/5;border-radius:20px;overflow:hidden;
  border:1px solid var(--line-2);background:var(--surface);
  box-shadow:0 34px 80px -24px rgba(0,0,0,.8),0 0 90px -34px rgba(124,140,255,.6);
  transition:border-color .4s,box-shadow .4s,transform .5s var(--ease)}
.stApp .yp .portrait:hover .portrait-frame{border-color:var(--accent-line);transform:translateY(-4px);
  box-shadow:0 40px 90px -24px rgba(0,0,0,.85),0 0 110px -30px rgba(124,140,255,.75)}
.stApp .yp .portrait-frame img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;
  transition:transform .9s var(--ease)}
.stApp .yp .portrait:hover img{transform:scale(1.035)}
.stApp .yp .portrait-frame::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,transparent 62%,rgba(13,14,18,.75))}
.stApp .yp .portrait-tag{position:absolute;left:14px;bottom:14px;z-index:2;padding:.4rem .75rem;border-radius:8px;
  font-family:var(--mono);font-size:.72rem;color:var(--text);background:rgba(13,14,18,.6);
  border:1px solid rgba(255,255,255,.1);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px)}
.stApp .yp .portrait-ph{height:100%;display:grid;place-content:center;text-align:center;gap:8px;color:var(--dim);
  font-family:var(--mono);font-size:.8rem;padding:24px}
.stApp .yp .portrait-ph b{font-family:var(--font);font-size:3rem;color:var(--muted);letter-spacing:-.04em}

.stApp .yp .scroll-ind{position:absolute;left:50%;bottom:24px;width:22px;height:36px;margin-left:-11px;
  border:1px solid var(--line-2);border-radius:12px;opacity:.9}
.stApp .yp .scroll-ind span{position:absolute;left:50%;top:7px;width:2px;height:7px;margin-left:-1px;border-radius:2px;
  background:var(--accent);animation:wheel 1.9s ease-in-out infinite}

/* ---------- 5. About ------------------------------------------------------------------ */
.stApp .yp .about-grid{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(32px,6vw,80px);align-items:start}
.stApp .yp .about-copy p{color:var(--muted);font-size:1.1rem;max-width:56ch}
.stApp .yp .about-copy p + p{margin-top:1.1em}
.stApp .yp .about-copy p:first-child{color:var(--text);font-size:1.2rem}
.stApp .yp .about-copy .chips{margin-top:28px}
.stApp .yp .loop{border:1px solid var(--line);border-radius:16px;background:var(--surface);overflow:hidden}
.stApp .yp .loop-step{display:grid;grid-template-columns:22px 1fr;gap:14px;padding:18px 22px;border-bottom:1px solid var(--line);
  transition:background .25s}
.stApp .yp .loop-step:hover{background:var(--surface-2)}
.stApp .yp .loop-step::before{content:"";width:8px;height:8px;margin-top:8px;border-radius:50%;background:var(--accent)}
.stApp .yp .loop-word{font-family:var(--mono);font-size:.85rem;letter-spacing:.12em;font-weight:500}
.stApp .yp .loop-desc{color:var(--muted);font-size:.95rem;margin-top:2px}
.stApp .yp .loop-return{padding:14px 22px;font-family:var(--mono);font-size:.76rem;color:var(--dim)}

/* ---------- 6. Skills ----------------------------------------------------------------- */
.stApp .yp .legend{display:flex;align-items:center;gap:.5rem;margin:-20px 0 26px;font-size:.85rem;color:var(--dim)}
.stApp .yp .legend::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--accent)}
.stApp .yp .skills-grid{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:16px}
.stApp .yp .skills-grid .panel{grid-column:span 2}
.stApp .yp .skills-grid .panel:nth-child(n+4){grid-column:span 3}
.stApp .yp .panel{border:1px solid var(--line);border-radius:16px;background:var(--surface);padding:24px;
  transition:border-color .3s}
.stApp .yp .panel:hover{border-color:var(--line-2)}
.stApp .yp .panel h3{font-size:1rem;font-weight:600;margin-bottom:16px;letter-spacing:-.01em}

/* ---------- 7. Featured project ------------------------------------------------------- */
.stApp .yp .feature{position:relative;border:1px solid var(--line-2);border-radius:24px;overflow:hidden;
  background:linear-gradient(180deg,var(--surface),var(--bg-2));padding:clamp(24px,4.5vw,60px)}
.stApp .yp .feature::before{content:"";position:absolute;right:-120px;top:-160px;width:520px;height:520px;border-radius:50%;
  background:radial-gradient(circle,rgba(124,140,255,.20),transparent 68%);pointer-events:none}
.stApp .yp .feature > *{position:relative}
.stApp .yp .feature-title{font-size:clamp(2.8rem,7vw,5rem);line-height:.98;letter-spacing:-.045em;font-weight:600}
.stApp .yp .feature-sub{margin-top:16px;max-width:52ch;color:var(--muted);font-size:clamp(1.05rem,1.6vw,1.25rem)}
.stApp .yp .feature .btn-row{margin-top:28px}
.stApp .yp .feature-meta{margin-top:18px;font-size:.88rem;color:var(--dim)}
.stApp .yp .feature-cols{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(28px,5vw,64px);
  margin-top:clamp(36px,5vw,60px);align-items:start}
.stApp .yp .story h4{font-size:.8rem;font-family:var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--accent);
  font-weight:500;margin-bottom:8px}
.stApp .yp .story p{color:var(--muted);max-width:56ch}
.stApp .yp .story p + h4{margin-top:24px}
.stApp .yp .features{margin-top:28px;display:grid;grid-template-columns:1fr 1fr;gap:18px 22px}
.stApp .yp .features li{border-left:1px solid var(--line-2);padding-left:14px}
.stApp .yp .features strong{display:block;font-weight:500;font-size:.95rem}
.stApp .yp .features span{display:block;color:var(--dim);font-size:.85rem;margin-top:2px}
.stApp .yp .myrole{margin-top:26px;padding:16px 18px;border:1px solid var(--accent-line);background:var(--accent-soft);
  border-radius:12px;font-size:.95rem}
.stApp .yp .myrole b{font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);
  display:block;margin-bottom:4px;font-weight:500}

.stApp .yp .preview{border:1px solid var(--line-2);border-radius:14px;background:var(--bg);overflow:hidden;
  box-shadow:0 30px 60px -30px rgba(0,0,0,.8)}
.stApp .yp .preview img{width:100%;height:auto}
.stApp .yp .pv-bar{display:flex;align-items:center;gap:6px;padding:12px 14px;border-bottom:1px solid var(--line);background:var(--surface)}
.stApp .yp .pv-bar i{width:9px;height:9px;border-radius:50%;background:var(--line-2)}
.stApp .yp .pv-tabs{display:flex;gap:6px;padding:14px 14px 0}
.stApp .yp .pv-tabs span{padding:.4rem .8rem;border-radius:8px 8px 0 0;font-size:.8rem;color:var(--dim);border:1px solid transparent}
.stApp .yp .pv-tabs span.on{color:var(--text);background:var(--surface);border-color:var(--line);border-bottom-color:transparent}
.stApp .yp .pv-body{margin:0 14px 14px;border:1px solid var(--line);border-radius:0 10px 10px 10px;background:var(--surface);
  padding:18px;display:grid;gap:10px}
.stApp .yp .pv-line{height:9px;border-radius:5px;background:var(--line)}
.stApp .yp .pv-line.a{width:88%} .stApp .yp .pv-line.b{width:64%} .stApp .yp .pv-line.c{width:76%;background:var(--accent-soft);
  border:1px solid var(--accent-line)} .stApp .yp .pv-line.d{width:52%;background:var(--accent-soft);border:1px solid var(--accent-line)}
.stApp .yp .pv-input{margin-top:6px;height:34px;border-radius:9px;border:1px solid var(--line-2);background:var(--bg)}

/* RAG architecture */
.stApp .yp .rag{margin-top:clamp(36px,5vw,60px);border:1px solid var(--line);border-radius:18px;background:rgba(0,0,0,.28);
  padding:clamp(20px,3.2vw,36px)}
.stApp .yp .rag-title{font-size:1.25rem;font-weight:600;letter-spacing:-.02em}
.stApp .yp .rag-note{margin-top:8px;color:var(--muted);max-width:68ch;font-size:.98rem}
.stApp .yp .lane{margin-top:28px}
.stApp .yp .lane-label{font-family:var(--mono);font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent);
  margin-bottom:4px}
.stApp .yp .lane-cap{color:var(--dim);font-size:.86rem;margin-bottom:16px}
.stApp .yp .flow{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px}
.stApp .yp .node{position:relative;border:1px solid var(--line-2);background:var(--surface);border-radius:12px;
  padding:14px 16px;transition:border-color .3s,transform .3s var(--ease)}
.stApp .yp .node:hover{border-color:var(--accent-line);transform:translateY(-3px)}
.stApp .yp .node b{display:block;font-weight:500;font-size:.98rem}
.stApp .yp .node small{display:block;margin-top:3px;font-family:var(--mono);font-size:.72rem;color:var(--dim);line-height:1.4}
.stApp .yp .node.key{border-color:var(--accent-line);background:linear-gradient(180deg,var(--accent-soft),var(--surface))}
.stApp .yp .node:not(:last-child)::after{content:"";position:absolute;top:50%;right:-22px;width:22px;height:2px;margin-top:-1px;
  background:linear-gradient(90deg,var(--line-2) 0%,var(--accent) 50%,var(--line-2) 100%);background-size:220% 100%;
  animation:flow 2.6s linear infinite}
.stApp .yp .node:not(:last-child)::before{content:"";position:absolute;top:50%;right:-22px;margin-top:-4px;
  border:4px solid transparent;border-left:6px solid var(--accent);border-right:0;z-index:1}

/* ---------- 8. Project cards ---------------------------------------------------------- */
.stApp .yp .sub-title{font-size:1.1rem;font-weight:600;margin:clamp(48px,7vw,80px) 0 22px;letter-spacing:-.01em}
.stApp .yp .cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:20px}
.stApp .yp .card{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:18px;background:var(--surface);
  overflow:hidden;transition:transform .35s var(--ease),border-color .3s,box-shadow .35s}
.stApp .yp .card:hover{transform:translateY(-6px);border-color:var(--accent-line);
  box-shadow:0 26px 50px -26px rgba(0,0,0,.85),0 0 60px -40px rgba(124,140,255,.9)}
.stApp .yp .card-media{aspect-ratio:16/9;overflow:hidden;background:var(--bg-2);border-bottom:1px solid var(--line)}
.stApp .yp .card-media > *{width:100%;height:100%;object-fit:cover;transition:transform .8s var(--ease)}
.stApp .yp .card:hover .card-media > *{transform:scale(1.06)}
.stApp .yp .card-body{display:flex;flex-direction:column;gap:10px;padding:22px;flex:1}
.stApp .yp .cat{font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
.stApp .yp .card h3{font-size:1.25rem;font-weight:600;letter-spacing:-.02em}
.stApp .yp .card p.desc{color:var(--muted);font-size:.95rem}
.stApp .yp .card .chips{margin-top:4px}
.stApp .yp .card-links{margin-top:auto;padding-top:14px;display:flex;flex-wrap:wrap;gap:16px}
.stApp .yp .link-arrow{display:inline-flex;align-items:center;gap:.4rem;font-size:.92rem;font-weight:500;color:var(--text);
  transition:color .2s}
.stApp .yp .link-arrow:hover{color:var(--accent)}
.stApp .yp .link-arrow .arr{display:inline-block;transition:transform .25s var(--ease)}

/* ---------- 9. How I build ------------------------------------------------------------ */
.stApp .yp .steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:28px}
.stApp .yp .step{position:relative;border-top:1px solid var(--line-2);padding-top:24px}
.stApp .yp .step::before{content:"";position:absolute;left:0;top:-4px;width:7px;height:7px;border-radius:50%;background:var(--accent)}
.stApp .yp .step-n{font-family:var(--mono);font-size:.78rem;color:var(--accent)}
.stApp .yp .step h3{font-size:1.35rem;font-weight:600;letter-spacing:-.02em;margin:8px 0}
.stApp .yp .step p{color:var(--muted);font-size:.98rem}

/* ---------- 10. Education + certificate ------------------------------------------------ */
.stApp .yp .edu-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(32px,6vw,72px);align-items:start}
.stApp .yp .tl{position:relative;margin-left:6px;padding-left:30px;border-left:1px solid var(--line-2);display:grid;gap:40px}
.stApp .yp .tl-item{position:relative}
.stApp .yp .tl-item::before{content:"";position:absolute;left:-36px;top:7px;width:11px;height:11px;border-radius:50%;
  background:var(--bg);border:2px solid var(--accent)}
.stApp .yp .tl-meta{font-family:var(--mono);font-size:.78rem;color:var(--accent)}
.stApp .yp .tl-item h3{font-size:1.4rem;font-weight:600;letter-spacing:-.02em;margin-top:4px}
.stApp .yp .tl-item .where{color:var(--muted);margin-top:2px}
.stApp .yp .tl-item p.note{color:var(--muted);margin-top:12px;max-width:52ch}
.stApp .yp .tl-item .chips{margin-top:14px}

.stApp .yp .cert{display:grid;grid-template-columns:150px minmax(0,1fr);gap:22px;padding:20px;border:1px solid var(--line-2);
  border-radius:18px;background:linear-gradient(180deg,var(--surface),var(--bg-2));scroll-margin-top:90px;
  transition:border-color .3s}
.stApp .yp .cert:hover{border-color:var(--accent-line)}
.stApp .yp .cert-thumb{display:block;position:relative;aspect-ratio:1/1.414;border-radius:8px;overflow:hidden;
  border:1px solid var(--line-2);background:var(--surface-2)}
.stApp .yp .cert-thumb img{width:100%;height:100%;object-fit:cover;transition:transform .6s var(--ease)}
.stApp .yp .cert:hover .cert-thumb img{transform:scale(1.05)}
.stApp .yp .cert-ph{height:100%;display:grid;place-content:center;padding:12px;text-align:center;color:var(--dim);
  font-family:var(--mono);font-size:.7rem}
.stApp .yp .cert-badge{display:inline-block;font-family:var(--mono);font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;
  color:var(--accent);border:1px solid var(--accent-line);background:var(--accent-soft);padding:.2rem .55rem;border-radius:6px}
.stApp .yp .cert h3{font-size:1.35rem;font-weight:600;letter-spacing:-.02em;margin-top:10px;line-height:1.2}
.stApp .yp .cert .by{color:var(--muted);margin-top:4px;font-size:.95rem}
.stApp .yp .cert .chips{margin-top:14px}
.stApp .yp .cert .chip{font-size:.78rem;padding:.25rem .55rem}
.stApp .yp .cert .btn-row{margin-top:18px}
.stApp .yp .cert .btn{padding:.65rem 1rem;font-size:.88rem}

.stApp .yp .lightbox{position:fixed;inset:0;z-index:1000;display:none;align-items:center;justify-content:center;padding:24px;
  background:rgba(6,7,10,.88);-webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px)}
.stApp .yp .lightbox:target{display:flex;animation:fadein .25s ease both}
.stApp .yp .lb-close-area{position:absolute;inset:0;cursor:zoom-out}
.stApp .yp .lightbox img{position:relative;max-height:90vh;max-width:min(94vw,720px);width:auto;height:auto;border-radius:10px;
  box-shadow:0 40px 100px rgba(0,0,0,.7)}
.stApp .yp .lb-x{position:absolute;top:16px;right:20px;z-index:2;width:42px;height:42px;display:grid;place-items:center;
  border-radius:10px;border:1px solid var(--line-2);background:var(--surface);color:var(--text);font-size:1.3rem;line-height:1}
.stApp .yp .lb-x:hover{border-color:var(--accent-line)}

/* ---------- 11. Exploring -------------------------------------------------------------- */
.stApp .yp .explore{padding:clamp(48px,7vw,80px) 0;border-top:1px solid var(--line)}
.stApp .yp .explore h2{font-size:clamp(1.6rem,3vw,2.2rem);letter-spacing:-.03em;font-weight:600;line-height:1.1}
.stApp .yp .explore p{color:var(--muted);margin:10px 0 24px;max-width:58ch}

/* ---------- 12. Contact + footer -------------------------------------------------------- */
.stApp .yp .contact{position:relative;text-align:center;overflow:hidden;border-top:1px solid var(--line)}
.stApp .yp .contact::before{content:"";position:absolute;left:50%;top:0;width:720px;height:420px;margin-left:-360px;
  background:radial-gradient(ellipse at 50% 0%,rgba(124,140,255,.20),transparent 70%);pointer-events:none}
.stApp .yp .contact .wrap{position:relative}
.stApp .yp .contact h2{font-size:clamp(2.3rem,6.4vw,4.8rem);line-height:1.02;letter-spacing:-.045em;font-weight:600;
  max-width:22ch;margin:0 auto}
.stApp .yp .contact p.lead{margin:22px auto 34px;max-width:46ch;color:var(--muted);font-size:1.12rem}
.stApp .yp .contact .btn-row{justify-content:center}
.stApp .yp .contact .loc{margin-top:28px;font-family:var(--mono);font-size:.78rem;color:var(--dim)}

.stApp .yp .footer{border-top:1px solid var(--line);padding:32px 0 40px;color:var(--dim);font-size:.88rem}
.stApp .yp .footer-in{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:14px 24px}
.stApp .yp .footer b{color:var(--text);font-weight:500}
.stApp .yp .footer-links{display:flex;gap:18px}
.stApp .yp .footer-links a:hover{color:var(--accent)}

/* ---------- 13. Motion (kept to a few moments) ------------------------------------------ */
.stApp .yp .rise{animation:rise .9s var(--ease) both}
.stApp .yp .d1{animation-delay:.05s} .stApp .yp .d2{animation-delay:.15s} .stApp .yp .d3{animation-delay:.28s}
.stApp .yp .d4{animation-delay:.4s}  .stApp .yp .d5{animation-delay:.52s} .stApp .yp .d6{animation-delay:.64s}
.stApp .yp .portrait.rise{animation-name:riseScale;animation-duration:1.1s}

@supports (animation-timeline: view()){
  .stApp .yp .reveal{animation:reveal linear both;animation-timeline:view();animation-range:entry 0% entry 42%}
}
@keyframes rise{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
@keyframes riseScale{from{opacity:0;transform:translateY(26px) scale(.975)}to{opacity:1;transform:none}}
@keyframes reveal{from{opacity:0;transform:translateY(26px)}to{opacity:1;transform:none}}
@keyframes fadein{from{opacity:0}to{opacity:1}}
@keyframes gridmove{to{transform:translateY(56px)}}
@keyframes drift{from{transform:translate3d(0,0,0)}to{transform:translate3d(-40px,36px,0)}}
@keyframes floaty{0%,100%{transform:translateY(0);opacity:.15}50%{transform:translateY(-18px);opacity:.55}}
@keyframes wheel{0%{opacity:0;transform:translateY(0)}30%{opacity:1}100%{opacity:0;transform:translateY(12px)}}
@keyframes flow{from{background-position:220% 0}to{background-position:-20% 0}}

/* ---------- 14. Responsive -------------------------------------------------------------- */
@media (max-width:960px){
  .stApp .yp .hero{min-height:auto;padding:104px 0 88px}
  .stApp .yp .hero-grid,.stApp .yp .about-grid,.stApp .yp .feature-cols,.stApp .yp .edu-grid{grid-template-columns:minmax(0,1fr)}
  .stApp .yp .portrait{justify-self:start;width:min(100%,360px)}
  .stApp .yp .steps{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:40px}
  .stApp .yp .flow{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:22px}
  .stApp .yp .flow .node:nth-child(2)::after,.stApp .yp .flow .node:nth-child(2)::before{display:none}
  .stApp .yp .scroll-ind{display:none}
  .stApp .yp .skills-grid .panel,.stApp .yp .skills-grid .panel:nth-child(n+4){grid-column:span 3}
  .stApp .yp .skills-grid .panel:last-child:nth-child(odd){grid-column:span 6}
}
@media (max-width:600px){
  .stApp .yp .brand .full{display:none}
  .stApp .yp .brand .short{display:inline}
  .stApp .yp .nav-links{gap:0}
  .stApp .yp .nav-links a{padding:.45rem .42rem;font-size:.84rem}
  .stApp .yp .hero .btn-row .btn,.stApp .yp .feature .btn-row .btn,.stApp .yp .contact .btn-row .btn{flex:1 1 100%}
  .stApp .yp .features{grid-template-columns:minmax(0,1fr)}
  .stApp .yp .steps{grid-template-columns:minmax(0,1fr)}
  .stApp .yp .flow{grid-template-columns:minmax(0,1fr)}
  .stApp .yp .flow .node:nth-child(2)::after,.stApp .yp .flow .node:nth-child(2)::before{display:block}
  .stApp .yp .node:not(:last-child)::after{top:100%;right:auto;left:26px;width:2px;height:22px;margin:0;
    background:linear-gradient(180deg,var(--line-2) 0%,var(--accent) 50%,var(--line-2) 100%);background-size:100% 220%;
    animation:flowv 2.6s linear infinite}
  .stApp .yp .node:not(:last-child)::before{top:calc(100% + 16px);right:auto;left:22px;margin:0;
    border:4px solid transparent;border-top:6px solid var(--accent);border-bottom:0}
  .stApp .yp .cert{grid-template-columns:minmax(0,1fr)}
  .stApp .yp .cert-thumb{max-width:170px}
  .stApp .yp .panel{padding:20px}
  .stApp .yp .skills-grid .panel,.stApp .yp .skills-grid .panel:nth-child(n+4),
  .stApp .yp .skills-grid .panel:last-child:nth-child(odd){grid-column:span 6}
}
@keyframes flowv{from{background-position:0 220%}to{background-position:0 -20%}}

@media (prefers-reduced-motion:reduce){
  html,body,.stApp,[data-testid="stAppViewContainer"],[data-testid="stMain"],section.main,.main{scroll-behavior:auto}
  .stApp .yp *,.stApp .yp *::before,.stApp .yp *::after{animation:none!important;transition:none!important}
}
</style>
"""
