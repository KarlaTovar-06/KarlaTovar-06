```aura
<div style={{ display: 'flex', width: '100%', height: '100%', position: 'relative', backgroundColor: '#0B0B14', borderRadius: 24, overflow: 'hidden', border: '1px solid #1F2037' }}>
  <svg width="800" height="220" viewBox="0 0 800 220" style={{ position: 'absolute', top: 0, left: 0 }}>
    <defs>
      <radialGradient id="glowA" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#6D63F5" stopOpacity="0.55" />
        <stop offset="100%" stopColor="#6D63F5" stopOpacity="0" />
      </radialGradient>
      <radialGradient id="glowB" cx="50%" cy="50%" r="50%">
        <stop offset="0%" stopColor="#B794F6" stopOpacity="0.45" />
        <stop offset="100%" stopColor="#B794F6" stopOpacity="0" />
      </radialGradient>
    </defs>
    <style>{`
      @keyframes driftA { 0% { transform: translate(0px, 0px); } 50% { transform: translate(-40px, 18px); } 100% { transform: translate(0px, 0px); } }
      @keyframes driftB { 0% { transform: translate(0px, 0px); } 50% { transform: translate(30px, -16px); } 100% { transform: translate(0px, 0px); } }
      #orbA { animation: driftA 9s ease-in-out infinite; }
      #orbB { animation: driftB 11s ease-in-out infinite; }
    `}</style>
    <ellipse id="orbA" cx="650" cy="50" rx="260" ry="150" fill="url(#glowA)" />
    <ellipse id="orbB" cx="470" cy="210" rx="220" ry="110" fill="url(#glowB)" />
  </svg>
  <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', padding: '0 56px' }}>
    <div style={{ display: 'flex', fontSize: 58, fontWeight: 700, color: '#FFFFFF', letterSpacing: -1.5 }}>Karla Tovar</div>
    <div style={{ display: 'flex', fontSize: 22, color: '#A5A1F8', marginTop: 8 }}>Software Engineer · Frontend</div>
    <div style={{ display: 'flex', fontSize: 16, color: '#6B7280', marginTop: 6 }}>Mexico City</div>
  </div>
</div>
```

```aura
<SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><circle cx='12' cy='12' r='9'/><path d='M3 12h18'/><path d='M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18'/></svg>" text="Portfolio" backgroundColor="#111827" width={150} height={44} />
```

```aura
<SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><rect x='3' y='5' width='18' height='14' rx='2'/><path d='M3 7l9 6l9-6'/></svg>" text="Email" backgroundColor="#111827" width={150} height={44} />
```

```aura
<SocialMediaButton icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'><path d='M8 8l-5 4l5 4'/><path d='M16 8l5 4l-5 4'/></svg>" text="GitHub" backgroundColor="#111827" width={150} height={44} />
```

<p align="center">
  <img src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/terminal.gif" alt="Terminal" width="760" />
</p>

```aura
<div style={{ display: 'flex', flexDirection: 'column', width: '100%', height: '100%', backgroundColor: '#0B0B14', borderRadius: 24, border: '1px solid #1F2037', padding: '28px 40px', justifyContent: 'space-between' }}>
  <div style={{ display: 'flex', alignItems: 'center' }}>
    <div style={{ display: 'flex', width: 140, flexShrink: 0, fontSize: 14, color: '#6B7280', letterSpacing: 1 }}>FRONTEND</div>
    <div style={{ display: 'flex', flexWrap: 'wrap' }}>
      {['React', 'Next.js', 'TypeScript', 'JavaScript', 'Tailwind', 'HTML', 'CSS'].map((t) => (
        <div style={{ display: 'flex', padding: '6px 14px', marginRight: 8, borderRadius: 999, backgroundColor: '#161629', border: '1px solid #2A2A4A', color: '#E5E7EB', fontSize: 15 }}>{t}</div>
      ))}
    </div>
  </div>
  <div style={{ display: 'flex', alignItems: 'center' }}>
    <div style={{ display: 'flex', width: 140, flexShrink: 0, fontSize: 14, color: '#6B7280', letterSpacing: 1 }}>BACKEND</div>
    <div style={{ display: 'flex', flexWrap: 'wrap' }}>
      {['Python', 'PHP', 'Laravel'].map((t) => (
        <div style={{ display: 'flex', padding: '6px 14px', marginRight: 8, borderRadius: 999, backgroundColor: '#161629', border: '1px solid #2A2A4A', color: '#E5E7EB', fontSize: 15 }}>{t}</div>
      ))}
    </div>
  </div>
  <div style={{ display: 'flex', alignItems: 'center' }}>
    <div style={{ display: 'flex', width: 140, flexShrink: 0, fontSize: 14, color: '#6B7280', letterSpacing: 1 }}>MORE</div>
    <div style={{ display: 'flex', flexWrap: 'wrap' }}>
      {['SwiftUI', 'Unity', 'Git', 'Figma'].map((t) => (
        <div style={{ display: 'flex', padding: '6px 14px', marginRight: 8, borderRadius: 999, backgroundColor: '#161629', border: '1px solid #2A2A4A', color: '#E5E7EB', fontSize: 15 }}>{t}</div>
      ))}
    </div>
  </div>
</div>
```

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake.svg" />
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/KarlaTovar-06/KarlaTovar-06/output/snake.svg" />
  </picture>
</p>
